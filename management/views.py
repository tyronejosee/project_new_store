"""Views for Management App."""

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from home.models import Page
from users.models import CustomUser
from products.models import Product
from management.forms import PageForm, ProductForm


class ManagementView(TemplateView):
    """Pending."""
    template_name = 'management/management.html'


class PageListView(ListView):
    """Pending."""

    model = Page
    template_name = 'management/page_list.html'
    context_object_name = 'pages'
    paginate_by = 8


class PageUpdateView(UpdateView):
    """Pending."""

    model = Page
    form_class = PageForm
    template_name = 'management/page_form.html'
    success_url = reverse_lazy('management:page_list')


class UserListView(ListView):
    """Pending."""

    model = CustomUser
    template_name = 'management/user_list.html'
    context_object_name = 'users'


class ProductListView(ListView):
    """Display a list of available products."""

    model = Product
    template_name = 'management/product_list.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        """Select specific fields from the 'Product' model using the 'only' method"""
        return Product.objects.filter(show_hide=True).only(
            'title', 'normal_price', 'image', 'stock',
            'featured', 'show_hide'
        )


class DeletedProductListView(ListView):
    """Display a list of deleted products."""

    model = Product
    template_name = 'management/product_list.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        """Select specific fields from the 'Product' model using the 'only' method"""
        return Product.objects.filter(show_hide=False).only(
            'title', 'normal_price', 'image', 'stock',
            'featured', 'show_hide'
        )


class ProductCreateView(CreateView):
    """Create a new product."""

    model = Product
    form_class = ProductForm
    template_name = 'management/product_form.html'
    success_url = reverse_lazy('management:prod_available')


class ProductUpdateView(UpdateView):
    """Update the information of a product."""

    model = Product
    form_class = ProductForm
    template_name = 'management/product_form.html'
    success_url = reverse_lazy('management:prod_available')


class ProductDeleteView(DeleteView):
    """Remove an item from the products logically."""

    model = Product
    success_url = None

    def post(self, request, pk, *args, **kwargs):
        """Redefine the POST method for logically deleting the product."""
        object = Product.objects.get(id=pk)
        object.show_hide = False
        object.save()
        return redirect('management:prod_available')


class ProductStatusToggleView(DeleteView):
    """Toggle the status of a product (delete or reactivate)."""

    model = Product
    success_url = None

    def post(self, request, pk, action, *args, **kwargs):
        """Toggle the status of the product (delete or reactivate)."""
        product = Product.objects.get(id=pk)

        if action == "delete":
            product.show_hide = False
            product.save()
            return redirect('management:prod_available')
        elif action == "reactivate":
            product.show_hide = True
            product.save()
            return redirect('management:prod_deleted')
