from django.db import models


class Produto(models.Model):
    idcadastroextraproduto = models.UUIDField(primary_key=True)
    idproduto = models.UUIDField()
    idfornecedor = models.UUIDField()
    disponivel = models.BooleanField()
    descricao = models.CharField(max_length=255)
    descricao_longa = models.CharField(max_length=255)
    ativo = models.BooleanField()

    class Meta:
        db_table = 'cadastro_extra_produto'
