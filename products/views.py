"""Views for Products App."""

from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from products.models import Product

class StaffRequiredMixin(object):
    """Mixin will require the user to be staff, or else it redirects to the admin login."""
    def dispatch(self, request, *args, **kwargs):
        """Main function of the mixin."""
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) 


class ProductListView(ListView):
    """View generates a list of all products."""
    model = Product
    paginate_by = 12
    template_name = 'products/product_list.html'
    context_object_name = 'products_list'
    queryset = Product.objects.filter(show_hide = True, stock__gte = 1)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'


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
