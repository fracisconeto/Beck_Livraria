from cffi import model
from rest_framework.serializers import ModelSerializer

from core.models import Editora

class EditoraSerializers(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"