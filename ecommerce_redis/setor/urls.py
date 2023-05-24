from django.urls import path
from .views import SetorList


urlpatterns = [
    path('<uuid:idfornecedor>/', SetorList.as_view()),
]
