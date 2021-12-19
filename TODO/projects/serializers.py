from rest_framework import serializers
from .models import Project, TODO


class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializer(serializers.ModelSerializer):
    project = serializers.HyperlinkedRelatedField(read_only=True, view_name='project')
    user = serializers.StringRelatedField()

    class Meta:
        model = TODO
        fields = '__all__'


