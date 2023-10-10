"""Forms for Cart App."""

from django import forms
from products.models import Product


class AddToCartForm(forms.Form):
    """Pending."""
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        empty_label=None,  # Evita la opción vacía en el campo de selección
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    quantity = forms.IntegerField(
        min_value=1,  # Establece un valor mínimo para la cantidad
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
