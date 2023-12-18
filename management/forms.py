"""Forms for Management App."""

from django import forms
from home.models import Page
from products.models import Product
from core.utils import form_select, form_text, form_number, form_checkbox, form_file, form_textarea


class PageForm(forms.ModelForm):
    """Base form for page update."""

    class Meta:
        """Meta definition for Page form."""
        model = Page
        fields = ['key', 'content', 'image']
        widgets = {
            'key': forms.TextInput(attrs=form_text('Key')),
            'content': forms.Textarea(attrs=form_textarea()),
            'image': forms.ClearableFileInput(attrs=form_file()),
        }


class ProductForm(forms.ModelForm):
    """Base form for product creation and update."""

    class Meta:
        """Meta definition for Product form."""
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs=form_text('Title product')),
            'brand': forms.Select(attrs=form_select()),
            'normal_price': forms.NumberInput(attrs=form_number('Normal price')),
            'deal': forms.Select(attrs=form_select()),
            'category': forms.Select(attrs=form_select()),
            'image': forms.ClearableFileInput(attrs=form_file()),
            'stock': forms.NumberInput(attrs=form_number('Stock')),
            'warranty': forms.Select(attrs=form_select()),
            'featured': forms.CheckboxInput(attrs=form_checkbox()),
            'show_hide': forms.CheckboxInput(attrs=form_checkbox()),
            'description': forms.Textarea(attrs=form_textarea()),
            'specifications': forms.Textarea(attrs=form_textarea()),
        }
