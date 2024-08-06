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
