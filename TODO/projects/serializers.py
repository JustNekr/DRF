from rest_framework import serializers

from users.serializers import UserModelSerializer
from .models import Project, TODO


class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializer(serializers.ModelSerializer):
    # project = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = TODO
        fields = '__all__'


