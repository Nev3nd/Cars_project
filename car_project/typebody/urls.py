from django.urls import path
from .views import (
    TypeBodyListAPIView,
    TypeBodyCreateAPIView,
)

urlpatterns = [
    path('api/cars/typebody/', TypeBodyListAPIView.as_view(), name='typebody-list'),
    path('api/cars/typebody/create/', TypeBodyCreateAPIView.as_view(), name='typebody-create'),
]