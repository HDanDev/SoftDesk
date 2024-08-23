from rest_framework import viewsets, permissions
from .models import Comment
from users.views import IsContributor, IsAuthor
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'view': self
            }

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
                IsContributor(),
                IsAuthor()
                ]
        return [IsContributor()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
