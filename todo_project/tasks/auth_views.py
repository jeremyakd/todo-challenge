from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .constants import (
    AUTH_ERROR_INVALID_CREDENTIALS,
    AUTH_ERROR_MISSING_CREDENTIALS,
    AUTH_ERROR_USER_EXISTS,
    JSON_KEY_DETAIL,
    JSON_KEY_TOKEN,
)
from .docs.auth_docs import login_schema, logout_schema, register_schema


@register_schema
@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    """Registers a new user and returns an authentication token.

    This endpoint creates a new user account with the provided username, password, and optional email.
    If the username already exists or required fields are missing, an error is returned.

    Args:
        request: The HTTP request object containing user registration data.

    Returns:
        Response: A Response object with a token if registration is successful, or an error message otherwise.
    """
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", "")

    if not username or not password:
        return Response(
            {JSON_KEY_DETAIL: AUTH_ERROR_MISSING_CREDENTIALS},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user_model = get_user_model()
    if user_model.objects.filter(username=username).exists():
        return Response(
            {JSON_KEY_DETAIL: AUTH_ERROR_USER_EXISTS},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = user_model.objects.create_user(
        username=username, password=password, email=email
    )
    token, _ = Token.objects.get_or_create(user=user)
    return Response({JSON_KEY_TOKEN: token.key}, status=status.HTTP_201_CREATED)


@login_schema
@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    """Authenticates a user and returns an authentication token.

    This endpoint verifies the provided username and password,
    and returns a token if authentication is successful.
    If the credentials are invalid, an error message is returned.

    Args:
        request: The HTTP request object containing user login data.

    Returns:
        Response: A Response object with a token if login is successful, or an error message otherwise.
    """
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {JSON_KEY_DETAIL: AUTH_ERROR_MISSING_CREDENTIALS},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = authenticate(username=username, password=password)
    if not user:
        return Response(
            {JSON_KEY_DETAIL: AUTH_ERROR_INVALID_CREDENTIALS},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    token, _ = Token.objects.get_or_create(user=user)
    return Response({JSON_KEY_TOKEN: token.key})


@logout_schema
@api_view(["POST"])
def logout(request):
    """Logs out the authenticated user by deleting their authentication token.

    This endpoint removes the user's authentication token, effectively logging them out.
    If the user is not authenticated, no action is taken.

    Args:
        request: The HTTP request object containing authentication information.

    Returns:
        Response: A Response object with HTTP 204 status code upon successful logout.
    """
    if request.auth:
        request.auth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
