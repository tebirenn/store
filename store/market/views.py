from django.shortcuts import render
from .models import Product, Category, Basket

# Create your views here.

# def details(request, product_id):
#     return HttpResponse(f'Текущий ID продукта: {product_id}.')

menu = [
    {'title': 'Home', 'url': 'home'},
    {'title': 'Products list', 'url': 'products'},
    {'title': 'Basket', 'url': 'basket'},
]

def home(request):
    data = {
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'market/home.html', context=data)


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    data = {
        'menu': menu,
        'title': 'Все продукты',
        'products': products,
        'categories': categories,
    }

    return render(request, 'market/products.html', context=data)


def basket(request):
    basket_items = Basket.objects.all()

    data = {
        'menu': menu,
        'title': 'Корзина',
        'basket_items': basket_items,
    }

    return render(request, 'market/basket.html', context=data)