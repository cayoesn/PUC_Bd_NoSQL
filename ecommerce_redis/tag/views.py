from .models import TagPesquisa
from rest_framework import generics
from .serializers import TagPesquisaSerializer
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class TagPesquisaList(generics.ListAPIView):
    queryset = TagPesquisa.objects.all()
    serializer_class = TagPesquisaSerializer

    def get_queryset(self):
        return TagPesquisa.objects.filter(idfornecedor=self.kwargs['idfornecedor']).order_by('valor')

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super(TagPesquisaList, self).dispatch(*args, **kwargs)
