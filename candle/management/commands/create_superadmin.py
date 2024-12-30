from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    help = "Create a superadmin from environment variables"

    def handle(self, *args, **kwargs):
        username = settings.SUPERADMIN_USERNAME
        email = settings.SUPERADMIN_EMAIL
        password = settings.SUPERADMIN_PASSWORD

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superadmin '{username}' created successfully."))
        else:
            self.stdout.write(self.style.WARNING(f"Superadmin '{username}' already exists."))
