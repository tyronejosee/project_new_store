"""URLs for Cart App."""

from django.urls import path

from cart.views import (
    cart,
    add_prod_cart,
    remove_prod_cart,
    subtract_prod_cart,
    clear_cart,
    add_prod_wishlist,
    remove_prod_wishlist,
)

app_name = "cart"

urlpatterns = [
    # Cart URLs
    path(
        "",
        cart,
        name="cart",
    ),
    path(
        "cart/add/<int:product_id>/",
        add_prod_cart,
        name="add_prod_cart",
    ),
    path(
        "cart/remove/<int:product_id>/",
        remove_prod_cart,
        name="remove_prod_cart",
    ),
    path(
        "cart/subtract/<int:product_id>/",
        subtract_prod_cart,
        name="subtract_prod_cart",
    ),
    path(
        "cart/clear/",
        clear_cart,
        name="clear_cart",
    ),
    # Wishlist URLs
    path(
        "wishlist/add/<int:product_id>/",
        add_prod_wishlist,
        name="add_prod_wishlist",
    ),
    path(
        "wishlist/remove/<int:product_id>/",
        remove_prod_wishlist,
        name="remove_prod_wishlist",
    ),
]
