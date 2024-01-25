"""Forms for Products App."""

from django import forms
from products.models import Category, Brand, Deal
from utils.tailwind_classes import form_select, form_number


class CategoriesForm(forms.Form):
    """Base form for categories filter."""

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
        min_value=1,
        max_value=10000,
        widget=forms.NumberInput(attrs=form_number('Min Price'))
    )
    max_price = forms.DecimalField(
        required=False,
        min_value=1,
        max_value=10000,
        widget=forms.NumberInput(attrs=form_number('Max Price'))
    )
