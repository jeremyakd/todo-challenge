"""Miscellaneous integration tests."""

import pytest
from tests.factories.tasks import TaskFactory

pytestmark = pytest.mark.django_db


def test_task_str_returns_title():
    """Task string representation should match its title."""

    task = TaskFactory(title="My Task")

    assert str(task) == "My Task"
