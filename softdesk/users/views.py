from rest_framework import viewsets, permissions
from .models import User, Contributor
from projects.models import Project
from issues.models import Issue
from comments.models import Comment
from .serializers import UserSerializer, ContributorSerializer, UserCreateSerializer


class IsSelf(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user or (hasattr(obj, 'user') and obj.user == request.user)

class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Project):
            return Contributor.objects.filter(
                user=request.user,
                project=obj
                ).exists()
        if isinstance(obj, Issue):
            return Contributor.objects.filter(
                user=request.user,
                project=obj.project
                ).exists()
        if isinstance(obj, Comment):
            return Contributor.objects.filter(
                user=request.user,
                project=obj.issue.project
                ).exists()
        return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated()
        ]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'view': self
            }

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        elif self.action in [
            'update',
            'partial_update',
            'destroy'
            ]:
            return [
                permissions.IsAuthenticated(),
                IsSelf()
                ]
        return [IsContributor()]

    def perform_create(self, serializer):
        age = self.request.data.get('age')
        serializer.save()

class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [
        permissions.IsAuthenticated(),
        IsContributor()
        ]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action in [
            'update',
            'partial_update',
            'destroy'
            ]:
            return [
                permissions.IsAuthenticated(),
                IsSelf()
                ]
        return [IsContributor()]
