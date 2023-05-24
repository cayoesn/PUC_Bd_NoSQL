from django.urls import path
from .views import ProdutoList


urlpatterns = [
    path('<uuid:idfornecedor>/', ProdutoList.as_view()),
]
