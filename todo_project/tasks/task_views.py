from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .docs.task_docs import (
    create_task_schema,
    delete_task_schema,
    list_tasks_schema,
    partial_update_task_schema,
    retrieve_task_schema,
    update_task_schema,
)
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @list_tasks_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @create_task_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @retrieve_task_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @update_task_schema
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @partial_update_task_schema
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @delete_task_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
