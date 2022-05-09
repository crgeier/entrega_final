from distutils.command.upload import upload
from django import forms

class recetaForms(forms.Form):
    name = forms.CharField()
    receta = forms.CharField(max_length=500)
    image = forms.ImageField()
