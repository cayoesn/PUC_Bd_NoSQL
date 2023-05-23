from django.shortcuts import render
from .models import Fornecedor
from rest_framework import generics
from .serializers import FornecedorSerializer
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
class FornecedorList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class FornecedorDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
