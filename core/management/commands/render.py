"""Commands for the core app."""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    """Command to create a superuser if "admin" does not exist."""

    help = "Create a superuser if 'admin' does not exist"

    def handle(self, *args, **options):
        user_admin = User.objects.filter(username="newstore")
        if not user_admin:
            user_admin = User.objects.create_superuser(
                username="newstore",
                email="newstore@admin.com",
                first_name="new",
                last_name="store",
                password="newstoreadmin",
            )
            self.stdout.write(
                self.style.SUCCESS("Superuser created successfully."),
            )
