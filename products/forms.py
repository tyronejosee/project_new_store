"""Forms for Products App."""

from django import forms

class ProductSearchForm(forms.Form):
    """Pending."""
    search_query = forms.CharField(label='Search...', max_length=100, required=False)
