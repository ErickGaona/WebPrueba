
from rest_framework import serializers
from .models import *
class TrabajosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajos
        fields = '__all__'
