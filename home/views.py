"""Views for Home App."""
from django.shortcuts import render
from django.views import View

from home.models import Page
from products.models import Product


def landing_page(request):
    """
    Simple view to test functionality.
    """
    featured_products = Product.objects.filter(featured=True)
    return render(request, 'home/index.html', {'featured_products': featured_products})

class TermsAndConditionsView(View):
    template_name = 'home/terms.html'

    def get(self, request):
        """Retrieve the list of products from the database."""
        terms = Page.objects.get(pk=1)

        context = {
            'terms': terms,
        }

        return render(request, self.template_name, context)

class AboutView(View):
    template_name = 'home/about.html'

    def get(self, request):
        """Retrieve the list of products from the database."""
        about = Page.objects.get(pk=2)

        context = {
            'about': about,
        }

        return render(request, self.template_name, context)
