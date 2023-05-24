from django.urls import include, path
from .views import SetorList


urlpatterns = [
    # path('create/', CustomerCreate.as_view(), name='create-customer'),
    path('<uuid:idfornecedor>/', SetorList.as_view()),

    # path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    # path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
]
