import pytest
from rest_framework.test import APIClient
from tests.factories.users import UserFactory


@pytest.fixture
def user():
    """Provide a persisted user instance."""
    return UserFactory()


@pytest.fixture
def api_client(user):
    """Return an authenticated DRF APIClient bound to the provided user."""
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def auth_client(api_client, user):
    """Return the authenticated client along with its user for convenience."""
    return api_client, user
