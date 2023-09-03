from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.home, name='home'),
    # path('products/', views.products, name='products'),
    # path('products/details/<int:product_id>/', views.product_details, name='details'),
    path('products/', views.MarketProducts.as_view(), name='products'),
    path('products/details/<int:product_id>/', views.MarketShowProduct.as_view(), name='details'),
    path('products/<int:category_id>/', views.category_products, name='category'),
    path('basket/', views.basket, name='basket'),
    # path('add/', views.add_product, name='add'),
    path('add/', views.MarketAddProduct.as_view(), name='add'),
    # path('edit/<int:product_id>', views.edit, name='edit'),
]