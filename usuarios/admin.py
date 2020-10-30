from django.contrib import admin
from .models import * 
class EmpleadoAdmin(admin.ModelAdmin):
    fields=['nombre','apellido','trabajo','celular','direccion']


    
admin.site.register(Empledo,EmpleadoAdmin)

# Register your models here.