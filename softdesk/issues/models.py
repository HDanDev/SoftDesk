from django.db import models
from projects.models import Project
from users.models import User
import uuid


class Issue(models.Model):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRIORITY_LEVELS = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    BUG = 'BUG'
    FEATURE = 'FEATURE'
    TASK = 'TASK'
    TAG_CHOICES = [
        (BUG, 'Bug'),
        (FEATURE, 'Feature'),
        (TASK, 'Task'),
    ]

    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    FINISHED = 'Finished'
    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
    ]

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
        )

    title = models.CharField(
        max_length=100
        )
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='issues'
        )
    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_issues'
        )
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_LEVELS,
        default=LOW
        )
    tag = models.CharField(
        max_length=7,
        choices=TAG_CHOICES,
        default=TASK
        )
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default=TODO
        )
    created_time = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return self.title
