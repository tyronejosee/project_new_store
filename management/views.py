"""Views for Management App."""

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from products.models import Product
from management.forms import ProductForm


class ProductListView(ListView):
    """Display a list of available products."""

    model = Product
    template_name = 'management/product_list.html'
    context_object_name = 'products'
    paginate_by = 18

    def get_queryset(self):
        """Select specific fields from the 'Product' model using the 'only' method"""
        return Product.objects.only(
            'title', 'normal_price', 'image', 'stock',
            'featured', 'show_hide'
        )


class ProductCreateView(CreateView):
    """Create a new product."""

    model = Product
    form_class = ProductForm
    template_name = 'management/product_form.html'
    success_url = reverse_lazy('management:prod_list')


class ProductUpdateView(UpdateView):
    """Update the information of a product."""

    model = Product
    form_class = ProductForm
    template_name = 'management/product_form.html'
    success_url = reverse_lazy('management:prod_list')


class ProductDeleteView(DeleteView):
    """Remove an item from the products logically."""

    model = Product
    success_url = None

    def post(self, request, pk, *args, **kwargs):
        """Redefine the POST method for logically deleting the product."""
        object = Product.objects.get(id=pk)
        object.show_hide = False
        object.save()
        return redirect('management:prod_list')
