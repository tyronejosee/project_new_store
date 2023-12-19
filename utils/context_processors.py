"""Utils: Context Processors"""

from cart.models import Cart


def cart_items_context(request):
    """Context processor to add the cart items count to the context."""
    user = request.user

    # Get the current user's cart
    cart, created = Cart.objects.get_or_create(user=user)

    # Calculate the total quantity of items in the cart
    cart_items_count = sum(item.quantity for item in cart.cart_items.all())

    return {'cart_items_count': cart_items_count}
