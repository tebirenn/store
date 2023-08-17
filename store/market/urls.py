from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/details/<int:product_id>/', views.product_details, name='details'),
    path('basket/', views.basket, name='basket'),
    path('add/', views.add_product, name='add'),
]