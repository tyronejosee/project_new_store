"""Views for Home App."""
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from home.models import Page
from products.models import Product


def landing_page(request):
    """
    Simple view to test functionality.
    """
    featured_products = Product.objects.filter(featured=True)
    return render(request, 'home/index.html', {'featured_products': featured_products})


class TermsAndConditionsListView(ListView):
    model = Page
    template_name = 'home/terms.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Page.objects.filter(pk=1)

class AboutView(View):
    template_name = 'home/about.html'

    def get(self, request):
        """Retrieve the list of products from the database."""
        pages = Page.objects.all()

        context = {
            'pages': pages,
        }

        return render(request, self.template_name, context)
