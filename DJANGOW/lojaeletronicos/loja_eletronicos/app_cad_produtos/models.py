from django.db import models

# Create your models here.
class Produto(models.Model):
    id_produtoeletronico = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=255)
    marca = models.TextField(max_length=255)
    valor = models.FloatField()
    estoque = models.IntegerField()