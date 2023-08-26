from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *

menu = [
    {'title': 'Home', 'url': 'market:home'},
    {'title': 'Products list', 'url': 'market:products'},
    {'title': 'Basket', 'url': 'market:basket'},
]

# Create your views here.

class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'authe/signup.html'
    success_url = reverse_lazy('market:products')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'
        context['menu'] = menu

        return context