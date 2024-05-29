from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    puesto = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.puesto}'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)
    producto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre