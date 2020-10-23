from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['POST'])
def crear_gerente(request):
    gerente_serializer = GerenteSerializer(data=request.data)
    gerente_serializer.is_valid(raise_exception=True)
    return Response(gerente_serializer.data)