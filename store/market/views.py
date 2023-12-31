from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy
from .models import Product, Category, Basket
from .forms import *

# Create your views here.

# def details(request, product_id):
#     return HttpResponse(f'Текущий ID продукта: {product_id}.')

menu = [
    {'title': 'Home', 'url': 'market:home'},
    {'title': 'Products list', 'url': 'market:products'},
    {'title': 'Basket', 'url': 'market:basket'},
]

def home(request):
    data = {
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'market/home.html', context=data)



class MarketProducts(ListView):
    model = Product   # objects_list
    template_name = 'market/products.html'
    context_object_name = 'products'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Продукты'
        context['menu'] = menu
        context['categories'] = Category.objects.all()

        return context


# def products(request):
#     products = Product.objects.all()
#     categories = Category.objects.all()

#     data = {
#         'menu': menu,
#         'title': 'Все продукты',
#         'products': products,
#         'categories': categories,
#         'category_id': 0,
#     }

#     return render(request, 'market/products.html', context=data)


def basket(request):
    basket_items = Basket.objects.all()

    data = {
        'menu': menu,
        'title': 'Корзина',
        'basket_items': basket_items,
    }

    return render(request, 'market/basket.html', context=data)


class MarketShowProduct(DetailView):
    model = Product  # product
    template_name = 'market/details.html'
    pk_url_kwarg = 'product_id'
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Детали продукта'
        context['menu'] = menu

        return context


# def product_details(request, product_id):
#     product = Product.objects.get(id=product_id)

#     data = {
#         'menu': menu,
#         'title': 'Описание товара',
#         'product': product,
#     }

#     return render(request, 'market/details.html', context=data)


class MarketAddProduct(CreateView):
    form_class = AddProductForm
    template_name = 'market/add-product.html'
    success_url = reverse_lazy('market:products')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Новый продукт'
        context['menu'] = menu

        return context
    


# def add_product(request):
#     if request.method == 'POST':
#         form = AddProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # form_data = form.cleaned_data
#             # Product.ob (name=form_data['name'], description=form_data['description'], price=form_data['price'], category=form_data['category'])
#             # Product.objects.create(**form_data)
#             return redirect('market:products')
#     else:
#         form = AddProductForm()

#     data = {
#         'menu': menu,
#         'title': 'Добавить новый продукт',
#         'form': form,
#     }

#     return render(request, 'market/add-product.html', context=data)



def category_products(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    data = {
        'products': products,
        'categories': categories,
        'menu': menu,
        'title': 'Продукты',
        'category_id': category_id
    }

    return render(request, 'market/products.html', context=data)

