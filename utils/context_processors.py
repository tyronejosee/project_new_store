"""Utils: Context Processors"""

from home.models import Company
from products.models import Product, Category
from cart.models import Cart


def company(_request):
    """Context processor for company data."""
    company_data = Company.objects.first()
    return {'company': company_data}


def products_featured(_request):
    """Context processor return a list of featured products."""
    products_featured_list = Product.objects.filter(featured=True, show_hide=True, stock__gte=1)[:6]
    return {'products_featured': products_featured_list}


def products_categories(_request):
    """Context processor to provide a list of categories."""
    products_categories_list = Category.objects.filter(show_hide=True)
    return {'products_categories': products_categories_list}


def cart_items_count(request):
    """Context processor to add the cart items count to the context."""
    user = request.user

    # Get the current user's cart
    cart, created = Cart.objects.get_or_create(user=user)

    # Calculate the total quantity of items in the cart
    cart_items_count_list = sum(item.quantity for item in cart.cart_items.all())

    return {'cart_items_count': cart_items_count_list}
