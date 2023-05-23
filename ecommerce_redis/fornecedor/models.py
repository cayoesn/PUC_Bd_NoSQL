from django.db import models


class Fornecedor(models.Model):
    idfornecedor = models.UUIDField(primary_key=True)
    nome = models.CharField(max_length=255)
    ativo = models.BooleanField()
    tipodocumento = models.CharField(max_length=255)
    nrdocumento = models.CharField(max_length=255)

    class Meta:
        db_table='fornecedor'
