from django.db import models

from users.models import User

"""
Создать API для моделей Projects и ToDo. Пока можно использовать ViewSets по аналогии с моделью User.
При сериализации моделей выбрать нужный вид для связанных моделей.

(Задание со *) На стороне клиента используется camelCase в отличие от snake_case, который мы используем в python. 
Реализовать представление данных в виде camelCase (https://www.django-rest-framework.org/api-guide/parsers/#camelcase-json).
"""


class Project(models.Model):
    """
    модель Project. Это проект, для которого записаны TODO.
    У него есть название, может быть ссылка на репозиторий и набор пользователей,
    которые работают с этим проектом. Создать модель, выбрать подходящие типы полей и связей с другими моделями.
    """
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=128, blank=True)
    users = models.ManyToManyField(User)


class TODO(models.Model):
    """
    модель TODO. Это заметка. У ToDo есть проект, в котором сделана заметка, текст заметки,
    дата создания и обновления, пользователь, создавший заметку. Содержится и признак — активно TODO или закрыто.
    Выбрать подходящие типы полей и связей с другими моделями.
    """
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    text = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

