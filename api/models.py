from django.db import models
from cpffield import cpffield

class Usuario(models.Model):
    """
        autor: Carlos Arruda
        criado em: 08/2018
    """
    nome = models.CharField(max_length=255)
    cpf_cnpj = cpffield.CPFField('CPF', max_length=14, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)
    atualizado_em = models.DateTimeField(null=True)
    cadatrado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    """
        autor: Carlos Arruda
        criado em: 08/2018
    """
    produto = models.CharField(max_length=255)
    atualizado_em = models.DateTimeField(null=True)
    cadatrado_em = models.DateTimeField(auto_now_add=True)
    cadastro_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='produto')


    def __str__(self):
        return self.nome_produto

class Permissoes(models.Model):
    """
        autor: Carlos Arruda
        criado em: 08/2018
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='permissoes')
    alterar = models.BooleanField()
    criar = models.BooleanField()
    deletar = models.BooleanField()
    is_adim = models.BooleanField()
    atualizado_em = models.DateTimeField(null=True)
    cadatrado_em = models.DateTimeField(auto_now_add=True)
    cadastro_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='permissoes_cadastrado_por')

    def __str__(self):
        return self.usuario

class Voto(models.Model):
    """
        autor: Carlos Arruda
        criado em: 08/2018
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='voto')  
    nota = models.IntegerField(null=False, blank=False) 
    cadatrado_em = models.DateTimeField(auto_now_add=True)
    cadastro_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='voto_cadastrado_por')

    def __str__(self):
        return self.usuario     
