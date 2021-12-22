from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    filterset_fields = ['first_name', 'username']
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
