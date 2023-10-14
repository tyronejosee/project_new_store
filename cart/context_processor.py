"""Context Processor."""


def total_cart(request):
    """Pending."""
    total = 0.0
    if request.user.is_authenticated:
        if "cart" in request.session:
            for key in request.session["cart"]:
                total += float(request.session["cart"][key]["acumulado"])
    return {"total_cart": total}
