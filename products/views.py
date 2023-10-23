"""Views for Products App."""

from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.db.models import Q
from products.models import Product, Brand
from products.forms import CategoriesForm


class ProductListView(ListView):
    """Display the complete list of all products, active and in stock."""
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(show_hide=True, stock__gte=1)
    paginate_by = 8
    ordering = ['normal_price']


class ProductDetailView(DetailView):
    """Display the details of a specific product."""
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'


class CategoriesListView(ListView):
    """Display a list of products filtered by categories."""

    model = Product
    template_name = 'products/categories.html'
    context_object_name = 'products'
    paginate_by = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoriesForm()
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(show_hide=True, stock__gte=1)
        form = CategoriesForm(self.request.GET)

        if form.is_valid():
            category = form.cleaned_data['category']
            brand = form.cleaned_data['brand']
            deal = form.cleaned_data['deal']
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']

            if category:
                queryset = queryset.filter(category=category)
            if brand:
                queryset = queryset.filter(brand=brand)
            if deal:
                queryset = queryset.filter(productdeal__deal=deal)
            if min_price:
                queryset = queryset.filter(normal_price__gte=min_price)
            if max_price:
                queryset = queryset.filter(normal_price__lte=max_price)

        return queryset


class RecentProductsListView(ListView):
    """Display a list of recent products."""
    model = Product
    template_name = 'products/recent.html'
    context_object_name = 'products'
    paginate_by = 8
    ordering = ['-created_at', 'title']


def product_search(request):
    """Search bar, filtering by product title and brand."""
    queryset = request.GET.get("search")
    products = Product.objects.filter(show_hide=True)
    if queryset:
        products = Product.objects.filter(
            Q(title__icontains=queryset)
        ).distinct()
    return render(request, 'products/search_bar.html', {'products': products})


class BrandListView(ListView):
    """Display a list of all products from a brand."""
    model = Product
    template_name = 'products/brand.html'
    context_object_name = 'products'

    def get_queryset(self):
        brand_name = self.kwargs['brand_name']
        return Product.objects.filter(brand__name=brand_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['brand'] = Brand.objects.get(name=self.kwargs['brand_name'])
        return context
