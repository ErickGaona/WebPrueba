from django.db import models

# Create your models here.
class Trabajos(models.Model):
    cargo = models.CharField(blank=True, max_length=50)
    cargo = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'
        
    def __str__(self):
        return self.cargo