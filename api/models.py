from django.db import models
from cpffield import cpffield

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    cpf_cnpj = cpffield.CPFField('CPF', max_length=14, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)
    cadatrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.nome