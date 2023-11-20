"""Forms for Management App."""

from django import forms
from home.models import Page
from products.models import Product
from core.utils import form_select, form_text_input, form_number_input


class PageForm(forms.ModelForm):
    """Base form for page update."""

    class Meta:
        model = Page
        fields = ['key', 'content', 'image']
        widgets = {
            'key': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'content': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-3xl'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border rounded-3xl'}),
        }


class ProductForm(forms.ModelForm):
    """Base form for product creation and update."""

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs=form_text_input('Title product')),
            'brand': forms.Select(attrs=form_select()),
            'normal_price': forms.NumberInput(attrs=form_number_input('Normal price')),
            'deal': forms.Select(attrs=form_select()),
            'category': forms.Select(attrs=form_select()),
            'image': forms.ClearableFileInput(attrs={'class': 'bg-neutral-100 dark:bg-neutral-900 w-full p-2 rounded-xl'}),
            'stock': forms.NumberInput(attrs=form_number_input('Stock')),
            'warranty': forms.Select(attrs=form_select()),
            'featured': forms.CheckboxInput(attrs={'class': 'bg-neutral-100 dark:bg-neutral-900 form-checkbox'}),
            'show_hide': forms.CheckboxInput(attrs={'class': 'bg-neutral-100 dark:bg-neutral-900 form-checkbox'}),
            'description': forms.Textarea(attrs={}),
            'specifications': forms.Textarea(attrs={}),
        }
