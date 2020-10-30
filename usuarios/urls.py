from django.urls import path, include
from usuarios import  api
urlpatterns=[
    
    path('usuario_create/', api.crear_empleado, name='usuario_create'),
    path('listar_usuarios/', api.listar_empleado, name='listar_usarios'),

        

]