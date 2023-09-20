"""Views for Home App."""
from django.shortcuts import render
from django.views.generic import DetailView

from home.models import Page
from products.models import Product


def landing_page(request):
    """
    Simple view to test functionality.
    """
    featured_products = Product.objects.filter(featured=True)
    return render(request, 'home/index.html', {'featured_products': featured_products})


class TermsAndConditionsView(DetailView):
    model = Page
    template_name = 'home/terms.html'
    context_object_name = 'page'

class AboutView(DetailView):
    model = Page
    template_name = 'home/about.html'
    context_object_name = 'page'
