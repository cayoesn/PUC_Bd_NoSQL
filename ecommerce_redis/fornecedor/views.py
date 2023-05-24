from .models import Fornecedor
from rest_framework import generics
from .serializers import FornecedorSerializer
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class FornecedorList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Fornecedor.objects.all().order_by('nome')
    serializer_class = FornecedorSerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL, key_prefix='fornecedor'))
    def dispatch(self, *args, **kwargs):
        return super(FornecedorList, self).dispatch(*args, **kwargs)


class FornecedorDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL, key_prefix='fornecedor'))
    def dispatch(self, *args, **kwargs):
        return super(FornecedorDetail, self).dispatch(*args, **kwargs)


class FornecedorClearCache(generics.ListAPIView):
    cache.clear()
    cache.delete('fornecedor')

    def get(self, request):
        return Response({'Message': 'Cache apagado com sucesso'}, status=status.HTTP_201_CREATED)
