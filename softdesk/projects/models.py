from django.db import models
from django.conf import settings


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
