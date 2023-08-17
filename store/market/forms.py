from django import forms
from .models import Category

class AddProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())