from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Task(TimeStampedModel):
    """Todo item owned by a single user."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title
