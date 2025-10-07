import pytest
from django.urls import reverse
from rest_framework import status
from tasks.models import Task
from tests.factories.tasks import TaskFactory

pytestmark = pytest.mark.django_db


def test_list_returns_only_authenticated_user_tasks(auth_client):
    """List endpoint should only return tasks belonging to the requester."""

    client, user = auth_client
    own_tasks = TaskFactory.create_batch(2, user=user)
    TaskFactory.create_batch(2)  # Tasks owned by other users

    url = reverse("tasks-list")
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    returned_ids = {item["id"] for item in response.data}
    assert returned_ids == {task.id for task in own_tasks}


def test_create_task_assigns_authenticated_user(auth_client):
    """Creating a task should automatically bind it to the requester."""

    client, user = auth_client
    url = reverse("tasks-list")
    payload = {"title": "Prepare sprint review", "description": "Gather metrics."}

    response = client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    task = Task.objects.get(id=response.data["id"])
    assert task.user == user
    assert task.title == payload["title"]


def test_retrieve_returns_single_task(auth_client):
    """Requester must be able to retrieve their own task details."""

    client, user = auth_client
    task = TaskFactory(user=user)
    url = reverse("tasks-detail", args=[task.id])

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == task.id
    assert response.data["title"] == task.title


def test_update_task_with_put(auth_client):
    """Full updates should allow changing all mutable fields."""

    client, user = auth_client
    task = TaskFactory(user=user, title="Initial title", description="Initial")
    url = reverse("tasks-detail", args=[task.id])
    payload = {
        "title": "Updated title",
        "description": "Updated description",
        "is_completed": True,
    }

    response = client.put(url, payload, format="json")

    assert response.status_code == status.HTTP_200_OK
    task.refresh_from_db()
    assert task.title == payload["title"]
    assert task.description == payload["description"]
    assert task.is_completed is True


def test_partial_update_task_toggles_completion(auth_client):
    """PATCH requests should be able to toggle completion state."""

    client, user = auth_client
    task = TaskFactory(user=user, is_completed=False)
    url = reverse("tasks-detail", args=[task.id])

    response = client.patch(url, {"is_completed": True}, format="json")

    assert response.status_code == status.HTTP_200_OK
    task.refresh_from_db()
    assert task.is_completed is True


def test_delete_task_removes_instance(auth_client):
    """Deleting a task should remove it from the database."""

    client, user = auth_client
    task = TaskFactory(user=user)
    url = reverse("tasks-detail", args=[task.id])

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Task.objects.filter(id=task.id).exists()


def test_forbidden_when_accessing_other_user_task(auth_client):
    """Users must not access or delete tasks that they do not own."""

    client, _ = auth_client
    other_task = TaskFactory()
    url = reverse("tasks-detail", args=[other_task.id])

    get_response = client.get(url)
    delete_response = client.delete(url)

    assert get_response.status_code == status.HTTP_404_NOT_FOUND
    assert delete_response.status_code == status.HTTP_404_NOT_FOUND
