"""Context Processors for Products App."""

from products.models import Product, Category


def featured_products(_request):
    """Context processors return a list of featured products."""
    featured_products = Product.objects.filter(featured=True, show_hide=True, stock__gte=1)[:6]
    return {'featured_products': featured_products}


def categories(_request):
    """Context processor to provide a list of categories."""
    categories_list = Category.objects.filter(show_hide=True)
    return {'categories_list': categories_list}
