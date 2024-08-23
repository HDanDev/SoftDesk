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

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        request = self.context.get('request')
        view = self.context.get('view')

        if view and view.action == 'list':
            representation.pop('id', None)
            representation.pop('description', None)
            representation.pop('author', None)
            representation.pop('assignee', None)
            representation.pop('priority', None)
            representation.pop('tag', None)
            representation.pop('status', None)

        return representation
