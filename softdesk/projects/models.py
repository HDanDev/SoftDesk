from django.db import models
from django.conf import settings
import uuid


class Project(models.Model):
    BACKEND = 'Back-end'
    FRONTEND = 'Front-end'
    IOS = 'iOS'
    ANDROID = 'Android'
    PROJECT_TYPES = [
        (BACKEND, 'Back-end'),
        (FRONTEND, 'Front-end'),
        (IOS, 'iOS'),
        (ANDROID, 'Android'),
    ]

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
        )

    name = models.CharField(
        max_length=100
        )
    description = models.TextField()
    type = models.CharField(
        max_length=10,
        choices=PROJECT_TYPES
        )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    created_time = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return self.name
