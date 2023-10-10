"""Views for Home App."""

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from home.models import Page
from products.models import Product


class FeaturedProductListView(ListView):
    """View for displaying a list of featured products."""
    model = Product
    template_name = 'home/index.html'
    context_object_name = 'featured_products'
    queryset = Product.objects.filter(featured=True)


class AboutView(View):
    """View to display About information."""
    template_name = 'home/about.html'

    def get(self, request):
        """Handles GET requests for the view."""
        about = get_object_or_404(Page, key='about')
        context = {
            'about': about,
        }
        return render(request, self.template_name, context)


class TermsAndConditionsView(View):
    """View to display Terms & Conditions information."""
    template_name = 'home/terms.html'

    def get(self, request):
        """Handles GET requests for the view."""
        terms = get_object_or_404(Page, key='terms')
        context = {
            'terms': terms,
        }
        return render(request, self.template_name, context)


class PrivacyView(View):
    """View to display Privacy information."""
    template_name = 'home/privacy.html'

    def get(self, request):
        """Handles GET requests for the view."""
        privacy = get_object_or_404(Page, key='privacy')
        context = {
            'privacy': privacy,
        }
        return render(request, self.template_name, context)
