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
    """Handles CRUD operations for user tasks using Django REST Framework viewsets.

    Provides endpoints for listing, creating, retrieving, updating, partially updating, and deleting tasks.
    Ensures that only authenticated users can access and modify their own tasks.
    """

    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Returns the queryset of tasks belonging to the authenticated user.

        Filters tasks so that users only see their own tasks. Excludes results for schema generation views.

        Returns:
            QuerySet: A queryset of Task objects for the current user, or an empty queryset for schema views.
        """
        # Exclude swagger schema view from queryset filtering
        if getattr(self, "swagger_fake_view", False):
            return Task.objects.none()
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Associates the newly created task with the authenticated user.

        Ensures that tasks are always created for the user making the request.

        Args:
            serializer (TaskSerializer): The serializer instance used to save the new task.
        """
        serializer.save(user=self.request.user)

    @list_tasks_schema
    def list(self, request, *args, **kwargs):
        """Lists all tasks belonging to the authenticated user.

        Returns a paginated response containing the user's tasks.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A paginated list of Task objects for the user.
        """
        return super().list(request, *args, **kwargs)

    @create_task_schema
    def create(self, request, *args, **kwargs):
        """Creates a new task for the authenticated user.

        Accepts task data and returns the created task in the response.

        Args:
            request (Request): The HTTP request object containing task data.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The created Task object.
        """
        return super().create(request, *args, **kwargs)

    @retrieve_task_schema
    def retrieve(self, request, *args, **kwargs):
        """Retrieves a specific task belonging to the authenticated user.

        Returns the details of the requested task if it exists and belongs to the user.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The requested Task object.
        """
        return super().retrieve(request, *args, **kwargs)

    @update_task_schema
    def update(self, request, *args, **kwargs):
        """Updates an existing task for the authenticated user.

        Accepts updated task data and returns the modified task in the response.

        Args:
            request (Request): The HTTP request object containing updated task data.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The updated Task object.
        """
        return super().update(request, *args, **kwargs)

    @partial_update_task_schema
    def partial_update(self, request, *args, **kwargs):
        """Partially updates an existing task for the authenticated user.

        Allows updating specific fields of a task and returns the modified task in the response.

        Args:
            request (Request): The HTTP request object containing partial task data.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The partially updated Task object.
        """
        return super().partial_update(request, *args, **kwargs)

    @delete_task_schema
    def destroy(self, request, *args, **kwargs):
        """Deletes a specific task belonging to the authenticated user.

        Removes the requested task from the database if it exists and belongs to the user.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: An empty response indicating successful deletion.
        """
        return super().destroy(request, *args, **kwargs)
