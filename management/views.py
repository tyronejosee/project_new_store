"""Views for Management App."""

from django.contrib.auth.decorators import user_passes_test
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from products.models import Product


def is_admin(user):
    """
    Check if the user is an administrator.
    Returns True if the user is an administrator (is_staff).
    """
    return user.is_staff


@user_passes_test(is_admin)
class ProductListView(ListView):
    """Display a list of available products."""

    model = Product
    template_name = 'management/product_list.html'
    context_object_name = 'products'
    paginate_by = 18

    def get_queryset(self):
        """
        Select specific fields from the 'Product' model using the 'only' method
        """
        return Product.objects.only(
            'title', 'normal_price', 'image', 'stock',
            'featured', 'show_hide'
        )


@user_passes_test(is_admin)
class ProductCreateView(CreateView):
    """Pending."""

    model = Product
    form_class = None
    template_name = None
    success_url = None


@user_passes_test(is_admin)
class ProductUpdateView(UpdateView):
    """Pending."""

    model = Product
    form_class = None
    template_name = None
    success_url = None


@user_passes_test(is_admin)
class ProductDeleteView(DeleteView):
    """Pending."""

    model = Product
    success_url = None

    def post(self, request, pk, *args, **kwargs):
        pass
