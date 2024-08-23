from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import User, Contributor


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'age',
            'can_be_contacted',
            'can_data_be_shared'
            ]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = [
            'id',
            'username',
            'email',
            'age',
            'can_be_contacted',
            'can_data_be_shared'
            ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        request = self.context.get('request')
        view = self.context.get('view')

        if view and view.action == 'list':
            representation.pop('id', None)
            representation.pop('email', None)
            representation.pop('age', None)
            representation.pop('can_be_contacted', None)
            representation.pop('can_data_be_shared', None)

        return representation


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

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        request = self.context.get('request')
        view = self.context.get('view')

        if view and view.action == 'list':
            representation.pop('id', None)

        return representation
