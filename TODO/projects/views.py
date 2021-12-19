from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from .serializers import ProjectSerializer, TODOSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
