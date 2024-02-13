"""Commands for the core app."""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    """Command to create a superuser if 'admin' does not exist."""

    def handle(self, *args, **options):
        username = 'newstore'
        email = 'newstore@admin.com'
        first_name = 'new'
        last_name = 'store'
        password = 'newstoreadmin'

        user_admin = User.objects.create_superuser(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
