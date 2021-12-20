from django.core.management.base import BaseCommand


from projects.models import TODO, Project
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(200):
            if not Project.objects.filter(name=f'test_Project_{i}').exists():
                Project.objects.create(name=f'test_Project_{i}')
            else:
                pro = Project.objects.get(name=f'test_Project_{i}')
                pro.users.add(User.objects.get(pk=3))





