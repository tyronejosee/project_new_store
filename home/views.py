"""Views for Home App."""

from django.shortcuts import render
from django.views import View
from home.models import Page
from products.models import Product

def landing_page(request):
    """Simple view to test functionality."""
    featured_products = Product.objects.filter(featured=True)
    return render(request, 'home/index.html', {'featured_products': featured_products})


class AboutView(View):
    """"View to display About information."""
    # Set the template
    template_name = 'home/about.html'

    def get(self, request):
        """Handles GET requests for the view."""
        about = Page.objects.get(pk=2)
        context = {
            'about': about,
        }
        return render(request, self.template_name, context)


class TermsAndConditionsView(View):
    """"View to display Terms & Conditions information."""
    # Set the template
    template_name = 'home/terms.html'

    def get(self, request):
        """Handles GET requests for the view."""
        terms = Page.objects.get(pk=1)
        context = {
            'terms': terms,
        }
        return render(request, self.template_name, context)


class PrivacyView(View):
    """"View to display Privacy information."""
    # Set the template
    template_name = 'home/privacy.html'

    def get(self, request):
        """Handles GET requests for the view."""
        privacy = Page.objects.get(pk=3)
        context = {
            'privacy': privacy,
        }
        return render(request, self.template_name, context)
