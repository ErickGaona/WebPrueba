from django.urls import path, include
from usuarios import  api
urlpatterns=[
        
    path('crear_gerente/', api.crear_gerente, name='crear_gerente')

]