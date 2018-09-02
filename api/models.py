# Third
from django.db import models


class Produto(models.Model):
    """
        autor: Carlos Arruda
        criado em: 08/2018
    """
    produto = models.CharField(max_length=255)
    atualizado_em = models.DateTimeField(null=True)
    cadatrado_em = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.produto


class Voto(models.Model):
    """
        autor: Carlos Arruda
        criado em: 08/2018
    """
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='voto')
    nota = models.IntegerField()
    ponto_positivo = models.CharField(max_length=255, null=True, blank=True)
    ponto_negativo = models.CharField(max_length=255, null=True, blank=True)
    cadatrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.produto, self.nota)
