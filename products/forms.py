"""Forms for Products App."""

from django import forms
from products.models import Category, Brand, Deal
from core.utils import form_select


class CategoriesForm(forms.Form):
    """Base form for category filtering."""

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All Categories",
        widget=forms.Select(attrs=form_select())
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        required=False,
        empty_label="All Brands",
        widget=forms.Select(attrs=form_select())
    )
    deal = forms.ModelChoiceField(
        queryset=Deal.objects.all(),
        required=False,
        empty_label="All Deals",
        widget=forms.Select(attrs=form_select())
    )
    min_price = forms.DecimalField(
        required=False,
        min_value=0,
        max_value=10000,
        widget=forms.NumberInput(attrs={
            'class': 'border p-2 text-gray-700 rounded-lg focus:ring focus:ring-blue-300 focus:outline-none w-full'})
    )
    max_price = forms.DecimalField(
        required=False,
        min_value=0,
        max_value=10000,
        widget=forms.NumberInput(attrs={
            'class': 'border p-2 text-gray-700 rounded-lg focus:ring focus:ring-blue-300 focus:outline-none w-full'})
    )
