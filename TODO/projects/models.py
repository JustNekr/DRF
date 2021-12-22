from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=128, blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, unique=False)
    text = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    is_active = models.BooleanField(default=True)


