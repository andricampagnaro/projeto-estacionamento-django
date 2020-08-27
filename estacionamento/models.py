from django.conf import settings
from django.db import models
from django.utils import timezone


class Vaga(models.Model):
    id_vaga = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_vaga = models.CharField(max_length=6)
    status_vaga = models.BooleanField()
    
    def __str__(self):
        return self.nome_vaga