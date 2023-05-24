from django.db import models


class Setor(models.Model):
    idsetor = models.UUIDField(primary_key=True)
    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField()
    idfornecedor = models.UUIDField()

    class Meta:
        db_table='setor'
