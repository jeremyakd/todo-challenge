import factory
from tasks.models import Task
from tests.factories.users import UserFactory


class TaskFactory(factory.django.DjangoModelFactory):
    """Factory for task instances."""

    class Meta:
        model = Task

    user = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: f"Task {n}")
    description = "Collect requirements and execute."
    is_completed = False
