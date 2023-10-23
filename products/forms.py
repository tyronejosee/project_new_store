"""Forms for Products App."""

from django import forms
from .models import Category, Brand, Deal


class CategoriesForm(forms.Form):
    """Base form for category filtering."""

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All Categories",
        widget=forms.Select(attrs={
            'class': 'border p-2 text-gray-700 rounded-lg focus:ring focus:ring-blue-300 focus:outline-none w-full'})
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        required=False,
        empty_label="All Brands",
        widget=forms.Select(attrs={
            'class': 'border p-2 text-gray-700 rounded-lg focus:ring focus:ring-blue-300 focus:outline-none w-full'})
    )
    deal = forms.ModelChoiceField(
        queryset=Deal.objects.all(),
        required=False,
        empty_label="All Deals",
        widget=forms.Select(attrs={
            'class': 'border p-2 text-gray-700 rounded-lg focus:ring focus:ring-blue-300 focus:outline-none w-full'})

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
