
from rest_framework.serializers import ModelSerializer

from core.models import  Livro

class LivroSerializers(ModelSerializer):
    class Meta:
        model = Livro
        firlds = "__all__"