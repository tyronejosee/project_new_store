"""Forms for Management App."""

from django import forms

from home.models import Page
from products.models import Product, Category, Brand, Deal
from utils.tailwind_classes import (
    form_select,
    form_text,
    form_text_readonly,
    form_number,
    form_checkbox,
    form_file,
    form_textarea,
)


class PageForm(forms.ModelForm):
    """Base form for page update."""

    class Meta:
        model = Page
        fields = ["key", "content", "image"]
        widgets = {
            "key": forms.TextInput(
                attrs={"readonly": "readonly", **form_text_readonly("key")}
            ),
            "content": forms.Textarea(attrs=form_textarea()),
            "image": forms.ClearableFileInput(attrs=form_file()),
        }


class ProductForm(forms.ModelForm):
    """Base form for product creation and update."""

    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]
        widgets = {
            "title": forms.TextInput(attrs=form_text("Title product")),
            "slug": forms.TextInput(
                attrs={"readonly": "readonly", **form_text_readonly("Slug")}
            ),
            "brand": forms.Select(attrs=form_select()),
            "normal_price": forms.NumberInput(
                attrs=form_number("Normal price"),
            ),
            "sale_price": forms.NumberInput(attrs=form_number("Sale price")),
            "deal": forms.Select(attrs=form_select()),
            "category": forms.Select(attrs=form_select()),
            "image": forms.ClearableFileInput(attrs=form_file()),
            "stock": forms.NumberInput(attrs=form_number("Stock")),
            "warranty": forms.Select(attrs=form_select()),
            "featured": forms.CheckboxInput(attrs=form_checkbox()),
            "show_hide": forms.CheckboxInput(attrs=form_checkbox()),
            "description": forms.Textarea(attrs=form_textarea()),
            "specifications": forms.Textarea(attrs=form_textarea()),
        }


class CategoryForm(forms.ModelForm):
    """Base form for category creation and update."""

    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs=form_text("Title")),
            "slug": forms.TextInput(
                attrs={"readonly": "readonly", **form_text_readonly("Slug")}
            ),
            "show_hide": forms.CheckboxInput(attrs=form_checkbox()),
        }


class BrandForm(forms.ModelForm):
    """Base form for brand creation and update."""

    class Meta:
        model = Brand
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs=form_text("Name")),
            "slug": forms.TextInput(
                attrs={"readonly": "readonly", **form_text_readonly("Slug")}
            ),
            "show_hide": forms.CheckboxInput(attrs=form_checkbox()),
        }


class DealForm(forms.ModelForm):
    """Base form for deal creation and update."""

    class Meta:
        model = Deal
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs=form_text("Name")),
            "slug": forms.TextInput(
                attrs={"readonly": "readonly", **form_text_readonly("Slug")}
            ),
            "image": forms.ClearableFileInput(attrs=form_file()),
            "description": forms.Textarea(attrs=form_textarea()),
            "discount": forms.NumberInput(attrs=form_number("Discount")),
            "start_date": forms.TextInput(attrs=form_text("Start Date")),
            "end_date": forms.TextInput(attrs=form_text("End Date")),
            "status": forms.CheckboxInput(attrs=form_checkbox()),
        }
