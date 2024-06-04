from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField()
    local = models.CharField(max_length=200)

    def __str__(self):
        return self.nome