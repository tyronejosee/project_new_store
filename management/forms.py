"""Forms for Management App."""

from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    """Base form for product creation and update."""

    class Meta:
        model = Product
        fields = ['title', 'brand', 'normal_price', 'deal', 'category', 'image',
                  'stock', 'warranty', 'featured', 'show_hide', 'description', 'specifications']
