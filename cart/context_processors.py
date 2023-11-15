"""Context Processors for Cart App."""


from cart.models import Cart


def cart_total_price(request):
    """Context processors to retrieve the total price of products in the cart."""
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user).first()
        total_price = user_cart.total_price() if user_cart else 0
    else:
        total_price = 0

    return {'total_price': total_price}
