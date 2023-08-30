"""Views for Accounts App."""
from django.shortcuts import render


def accounts_main(request):
    """
    Simple view to test functionality.
    """
    return render(request, 'pages/accounts.html', {})
