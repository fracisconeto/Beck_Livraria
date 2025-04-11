from re import A
from cryptography.hazmat.primitives.kdf.kbkdf import Mode
from rest_framework.viewsets import ModelViewSet

from core.models import Autor
from core.serializers import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer