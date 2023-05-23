from rest_framework import serializers
from .models import Fornecedor


class FornecedorSerializer(serializers.ModelSerializer):
    idfornecedor = serializers.UUIDField()
    nome = serializers.CharField(max_length=255)
    ativo = serializers.BooleanField()

    class Meta:
        model = Fornecedor
        fields = ['idfornecedor', 'nome', 'ativo']
        read_only_fields = ['id']

