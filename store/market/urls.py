from django.urls import path
from . import views


urlpatterns = [
    # path('details/<int:product_id>/', views.details),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('basket/', views.basket, name='basket'),
]