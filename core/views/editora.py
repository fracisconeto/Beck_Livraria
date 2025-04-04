from rest_framework.viewsets import ModelViewSet

from core.models import Editora
from core.serializers import EditoraSerializers

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializers