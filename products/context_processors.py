"""Context Processors for Products App."""

from products.models import Product


def featured_products(_request):
    """Context processors return a list of products with the 'featured' tag set to True."""
    featured_products = Product.objects.filter(featured=True)[:6]   # First 6 prods
    return {'featured_products': featured_products}
