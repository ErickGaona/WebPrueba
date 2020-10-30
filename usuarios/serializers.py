
from rest_framework import serializers
from .models import *

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empledo
        fields = '__all__'