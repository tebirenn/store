from django.urls import path
from . import views

app_name = 'authe'

urlpatterns = [
    path('', views.signup, name='signup'),
]