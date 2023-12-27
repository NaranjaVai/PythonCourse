from django.db import models

class Persona (models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()

class Empresa(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)

class Producto (models.Model):
    nombre = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=0)