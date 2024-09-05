from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
        )

    class Meta:
        model = Project
        fields = [
            'uuid',
            'name',
            'description',
            'type',
            'author',
            'created_time'
            ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        request = self.context.get('request')
        view = self.context.get('view')

        if view and view.action == 'list':
            representation.pop('description', None)

        return representation
