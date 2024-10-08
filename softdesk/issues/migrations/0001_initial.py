# Generated by Django 5.0.8 on 2024-08-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("LOW", "Low"),
                            ("MEDIUM", "Medium"),
                            ("HIGH", "High"),
                        ],
                        default="LOW",
                        max_length=6,
                    ),
                ),
                (
                    "tag",
                    models.CharField(
                        choices=[
                            ("BUG", "Bug"),
                            ("FEATURE", "Feature"),
                            ("TASK", "Task"),
                        ],
                        default="TASK",
                        max_length=7,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("To Do", "To Do"),
                            ("In Progress", "In Progress"),
                            ("Finished", "Finished"),
                        ],
                        default="To Do",
                        max_length=12,
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
