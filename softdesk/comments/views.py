from rest_framework import viewsets, permissions
from .models import Comment
from users.views import IsContributor
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [IsContributor()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
