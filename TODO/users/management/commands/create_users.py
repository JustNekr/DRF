from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Creates an admin user if it doesn't exist, and 3 simple users"

    def handle(self, *args, **options):
        User = get_user_model()

        if not User.objects.filter(email='admin@mail.ru').exists():
            User.objects.create_superuser(username='admin',
                                          email='admin@mail.ru',
                                          password='admin')

        for i in range(3):
            if not User.objects.filter(email=f'{i}@mail.ru').exists():
                User.objects.create(username=f'{i}',
                                    email=f'{i}@mail.ru',
                                    password=f'{i}*4')





