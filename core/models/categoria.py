from django.db import models

from dill.tests.test_functors import f


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao}({self.id})"