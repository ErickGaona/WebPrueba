from django.db import models
from trabajos.models import Trabajos

# Create your models here.
class Gerente(models.Model):
    nombre = models.CharField(blank=True, max_length=50)
    apellido = models.CharField(blank=True, max_length=50)
    cargo = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    celular = models.CharField(blank=True, max_length=10)

    class Meta:
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'
        
    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

class Empledo(models.Model):
    nombre = models.CharField(blank=True, max_length=50)
    apellido = models.CharField(blank=True, max_length=50)
    cargo = models.CharField(blank=True, max_length=20)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    celular = models.CharField(blank=True, max_length=10)
    edad = models.IntegerField(blank=True, null=True)

    class Meta: 
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        
    def __str__(self):
        return "%s %s" % (self.longitud, self.latitud)