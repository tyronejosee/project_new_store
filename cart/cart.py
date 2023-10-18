"""Cart Logic."""


class Cart:
    """A simple shopping cart implementation."""

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def add(self, product):
        """Add a product to the cart."""
        id = str(product.id)
        if id not in self.cart.keys():
            self.cart[id] = {
                "product_id": product.id,
                "nombre": product.title,
                "acumulado": float(product.normal_price),
                "cantidad": 1,
            }
        else:
            self.cart[id]["cantidad"] += 1
            self.cart[id]["acumulado"] += float(product.normal_price)
        self.save_cart()

    def save_cart(self):
        """Save the cart to the session."""
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self, product):
        """Remove a product from the cart."""
        id = str(product.id)
        if id in self.cart:
            del self.cart[id]
            self.save_cart()

    def subtract(self, product):
        """Subtract one unit of a product from the cart."""
        id = str(product.id)
        if id in self.cart.keys():
            self.cart[id]["cantidad"] -= 1
            self.cart[id]["acumulado"] -= float(product.normal_price)
            if self.cart[id]["cantidad"] <= 0:
                self.remove(product)
            self.save_cart()

    def clear(self):
        """Clear the cart."""
        self.session["cart"] = {}
        self.session.modified = True
