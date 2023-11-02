"""Views for Home App."""

from django.views.generic import TemplateView, DetailView
from home.models import Page
from products.models import Product


class IndexTemplateView(TemplateView):
    """Renders the site's landing page."""
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_products'] = Product.objects.filter(
            show_hide=True, stock__gte=1
        ).order_by('title')[:12]
        context['recent_products'] = Product.objects.filter(
            show_hide=True, stock__gte=1
        ).order_by('-updated_at')[:12]
        return context


class PageDetailView(DetailView):
    """Pending."""
    model = Page
    template_name = 'home/page_detail.html'
    context_object_name = 'page'

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        return Page.objects.get(key=key)
