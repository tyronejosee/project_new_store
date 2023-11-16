"""URLs for Users App."""

from django.urls import path
from users.views import UserProfileView, UserRegistrationView, UserLoginView, user_logout
from cart.views import cart, add_product, remove_product, subtract_product, clear_cart
from wishlist.views import (
    wishlist,
    add_prod_to_wishlist,
    remove_prod_to_wishlist,
    subtract_prod_to_wishlist
    )


app_name = 'users'


urlpatterns = [
    # Users URLs
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),

    # Cart URLs
    path('cart/', cart, name='cart'),
    path('cart/add_product/<int:product_id>/', add_product, name='add_prod_to_cart'),
    path('cart/remove_product/<int:product_id>/', remove_product, name='remove_prod_to_cart'),
    path('cart/subtract_product/<int:product_id>/', subtract_product, name='subtract_prod_to_cart'),
    path('cart/clear_cart/', clear_cart, name='clear_cart'),

    # Wishlist URLs
    path('wishlist/', wishlist, name='wishlist'),
    path('wishlist/add_product/<int:product_id>/', add_prod_to_wishlist, name='add_prod_to_wishlist'),
    path('wishlist/remove_product/<int:product_id>/', remove_prod_to_wishlist, name='remove_prod_to_wishlist'),
    path('wishlist/subtract_product/<int:product_id>/', subtract_prod_to_wishlist, name='subtract_prod_to_wishlist'),
]
