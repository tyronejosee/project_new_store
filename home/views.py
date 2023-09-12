"""Views for Home App."""
from django.shortcuts import render
from products.models import Product


def landing_page(request):
    """
    Simple view to test functionality.
    """
    featured_products = Product.objects.filter(featured=True)
    return render(request, 'pages/index.html', {'featured_products': featured_products})
