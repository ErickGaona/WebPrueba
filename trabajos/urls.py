from django.urls import path, include
from trabajos import  api
urlpatterns=[

    path('crear_trabajo/', api.crear_trabajo, name='crear_trabajo')
]