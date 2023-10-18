"""Views for Wishlist App."""

from django.shortcuts import render, redirect
from products.models import Product
from wishlist.wishlist import Wishlist


def wishlist(request):
    """Render the wishlist view."""
    products = Product.objects.all()
    return render(request, "users/profile.html", {'products': products})


def add_product(request, product_id):
    """Add a product to the wishlist."""
    wishlist = Wishlist(request)
    product = Product.objects.get(id=product_id)
    wishlist.add(product)
    return redirect("users:profile")


def remove_product(request, product_id):
    """Remove a product from the wishlist."""
    wishlist = Wishlist(request)
    product = Product.objects.get(id=product_id)
    wishlist.remove(product)
    return redirect("users:profile")
