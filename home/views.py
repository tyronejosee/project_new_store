"""Views for Home App."""
from django.shortcuts import render


def landing_page(request):
    """
    Simple view to test functionality.
    """
    return render(request, 'pages/index.html', {})
