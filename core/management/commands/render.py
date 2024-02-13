"""Commands for the core app."""

# import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    """Command to create a superuser if 'admin' does not exist."""

    def handle(self, *args, **options):
        user_admin = User.objects.filter(username='admin')
        if not user_admin:
            # username = os.environ.get('SUPERUSER_USERNAME', 'admin')
            # email = os.environ.get('SUPERUSER_EMAIL', 'admin@admin.com')
            # first_name = os.environ.get('SUPERUSER_FIRST_NAME', 'admin')
            # last_name = os.environ.get('SUPERUSER_LAST_NAME', 'admin')
            # password = os.environ.get('SUPERUSER_PASSWORD', 'adminadmin')

            user_admin = User.objects.create_superuser(
                username = 'newstore',
                email = 'newstore@admin.com',
                first_name = 'new',
                last_name = 'store',
                password = 'newstoreadmin'
            )
