from django.db import models

# Create your models here.
class usuarios(models.Model):
    username = models.CharField(max_length=50)
    password = models.TextField(max_length=30)
    

class eventos(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=250)
    fecha = models.DateTimeField(True)
    hora = models.TimeField(blank=True)
    lugar = models.CharField(max_length=50)
    capacidad_max = models.BooleanField(True)
    usuarios = models.ForeignKey(usuarios, on_delete=models.CASCADE)