from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
        )
    assignee = serializers.ReadOnlyField(
        source='assignee.username'
        )

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'project',
            'author',
            'assignee',
            'priority',
            'tag',
            'status',
            'created_time'
            ]
