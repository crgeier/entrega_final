
from django.db import models

class recetas(models.Model):
    name = models.CharField(max_length=40)
    receta = models.TextField()
    image = models.ImageField(upload_to='recetas', null=True, blank= True)

    def __str__(self) -> str:
        return f'{self.name}.'

class foto(models.Model):
    image = models.ImageField(upload_to='fotos', null=True, blank= True)

