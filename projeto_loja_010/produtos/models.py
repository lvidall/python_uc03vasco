# produtos/models.py 
from django.db import models


##
# Aula 11 - 11.01.01
##
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0) # Campo para a quantidade em estoque
    disponivel = models.BooleanField(default=True) # Campo para indicar se o produto está disponível para venda
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True) # Campo para imagem

    # Campos de data para registro de criação e última atualização
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        # Define a ordem padrão dos produtos por nome
        ordering = ['nome']

    def __str__(self):
        return self.nome