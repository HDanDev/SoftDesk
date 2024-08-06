
from django.contrib.auth.models import AbstractUser
from django.db import models
from projects.models import Project
from .managers import UserManager


class User(AbstractUser):
    age = models.PositiveIntegerField()
    can_be_contacted = models.BooleanField(
        default=False
        )
    can_data_be_shared = models.BooleanField(
        default=False
        )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        if self.age < 15:
            msg = "User must be at least 15 years old to give consent"
            raise ValueError(msg)
        super().save(*args, **kwargs)


class Contributor(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
        )
    created_time = models.DateTimeField(
        auto_now_add=True
        )

    class Meta:
        unique_together = (
            'user',
            'project'
            )
