from django.urls import include, path
from .views import FornecedorList, FornecedorDetail, FornecedorClearCache


urlpatterns = [
    # path('create/', CustomerCreate.as_view(), name='create-customer'),
    path('', FornecedorList.as_view()),
    path('<uuid:pk>/', FornecedorDetail.as_view()),
    path('clear-cache', FornecedorClearCache.as_view()),
    # path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    # path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
]
