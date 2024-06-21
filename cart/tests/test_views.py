"""Views Tests for Cart App."""

from django.urls import reverse

from utils.tests import BaseTestCase
from cart.models import Cart, CartItem, Wishlist


class CartViewsTest(BaseTestCase):
    """Tests for Cart views."""

    def test_cart_view(self):
        """Test the cart main view."""
        # Add a product
        url = reverse("cart:add_prod_cart", args=[self.product.id])
        response_add = self.client.get(url)
        self.assertEqual(response_add.status_code, 302)

        # Cart view
        url = reverse("cart:cart")
        response_cart = self.client.get(url)
        self.assertEqual(response_cart.status_code, 200)
        self.assertTemplateUsed(response_cart, "cart/cart.html")

        # Verify that the cart information
        self.assertIn("cart", response_cart.context)
        self.assertIn("cart_items", response_cart.context)
        self.assertIn("wishlist", response_cart.context)
        self.assertIn("wishlist_products", response_cart.context)
        self.assertIn("wishlist_count", response_cart.context)
        self.assertContains(response_cart, "Cart")
        self.assertContains(response_cart, "Wishlist")

    def test_add_product_to_cart_view(self):
        """Test adding a product to the cart."""
        # Add a product
        url = reverse("cart:add_prod_cart", args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # Verify that the product is added
        cart = Cart.objects.get(user=self.user)
        cart_item = CartItem.objects.get(cart=cart, product=self.product)
        self.assertEqual(cart_item.quantity, 1)
        self.assertRedirects(response, reverse("cart:cart"))

    def test_remove_product_from_cart_view(self):
        """Test removing a product from the cart."""
        # Add a product
        url = reverse("cart:add_prod_cart", args=[self.product.id])
        response_add = self.client.get(url)
        self.assertEqual(response_add.status_code, 302)

        # Remove
        url = reverse("cart:remove_prod_cart", args=[self.product.id])
        response_remove = self.client.get(url)
        self.assertEqual(response_remove.status_code, 302)
        self.assertRedirects(response_remove, reverse("cart:cart"))

    def test_subtract_product_from_cart_view(self):
        """Test subtracting a product from the cart."""
        # Add a product
        url = reverse("cart:add_prod_cart", args=[self.product.id])
        response_add = self.client.get(url)
        self.assertEqual(response_add.status_code, 302)

        # Subtract
        url = reverse("cart:subtract_prod_cart", args=[self.product.id])
        response_subtract = self.client.get(url)
        self.assertEqual(response_subtract.status_code, 302)
        self.assertRedirects(response_subtract, reverse("cart:cart"))

    def test_clear_cart_view(self):
        """Test clearing the cart."""
        # Add a product
        url = reverse("cart:add_prod_cart", args=[self.product.id])
        response_add = self.client.get(url)
        self.assertEqual(response_add.status_code, 302)

        # Clear
        url = reverse("cart:clear_cart")
        response_clear = self.client.get(url)
        self.assertEqual(response_clear.status_code, 302)
        self.assertRedirects(response_clear, reverse("cart:cart"))

        # Verify that the cart is empty
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.cart_items.count(), 0)


class WishlistViewsTest(BaseTestCase):
    """Tests for Wishlist views."""

    def test_add_product_to_wishlist_view(self):
        """Test adding a product to the wishlist."""
        # Add a product
        url = reverse("cart:add_prod_wishlist", args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # Verify that the product is added
        wishlist = Wishlist.objects.get(user=self.user)
        self.assertTrue(wishlist.products.filter(pk=self.product.id).exists())
        self.assertRedirects(response, reverse("cart:cart"))

    def test_remove_product_from_wishlist_view(self):
        """Test removing a product from the wishlist."""
        # Add a product
        url = reverse("cart:add_prod_wishlist", args=[self.product.id])
        response_add = self.client.get(url)
        self.assertEqual(response_add.status_code, 302)

        # Remove from wishlist
        url = reverse("cart:remove_prod_wishlist", args=[self.product.id])
        response_remove = self.client.get(url)
        self.assertEqual(response_remove.status_code, 302)

        # Verify that the product is removed
        wishlist = Wishlist.objects.get(user=self.user)
        self.assertFalse(wishlist.products.filter(pk=self.product.id).exists())
        self.assertRedirects(response_remove, reverse("cart:cart"))
