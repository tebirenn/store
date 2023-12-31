from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
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
    success_url = reverse_lazy('authe:signin')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'
        context['menu'] = menu

        return context
    

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('market:products')
    

class SignInUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authe/signin.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Авторизация'
        context['menu'] = menu

        return context
    
    
    def get_success_url(self):
        return reverse_lazy('authe:profile')
    

def signout_user(request):
    logout(request)
    return redirect('authe:signin')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('authe:signin')

    data = {
        'title': 'Профиль',
        'menu': menu
    }

    return render(request, 'authe/profile.html', context=data)