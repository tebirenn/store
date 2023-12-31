from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpUserForm(UserCreationForm): 

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'from-input'})
        } 