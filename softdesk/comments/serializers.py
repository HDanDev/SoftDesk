from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
        )
    issue = serializers.ReadOnlyField(
        source='issue.id'
        )

    class Meta:
        model = Comment
        fields = [
            'uuid',
            'description',
            'issue',
            'author',
            'created_time'
            ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        request = self.context.get('request')
        view = self.context.get('view')

        if view and view.action == 'list':
            representation.pop('uuid', None)
            representation.pop('description', None)

        return representation
