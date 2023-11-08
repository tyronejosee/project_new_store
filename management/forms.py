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
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'brand': forms.Select(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'normal_price': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'deal': forms.Select(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'category': forms.Select(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'stock': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'warranty': forms.Select(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'show_hide': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'specifications': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-3xl'}),
        }
