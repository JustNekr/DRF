from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django.conf import settings

from .filters import ProjectFilter
from .models import Project, TODO
from .serializers import ProjectSerializer, TODOSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 10


class TODOPagination(PageNumberPagination):
    page_size = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination
    filterset_class = ProjectFilter


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    pagination_class = TODOPagination
    filterset_fields = ['project']

    def perform_destroy(self, instance):
        instance.is_active = False
