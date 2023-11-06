"""Views for Home App."""

from django.views.generic import TemplateView, DetailView
from home.models import Page
from products.models import Product


class IndexTemplateView(TemplateView):
    """Renders the site's index with multiple contexts."""
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        """Override the get_context_data method to send multiple contexts."""
        context = super().get_context_data(**kwargs)

        # Send all the products (first 12 prods.)
        context['all_products'] = Product.objects.filter(
            show_hide=True, stock__gte=1
        ).order_by('title')[:12]

        # Send recent products (first 12 prods.)
        context['recent_products'] = Product.objects.filter(
            show_hide=True, stock__gte=1
        ).order_by('-updated_at')[:12]

        # Send products from the apple brand (first 6 prods.)
        context['apple'] = Product.objects.filter(
            show_hide=True, stock__gte=1, brand__name__iexact='apple'
        ).order_by('-updated_at')[:6]

        # Send products from the samsung brand (first 6 prods.)
        context['samsung'] = Product.objects.filter(
            show_hide=True, stock__gte=1, brand__name__iexact='samsung'
        ).order_by('-updated_at')[:6]

        # Send products from the computer monitors category (first 6 prods.)
        context['computer_monitors'] = Product.objects.filter(
            show_hide=True, stock__gte=1, category__title__iexact='computer monitors'
        ).order_by('-updated_at')[:6]

        return context


class PageDetailView(DetailView):
    """Display details of the static site pages."""

    model = Page
    template_name = 'home/page_detail.html'
    context_object_name = 'page'

    def get_object(self, queryset=None):
        """Gets a key from the HTML and uses it as a filter for searching in the database."""
        key = self.kwargs['key']
        return Page.objects.get(key=key)
