
from rest_framework import serializers
from .models import *
class GerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        fields = '__all__'


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empledo
        fields = '__all__'