from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['POST'])
def crear_trabajo(request):
    trabajo_serializer = TrabajosSerializer(data=request.data)
    trabajo_serializer.is_valid(raise_exception=True)
    return Response(trabajo_serializer.data)