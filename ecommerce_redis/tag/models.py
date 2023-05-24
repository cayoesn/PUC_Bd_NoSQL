from django.db import models


class TagPesquisa(models.Model):
    idtagpesquisa = models.UUIDField(primary_key=True)
    idfornecedor = models.UUIDField()
    valor = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = 'tag_pesquisa'
