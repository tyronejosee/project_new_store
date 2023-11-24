"""Views for Cart App."""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from cart.models import Cart, Wishlist


# Views for Cart

@login_required
def cart(request):
    """Render the cart view and wishlist view."""
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)
    cart_products = cart.products.all()
    cart_count = cart_products.count()

    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlist_products = wishlist.products.all()
    wishlist_count = wishlist.products.count()

    return render(request, "cart/cart.html", {
        'cart': cart, 'cart_products': cart_products, 'cart_count': cart_count,
        'wishlist': wishlist, 'wishlist_products': wishlist_products,
        'wishlist_count': wishlist_count,
        }
    )


@login_required
def add_prod_cart(request, product_id):
    """Add a product to the cart."""
    user = request.user
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cart.add_product(product)
    return redirect("cart:cart")


@login_required
def remove_prod_cart(request, product_id):
    """Remove a product from the cart."""
    user = request.user
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cart.remove_product(product)
    return redirect("cart:cart")


@login_required
def subtract_prod_cart(request, product_id):
    """Subtract a product from the cart."""
    user = request.user
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cart.subtract_product(product)
    return redirect("cart:cart")


@login_required
def clear_cart(request):
    """Clear the cart."""
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart.clear_cart()
    return redirect("cart:cart")


# Views for Wishlist

def add_prod_wishlist(request, product_id):
    """Add a product to the wishlist."""
    user = request.user
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlist.add_product(product)
    return redirect("cart:cart")


def remove_prod_wishlist(request, product_id):
    """Remove a product from the wishlist."""
    user = request.user
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlist.remove_product(product)
    return redirect("cart:cart")
