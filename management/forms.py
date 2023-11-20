"""Forms for Management App."""

from django import forms
from home.models import Page
from products.models import Product
from core.utils import form_select, form_text_input, form_number_input, form_checkbox_input


class PageForm(forms.ModelForm):
    """Base form for page update."""

    class Meta:
        """Meta definition for Page form."""
        model = Page
        fields = ['key', 'content', 'image']
        widgets = {
            'key': forms.TextInput(attrs=form_text_input('Key')),
            'content': forms.Textarea(attrs={}),
            'image': forms.ClearableFileInput(attrs=form_select()),
        }


class ProductForm(forms.ModelForm):
    """Base form for product creation and update."""

    class Meta:
        """Meta definition for Product form."""
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs=form_text_input('Title product')),
            'brand': forms.Select(attrs=form_select()),
            'normal_price': forms.NumberInput(attrs=form_number_input('Normal price')),
            'deal': forms.Select(attrs=form_select()),
            'category': forms.Select(attrs=form_select()),
            'image': forms.ClearableFileInput(attrs=form_select()),
            'stock': forms.NumberInput(attrs=form_number_input('Stock')),
            'warranty': forms.Select(attrs=form_select()),
            'featured': forms.CheckboxInput(attrs=form_checkbox_input()),
            'show_hide': forms.CheckboxInput(attrs=form_checkbox_input()),
            'description': forms.Textarea(attrs={}),
            'specifications': forms.Textarea(attrs={}),
        }
