from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "is_completed",
            "created",
            "modified",
        ]
        read_only_fields = ["id", "created", "modified"]
