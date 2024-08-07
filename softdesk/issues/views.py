from rest_framework import viewsets, permissions
from .models import Issue
from users.views import IsContributor
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [IsContributor()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
