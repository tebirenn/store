from django import forms
from .models import *

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'description', 'price', 'category']
        # fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'textarea-form'})
        }

    # name = forms.CharField(max_length=50)
    # description = forms.CharField(widget=forms.Textarea)
    # price = forms.FloatField()
    # category = forms.ModelChoiceField(queryset=Category.objects.all())