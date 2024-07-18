# from products import views
from .views import productDetailes
from django.urls import path


urlpatterns = [
    path('product/', productDetailes.as_view(), name='product-list'),
    path('product/<pk>/', productDetailes.as_view(), name='sku'),
]