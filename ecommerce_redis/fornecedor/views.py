from django.shortcuts import render
from .models import Fornecedor
from rest_framework import generics
from .serializers import FornecedorSerializer


class FornecedorList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    
class FornecedorDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
