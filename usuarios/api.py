from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['POST'])
def crear_empleado(request):
    empleado_serializer = EmpleadoSerializer(data=request.data)
    empleado_serializer.is_valid(raise_exception=True)
    empleado_serializer.save()
    return Response(empleado_serializer.data)

@api_view(['GET'])
def listar_empleado(request):
    empleado = Empledo.objects.filter().all()
    empleado_serializer=EmpleadoSerializer(empleado,many=True)
    return Response(empleado_serializer.data)
