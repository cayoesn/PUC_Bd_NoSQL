from django.urls import path
from .views import TagPesquisaList


urlpatterns = [
    path('<uuid:idfornecedor>/', TagPesquisaList.as_view()),
]
