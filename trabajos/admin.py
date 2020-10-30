from django.contrib import admin
from .models import * 
class TrabajoAdmin(admin.ModelAdmin):
    fields=['nombre','paga']


    
admin.site.register(Trabajos,TrabajoAdmin)
