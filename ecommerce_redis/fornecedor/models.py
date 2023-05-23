from django.db import models


class Fornecedor(models.Model):
    idfornecedor = models.UUIDField(primary_key=True)
    nome = models.CharField(max_length=255)
    ativo = models.BooleanField()
    
    class Meta:
        db_table='fornecedor'
