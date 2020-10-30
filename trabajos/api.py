from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['POST'])
def crear_trabajo(request):
    trabajo_serializer = TrabajosSerializer(data=request.data)
    trabajo_serializer.is_valid(raise_exception=True)
    trabajo_serializer.save()
    return Response(trabajo_serializer.data)
@api_view(['GET'])
def listar_trabajo(request):
    trabajo = Trabajos.objects.filter().all()
    trabajo_serializer=TrabajosSerializer(trabajo,many=True)
    return Response(trabajo_serializer.data)
