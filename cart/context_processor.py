"""Context Processor."""


def total_cart(request):
    """Calculate and return the total cart value."""
    total = 0.0
    if request.user.is_authenticated:
        if "cart" in request.session:
            for key in request.session["cart"]:
                total += float(request.session["cart"][key]["acumulado"])
    return {"total_cart": total}
