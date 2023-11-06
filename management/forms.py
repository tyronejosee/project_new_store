"""Forms for Management App."""

from django import forms
from home.models import Page
from products.models import Product


class PageForm(forms.ModelForm):
    """Base form for page update."""

    class Meta:
        model = Page
        fields = '__all__'


class ProductForm(forms.ModelForm):
    """Base form for product creation and update."""

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': ''}),
            'brand': forms.Select(attrs={'class': ''}),
            'normal_price': forms.NumberInput(attrs={'class': ''}),
            'deal': forms.Select(attrs={'class': ''}),
            'category': forms.Select(attrs={'class': ''}),
            'image': forms.ClearableFileInput(attrs={'class': ''}),
            'stock': forms.NumberInput(attrs={'class': ''}),
            'warranty': forms.Select(attrs={'class': ''}),
            'featured': forms.CheckboxInput(attrs={'class': ''}),
            'show_hide': forms.CheckboxInput(attrs={'class': ''}),
            'description': forms.Textarea(attrs={'class': ''}),
            'specifications': forms.Textarea(attrs={'class': ''}),
        }
