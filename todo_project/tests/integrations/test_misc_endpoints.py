"""Miscellaneous integration tests."""

import pytest
from django.urls import reverse
from tests.factories.tasks import TaskFactory

pytestmark = pytest.mark.django_db


def test_health_endpoint_returns_ok(api_client):
    """Health check should respond with an ok payload."""

    url = reverse("health")
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data == {"status": "ok"}


def test_task_str_returns_title():
    """Task string representation should match its title."""

    task = TaskFactory(title="My Task")

    assert str(task) == "My Task"
