"""Views for Management App."""

from django.views.generic.list import ListView
from products.models import Product


# CRUD for Products

class ProductListView(ListView):
    """Pending."""

    model = Product
    template_name = 'management/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.only(
            'title', 'normal_price', 'image', 'stock',
            'featured', 'show_hide', 'description', 'specifications'
        )


class ProductDetailView():
    """Pending."""
    pass


class ProductCreateView():
    """Pending."""
    pass


class ProductUpdateView():
    """Pending."""
    pass


class ProductDeleteView():
    """Pending."""
    pass
