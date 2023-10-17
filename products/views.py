"""Views for Products App."""

from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.db.models import Q
from products.models import Product


class ProductListView(ListView):
    """ListView for displaying active products with stock greater than or equal to 1."""
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(show_hide=True, stock__gte=1)
    paginate_by = 8


class ProductDetailView(DetailView):
    """DetailView that expands product information."""
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'


class RecentProductsListView(ListView):
    """View to display a list of recent products."""
    model = Product
    template_name = 'products/recent_products.html'
    context_object_name = 'products'
    ordering = ['-created_at', 'title']


def product_search(request):
    """Search bar, filtering by product title and description."""
    queryset = request.GET.get("search")
    products = Product.objects.filter(show_hide=True)
    if queryset:
        products = Product.objects.filter(
            Q(title__icontains=queryset) |
            Q(brand__name__icontains=queryset)
        ).distinct()
    return render(request, 'products/product_search.html', {'products': products})
