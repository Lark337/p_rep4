from django import urls
from django.urls import path
from .views import get_product, get_products, add_product, index

urlpatterns = [
    path('get_product/<int:prodict_id>/',get_product,name = 'get_product'),
    path('get_products/', get_products, name = 'get_products'),
    path('add_product/', add_product, name = 'add_product'),
    path('', index, name = 'index')
]