from multiprocessing import context
from re import template
from typing import Any, Dict
from unicodedata import name
from attr import fields
from django import forms
from django.urls import reverse_lazy
#importo parte de CRUD
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
#importo parte de login, register y logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, UserChangeForm)
from django.contrib.auth import login, logout, authenticate
from final.users.models import (User, Avatar)
#importo mixin y decoradores
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#importo modelos / formularios
from cocina.models import recetas, foto
from cocina.forms import recetaForms
from django import forms

#PAGINA INICIO 
class inicioView(TemplateView):
    template_name = 'cocina/inicio.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

@login_required
def inicio(request):
    return render('cocina/home.html')

#ABOUT-US
class aboutView(TemplateView):
    template_name='cocina/about-us.html'
    
    def get(self, request):
        context = {
            
            'image' : foto.objects.all().last().image.url                      
        }
        return render(request, self.template_name, context)


#Arreglo para REGISTER por trabajar con COOKIECUTTER
      
class UserCreationFormCustom(UserCreationForm):
    def save(self, commit: bool=True) -> User:
        print(self.__dict__)
        self.data
        user = User.objects.create(
            username = self.data['username'],
            password = self.data['password1'],
        )
        return user

class UserChangeFormCustom(UserChangeForm):
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = "__all__"
        
#Clases de CRUD
class cocinaView(TemplateView):
    template_name = 'cocina/index.html'

    def get(self, request, status=None):
        context = {
            'imagen': Avatar.objects.filter(user=request.user).last().imagen.url
        }
        return render(request, self.template_name, context)

class recetaView(ListView):
    model = recetas
    template_name = 'cocina/receta/index.html'

class recetaViewDetail(DetailView):
    model = recetas
    template_name = 'cocina/receta/index-detail.html'
   


#ESTE NO ME FUNCIONA
class recetaCreate(CreateView):
    model = recetas
    template_name = 'cocina/receta/create.html'
    success_url = "/" #acá tengo que poner que vuelva a la página que quiero!!
    fields = ['name', 'receta', 'image']
    
class recetaUpdate(UpdateView):
    model = recetas
    template_name = 'cocina/receta/update-receta.html'
    success_url = "/" #acá tengo que poner que vuelva a la página que quiero!!
    fields = ['name', 'receta', 'image']

class recetaDelete(DeleteView):
    model = recetas
    template_name = 'cocina/receta/delete-receta.html'
    success_url = "/" #acá tengo que poner que vuelva a la página que quiero!!

#CREO NUEVO CRUD READ
class recetaReadDetalle(TemplateView):
    template_name = 'cocina/receta/detail.html'
    
    def get(self, request):
        
        context = {
            'recetas' : recetas.objects.all(),
            
        }
        return render(request, self.template_name, context)

#NO PUEDO MOSTRAR IMAGEN ASÍ QUE MUESTRO QUE PUEDO HACERLO CON UN CASO:
class recetaDetalleReceta(TemplateView):
    template_name = 'cocina/receta/detail1.html'
    def get(self, request):
        context = {
            'recetas' : recetas.objects.all()
            # 'recetas' : recetas.objects.filter(name=name)
            # este si!! 'recetas' : recetas.objects.filter(name="Tarta de Manzana")
            # 'imagenes' : recetas.objects.filter(name="Humita en Olla")[0].image.url  
            # 'image' : recetas.objects.all().last().image.url                   
        }
        return render(request, self.template_name, context)


#CRUD CREATE -> creo un nuevo form para crear porque no me funciona el CreateView

class recetaCreateForms(TemplateView):
    template_name = 'cocina/receta/createForm.html'
    def get(self, request):
         context = {
             'form': recetaForms()
         }
         return render(request, self.template_name, context)

    def post(self, request):
          object_receta1 = request.POST
          receta1 = recetas(
              name = object_receta1.get('name'),
              receta = object_receta1.get('receta'),
              image = object_receta1.get('image'),
          ) 
          receta1.save()

          context = {
              'form' : recetaForms()
          }
          return render(request, self.template_name, context)

# Comienzo con LOGIN
# acá tengo que ver si uso el botón de arriba o no y si queda como página de inicio!
class LoginView(TemplateView):
    template_name = 'cocina/usuarios/login.html'
    
    def get(self, request):
        context = {
            'form': AuthenticationForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form:
            user = request.POST.get('username')
            password = request.POST.get('password')

            user_auth = authenticate(username=user, password=password)
            if user_auth:
                login(request, user_auth)
                return render(request, self.template_name, context={'message': f'Bienvenido: {user}'})
            else:
                return render(request,self.template_name, context={'message':'Usuario Inválido'})
        else:
            # return redirect('http:google.com') esto lo tengo que ver!!
            return render(request,self.template_name, context={'message':'Formulario Equivocado'})

class RegisterView(TemplateView):
    template_name = 'cocina/usuarios/register.html'
    def get(self, request):
        context = {
            'form': UserCreationFormCustom()
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = UserCreationFormCustom(request.POST)
        if form:
            form.save()
            return render(request, self.template_name, context={'message':'Usuario Registrado Correctamente'})
        else:
            return render(request, self.template_name, context={'message': 'Ocurrió un error!'})

class UsarView(LoginRequiredMixin, TemplateView):
    template_name = 'cocina/usuarios/edit.html'
    
    def get(self, request):
        
        context = {
            'form': UserChangeFormCustom(
                initial={
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email
                }
            )
        }
        return render(request, self.template_name, context)

    def post(self, request):
        
        form = UserChangeFormCustom(request.POST)
        
        if form.is_valid:
            
            user_update_info = form.cleaned_data
            user = request.user
            user.email = user_update_info.get('email')
            user.password1 = user_update_info.get('password1')
            user.password2 = user_update_info.get('password2')
            user.save()
            
            context={
                'form': UserChangeFormCustom(
                    initial={
                        'first_name': request.user.first_name,
                        'last_name': request.user.last_name,
                        'email': request.user.email
                    }
                )
            }
        return render(request, self.template_name, context)

# PAGINAS VINCULADAS CON USUARIOS

class usuariosView(TemplateView):
    template_name = 'cocina/usuarios.html'
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)