"""Integration tests for authentication endpoints."""

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from tests.factories.users import UserFactory

pytestmark = pytest.mark.django_db


def _client() -> APIClient:
    """Return a plain API client without authentication."""

    return APIClient()


def test_register_creates_user_and_returns_token():
    """Register endpoint should create a user and respond with a token."""

    client = _client()
    payload = {"username": "newuser", "password": "Password123!"}

    url = reverse("auth-register")
    response = client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert "token" in response.data


def test_register_duplicate_username_returns_bad_request():
    """Register should reject duplicate usernames."""

    existing_user = UserFactory()
    client = _client()
    payload = {"username": existing_user.username, "password": "Password123!"}

    url = reverse("auth-register")
    response = client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_register_missing_credentials_returns_bad_request():
    """Register should require username and password."""

    client = _client()
    url = reverse("auth-register")

    response = client.post(url, {}, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_login_with_valid_credentials_returns_token():
    """Login should return a token for valid credentials."""

    user = UserFactory()
    user.set_password("Password123!")
    user.save()
    client = _client()
    payload = {"username": user.username, "password": "Password123!"}

    url = reverse("auth-login")
    response = client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert "token" in response.data


def test_login_with_invalid_password_returns_unauthorized():
    """Login should fail with incorrect password."""

    user = UserFactory()
    user.set_password("Password123!")
    user.save()
    client = _client()
    payload = {"username": user.username, "password": "WrongPassword!"}

    url = reverse("auth-login")
    response = client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_login_missing_credentials_returns_bad_request():
    """Login should require both username and password."""

    client = _client()
    url = reverse("auth-login")

    response = client.post(url, {}, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_logout_with_token_deletes_token():
    """Logout should delete the current token and return 204."""

    user = UserFactory()
    token = Token.objects.create(user=user)
    client = _client()
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    url = reverse("auth-logout")
    response = client.post(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Token.objects.filter(user=user).exists()


def test_logout_without_token_returns_unauthorized():
    """Logout should reject requests without authentication."""

    client = _client()
    url = reverse("auth-logout")

    response = client.post(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
