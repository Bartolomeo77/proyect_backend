from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=20)
    correo = models.CharField(max_length=15)
    ususario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=17)
