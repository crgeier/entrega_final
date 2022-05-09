from django.urls import path
from django.views.generic import TemplateView
from cocina.views import (inicioView, cocinaView,recetaView,recetaViewDetail, 
                          recetaCreate, recetaUpdate, recetaDelete, 
                          recetaReadDetalle,recetaDetalleReceta, aboutView, usuariosView,
                          inicio)
from cocina.views import recetaCreateForms 
from cocina.views import (LoginView, RegisterView, LogoutView, UsarView)
                        

app_name = "cocina"
urlpatterns = [
    path("blog/", inicioView.as_view(), name="blog"),
    path("inicio/", inicio, name="inicio"),
    path("home/", cocinaView.as_view(), name="home"),
    path("about-us/", aboutView.as_view(), name="about-us"),
    path("pages/", TemplateView.as_view(template_name='cocina/pages.html'), name="pages"),
    path("usuarios/",usuariosView.as_view(), name="usuarios"),
    #CRUD =>
    path("receta/receta-view/", recetaView.as_view(), name="receta-view"),
    path("receta/receta-view-detail/<int:pk>", recetaViewDetail.as_view(), name="receta-view-detail"),
    path("receta/receta-new/", recetaCreate.as_view(), name= "receta-new"),
    path("receta/receta-update/<int:pk>", recetaUpdate.as_view(), name= "receta-update"),
    path("receta/receta-delete/<int:pk>", recetaDelete.as_view(), name= "receta-delete"),
    #creo nueva ruta por crear receta que no me funciona anterior:
    path("receta/receta-new-form/", recetaCreateForms.as_view(), name="receta-new-form"),
    path("receta/detail/", recetaReadDetalle.as_view(), name="receta-detail"),
    #creo una nueva ruta para mostrar que puedo mostrar imágenes de un modelo:
    path("receta/detail1/", recetaDetalleReceta.as_view(), name="receta-detail1"),
    
    #USUARIOS (LOGIN, REGISTER, ETC) =>
    path("usuarios/login/", LoginView.as_view(), name='login'),
    path("usuarios/register/", RegisterView.as_view(), name='register'),
    path("usuarios/logout/", LogoutView.as_view(), name ='logout'),
    #path("usuarios/logout/", LogoutViewCustom.as_view(), name ='logout')
    path("usuarios/edit/", UsarView.as_view(), name='edit')
]













