from django.db import models
from trabajos.models import Trabajos

# Create your models here.
class Empledo(models.Model):
    nombre = models.CharField(blank=True, max_length=50)
    apellido = models.CharField(blank=True, max_length=50)
    trabajo = models.ForeignKey(Trabajos, on_delete=models.CASCADE)
    celular = models.CharField(blank=True, max_length=10)
    direccion = models.CharField(blank=True, null=True,max_length=50)

    class Meta: 
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        
    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)