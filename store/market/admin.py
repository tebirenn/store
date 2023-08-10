from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category_id', 'best_before_date')


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id')