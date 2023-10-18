"""Wishlist Logic."""


class Wishlist:
    """A simple wishlist implementation."""

    def __init__(self, request):
        self.request = request
        self.session = request.session
        wishlist = self.session.get("wishlist")
        if not wishlist:
            self.session["wishlist"] = {}
            self.wishlist = self.session["wishlist"]
        else:
            self.wishlist = wishlist

    def add(self, product):
        """Add a product to the wishlist."""
        id = str(product.id)
        if id not in self.wishlist.keys():
            self.wishlist[id] = {
                "product_id": product.id,
                "nombre": product.title,
                "acumulado": float(product.normal_price),
                "cantidad": 1,
            }
        else:
            self.wishlist[id]["cantidad"] += 1
            self.wishlist[id]["acumulado"] += float(product.normal_price)
        self.save_wishlist()

    def save_wishlist(self):
        """Save the wishlist to the session."""
        self.session["wishlist"] = self.wishlist
        self.session.modified = True

    def remove(self, product):
        """Remove a product from the wishlist."""
        id = str(product.id)
        if id in self.wishlist:
            del self.wishlist[id]
            self.save_wishlist()
