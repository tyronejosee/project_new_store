"""Views for Products App."""

from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.db.models import Q
from products.models import Product, Brand, Deal, Category
from products.forms import CategoriesForm


class ProductListView(ListView):
    """Display the complete list of all products, active and in stock."""
    model = Product
    template_name = 'components/section.html'
    context_object_name = 'products'
    paginate_by = 18

    def get_queryset(self):
        queryset = Product.objects.filter(show_hide=True, stock__gte=1)
        return queryset


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
                queryset = queryset.filter(deal=deal)
            if min_price:
                queryset = queryset.filter(normal_price__gte=min_price)
            if max_price:
                queryset = queryset.filter(normal_price__lte=max_price)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoriesForm()
        context['deals'] = Deal.objects.all()
        return context


class DealListView(ListView):
    """View to display a list of deals."""
    model = Deal
    template_name = 'products/deal_list.html'
    context_object_name = 'deals'


class DealDetailView(DetailView):
    """View to display in detail all the products of an offer."""
    model = Deal
    template_name = 'products/deal_detail.html'
    context_object_name = 'deal'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the products as context
        context['products'] = self.object.products.all()
        return context


class RecentProductsListView(ListView):
    """Display a list of recent products."""
    model = Product
    template_name = 'components/section.html'
    context_object_name = 'products'
    paginate_by = 18

    def get_queryset(self):
        queryset = Product.objects.filter(show_hide=True, stock__gte=1)
        queryset = queryset.order_by('-updated_at', 'title')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Recent Products'
        return context


class CategoryFilterListView(ListView):
    """Display a list of all products from a category."""
    model = Product
    template_name = 'components/section.html'
    context_object_name = 'products'
    paginate_by = 18
    ordering = ['title']

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Product.objects.filter(category__slug=category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        context['category'] = category
        context['title'] = f'{category.title}'
        return context


class BrandFilterListView(ListView):
    """Display a list of all products from a brand."""
    model = Product
    template_name = 'components/section.html'
    context_object_name = 'products'
    paginate_by = 18
    ordering = ['title']

    def get_queryset(self):
        brand_slug = self.kwargs['brand_slug']
        return Product.objects.filter(brand__slug=brand_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = Brand.objects.get(slug=self.kwargs['brand_slug'])
        context['brand'] = brand
        context['title'] = (f'{brand.name}')
        return context


def product_search(request):
    """Search bar, filtering by product title and brand."""
    queryset = request.GET.get("search")
    products = Product.objects.filter(show_hide=True)

    if queryset:
        products = Product.objects.filter(
            Q(title__icontains=queryset) |
            Q(brand__name__icontains=queryset)
        ).distinct()

    results = products.count()

    return render(request, 'components/section.html', {
        'products':products,
        'title':queryset,
        'results':results
    })
