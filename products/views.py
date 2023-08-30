"""Views for Products App."""
from django.shortcuts import render


def products_main(request):
    """
    Simple view to test functionality.
    """
    return render(request, 'pages/products.html', {})
