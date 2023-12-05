"""Models Tests for the Cart App."""

from django.test import TestCase
from users.models import CustomUser
from products.models import Product
from cart.models import Cart, CartItem, Wishlist


class CartModelTest(TestCase):
    """Tests for the Cart model."""

    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser')

    def test_cart_creation(self):
        """Verifies the correct creation of a cart."""
        cart = Cart.objects.create(user=self.user)
        self.assertEqual(cart.user, self.user)
        self.assertEqual(str(cart), f'Cart of {self.user.username}')


class CartItemModelTest(TestCase):
    """Tests for the CartItem model."""

    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser')
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(title='Test Product', normal_price=10)

    def test_cart_item_creation(self):
        """Verifies the correct creation of cart_item."""
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        self.assertEqual(cart_item.cart, self.cart)
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(str(cart_item), f'{self.cart.user} - {cart_item.quantity}')

    def test_add_to_cart_method(self):
        """Verifies the functionality of the 'add_to_cart' method."""
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=1)
        cart_item.add_to_cart(quantity=3)
        self.assertEqual(cart_item.quantity, 4)


class WishlistModelTest(TestCase):
    """Tests for the Wishlist model."""

    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser')
        self.product = Product.objects.create(title='Test Product', normal_price=10)

    def test_wishlist_creation(self):
        """Verifies the correct creation of wishlist."""
        wishlist = Wishlist.objects.create(user=self.user)
        wishlist.add_product(self.product)
        self.assertEqual(wishlist.user, self.user)
        self.assertTrue(self.product in wishlist.products.all())
        self.assertEqual(str(wishlist), f'{self.user.username} (1 prods)')
