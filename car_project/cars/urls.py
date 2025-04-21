from django.urls import path
from .views import (
    CarListAPIView,
    CarDetailAPIView,
    CarCreateAPIView,
    CarUpdateAPIView,
    CarDeleteAPIView,
)

urlpatterns = [
    path('api/cars/', CarListAPIView.as_view(), name='car-list'),
    path('api/cars/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail'),
    path('api/cars/create/', CarCreateAPIView.as_view(), name='car-create'),
    path('api/cars/update/<int:pk>/', CarUpdateAPIView.as_view(), name='car-update'),
    path('api/cars/delete/<int:pk>/', CarDeleteAPIView.as_view(), name='car-delete'),
]