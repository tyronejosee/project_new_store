class DealTemplateView(TemplateView):
    """Pending."""
    template_name = 'products/deal.html'

    def get_context_data(self, **kwargs):
        """Override the get_context_data method to send multiple contexts."""
        context = super().get_context_data(**kwargs)

        context['back_to_school'] = Product.objects.filter(
            show_hide=True, stock__gte=1, deal__name__iexact='back-to-school'
        ).order_by('-updated_at')[:6]

        context['fathers_day'] = Product.objects.filter(
            show_hide=True, stock__gte=1, deal__name__iexact='Father_s Day'
        ).order_by('-updated_at')[:6]

        context['summer_sales'] = Product.objects.filter(
            show_hide=True, stock__gte=1, deal__name__iexact='Summer Sales'
        ).order_by('-updated_at')[:6]

        return context

---

from django.utils.text import slugify
from products.models import Brand

entries = Brand.objects.filter(slug__isnull=True)

for entry in entries:
    entry.slug = slugify(entry.name)
    entry.save()

---