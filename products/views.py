"""Views for Products App."""

from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from django.db.models import Q
from products.models import Product

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
    queryset = request.GET.get("search")
    products = Product.objects.filter(show_hide = True)
    if queryset:
        products = Product.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset)
        ).distinct()
    return render(request, 'products/product_search.html', {'products':products})
