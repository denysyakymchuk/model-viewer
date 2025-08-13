from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Retrieve superuser details from project settings
        username = getattr(settings, "DJANGO_SUPERUSER_USERNAME", None)
        email = getattr(settings, "DJANGO_SUPERUSER_EMAIL", None)
        password = getattr(settings, "DJANGO_SUPERUSER_PASSWORD", None)

        try:
            # Check if a user with the provided username already exists
            if not User.objects.filter(username=username).exists():
                u = User.objects.create_superuser(username, email, password)
                print(f"===================================")
                print(f"A superuser '{username}' was created")
                print(f"===================================")
            else:
                print(f"===================================")
                print("Admin user found. Skipping super user creation")
                print(f"===================================")
        except Exception as e:
            print(f"There was an error: {e}")
