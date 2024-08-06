from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
        )

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'type',
            'author',
            'created_time'
            ]
