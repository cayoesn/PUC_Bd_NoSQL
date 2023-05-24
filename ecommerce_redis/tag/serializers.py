from rest_framework import serializers
from .models import TagPesquisa


class TagPesquisaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagPesquisa
        fields = '__all__'
