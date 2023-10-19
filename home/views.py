"""Views for Home App."""

from django.views.generic import ListView, DetailView
from home.models import Page
from products.models import Product


class FeaturedProductListView(ListView):
    """View for displaying a list of featured products."""
    model = Product
    template_name = 'home/index.html'
    context_object_name = 'featured_products'
    queryset = Product.objects.filter(featured=True)


class PageDetailView(DetailView):
    """Pending."""
    model = Page
    template_name = 'home/page_detail.html'
    context_object_name = 'page'

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        return Page.objects.get(key=key)
