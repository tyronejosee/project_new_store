"""Views for Products App."""

from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from products.models import Product
from products.forms import ProductSearchForm

class StaffRequiredMixin(object):
    """Mixin will require the user to be staff, or else it redirects to the admin login."""
    def dispatch(self, request, *args, **kwargs):
        """Main function of the mixin."""
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) 


class ProductListView(View):
    """View generates a list of all products."""
    template_name = 'products/product_list.html'

    def get(self, request):
        """Retrieve the list of products from the database."""
        products = Product.objects.all()

        context = {
            'products': products,
        }

        return render(request, self.template_name, context)


def product_search(request):
    """Search Bar."""
    form = ProductSearchForm(request.GET)
    products = Product.objects.all()

    if form.is_valid() and form.cleaned_data['search_query']:
        search_query = form.cleaned_data['search_query']
        products = products.filter(name__icontains=search_query)

    return render(request, 'products/product_search.html', {'products': products, 'form': form})
