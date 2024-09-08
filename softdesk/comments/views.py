from rest_framework import viewsets, permissions
from .models import Comment
from users.views import IsContributor, IsAuthor, IsAllowedToCreate
from issues.models import Issue
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.filter(issue__project__contributor__user=self.request.user)

    def get_serializer_context(self):
        return {
            'request': self.request,
            'view': self
            }

    def perform_create(self, serializer):
        issue_id = self.request.data.get('issue')
        issue = Issue.objects.get(id=issue_id)
        serializer.save(
            author=self.request.user,
            issue=issue
            )

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsAllowedToCreate()]
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
