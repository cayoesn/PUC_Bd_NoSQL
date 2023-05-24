from .models import Setor
from rest_framework import generics
from .serializers import SetorSerializer
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class SetorList(generics.ListAPIView):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

    def get_queryset(self):
        return Setor.objects.filter(idfornecedor=self.kwargs['idfornecedor']).order_by('descricao')

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super(SetorList, self).dispatch(*args, **kwargs)
