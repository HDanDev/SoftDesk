from rest_framework import serializers
from .models import User, Contributor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'age',
            'can_be_contacted',
            'can_data_be_shared'
            ]


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username'
        )

    class Meta:
        model = Contributor
        fields = [
            'id',
            'user',
            'project',
            'created_time'
            ]
