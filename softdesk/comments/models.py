from django.db import models
from issues.models import Issue
from users.models import User
import uuid


class Comment(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
        )
    description = models.TextField()
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    created_time = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return f'Comment by {self.author} on {self.issue}'
