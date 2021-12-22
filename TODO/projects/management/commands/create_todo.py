from django.core.management.base import BaseCommand


from projects.models import TODO, Project
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.get(username='nkr')
        for i in range(200):
            if not TODO.objects.filter(text=f'test_TODO_{i}').exists():
                TODO.objects.create(text=f'test_TODO_{i}',
                                    user_id=user.id,
                                    project_id=1)





