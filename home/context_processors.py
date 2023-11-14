"""Context Processors for Home App."""


from home.models import Company


def company_context(request):
    """Context processors for company data."""
    company = Company.objects.first()
    return {'company': company}
