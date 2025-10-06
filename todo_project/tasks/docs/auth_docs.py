from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..constants import (
    AUTH_ERROR_INVALID_CREDENTIALS,
    AUTH_ERROR_INVALID_OR_MISSING_TOKEN,
    AUTH_ERROR_MISSING_CREDENTIALS,
    AUTH_ERROR_USER_EXISTS,
    JSON_KEY_DETAIL,
    JSON_KEY_TOKEN,
    SWAGGER_DESC_LOGIN,
    SWAGGER_DESC_LOGOUT,
    SWAGGER_DESC_REGISTER,
    SWAGGER_EXAMPLE_EMAIL,
    SWAGGER_EXAMPLE_PASSWORD,
    SWAGGER_EXAMPLE_TOKEN,
    SWAGGER_EXAMPLE_USERNAME,
    SWAGGER_HEADER_AUTHORIZATION,
    SWAGGER_PARAM_AUTH_TOKEN_DESC,
    SWAGGER_RESPONSE_LOGIN_INVALID,
    SWAGGER_RESPONSE_LOGIN_MISSING,
    SWAGGER_RESPONSE_LOGIN_OK,
    SWAGGER_RESPONSE_LOGOUT_SUCCESS,
    SWAGGER_RESPONSE_LOGOUT_UNAUTHORIZED,
    SWAGGER_RESPONSE_REGISTER_CREATED,
    SWAGGER_RESPONSE_REGISTER_INVALID,
    SWAGGER_SUMMARY_LOGIN,
    SWAGGER_SUMMARY_LOGOUT,
    SWAGGER_SUMMARY_REGISTER,
    SWAGGER_TAG_AUTH,
)

register_schema = swagger_auto_schema(
    method="post",
    tags=SWAGGER_TAG_AUTH,
    operation_summary=SWAGGER_SUMMARY_REGISTER,
    operation_description=SWAGGER_DESC_REGISTER,
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["username", "password"],
        properties={
            "username": openapi.Schema(
                type=openapi.TYPE_STRING, example=SWAGGER_EXAMPLE_USERNAME
            ),
            "password": openapi.Schema(
                type=openapi.TYPE_STRING, example=SWAGGER_EXAMPLE_PASSWORD
            ),
            "email": openapi.Schema(
                type=openapi.TYPE_STRING, example=SWAGGER_EXAMPLE_EMAIL
            ),
        },
    ),
    responses={
        201: openapi.Response(
            description=SWAGGER_RESPONSE_REGISTER_CREATED,
            examples={"application/json": {JSON_KEY_TOKEN: SWAGGER_EXAMPLE_TOKEN}},
        ),
        400: openapi.Response(
            description=SWAGGER_RESPONSE_REGISTER_INVALID,
            examples={
                "application/json": [
                    {JSON_KEY_DETAIL: AUTH_ERROR_MISSING_CREDENTIALS},
                    {JSON_KEY_DETAIL: AUTH_ERROR_USER_EXISTS},
                ]
            },
        ),
    },
)


login_schema = swagger_auto_schema(
    method="post",
    tags=SWAGGER_TAG_AUTH,
    operation_summary=SWAGGER_SUMMARY_LOGIN,
    operation_description=SWAGGER_DESC_LOGIN,
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["username", "password"],
        properties={
            "username": openapi.Schema(
                type=openapi.TYPE_STRING, example=SWAGGER_EXAMPLE_USERNAME
            ),
            "password": openapi.Schema(
                type=openapi.TYPE_STRING, example=SWAGGER_EXAMPLE_PASSWORD
            ),
        },
    ),
    responses={
        200: openapi.Response(
            description=SWAGGER_RESPONSE_LOGIN_OK,
            examples={"application/json": {JSON_KEY_TOKEN: SWAGGER_EXAMPLE_TOKEN}},
        ),
        400: openapi.Response(
            description=SWAGGER_RESPONSE_LOGIN_MISSING,
            examples={
                "application/json": {JSON_KEY_DETAIL: AUTH_ERROR_MISSING_CREDENTIALS}
            },
        ),
        401: openapi.Response(
            description=SWAGGER_RESPONSE_LOGIN_INVALID,
            examples={
                "application/json": {JSON_KEY_DETAIL: AUTH_ERROR_INVALID_CREDENTIALS}
            },
        ),
    },
)


logout_schema = swagger_auto_schema(
    method="post",
    tags=SWAGGER_TAG_AUTH,
    operation_summary=SWAGGER_SUMMARY_LOGOUT,
    operation_description=SWAGGER_DESC_LOGOUT,
    manual_parameters=[
        openapi.Parameter(
            SWAGGER_HEADER_AUTHORIZATION,
            openapi.IN_HEADER,
            description=SWAGGER_PARAM_AUTH_TOKEN_DESC,
            type=openapi.TYPE_STRING,
            required=True,
        ),
    ],
    responses={
        204: openapi.Response(
            description=SWAGGER_RESPONSE_LOGOUT_SUCCESS,
            examples={"application/json": None},
        ),
        401: openapi.Response(
            description=SWAGGER_RESPONSE_LOGOUT_UNAUTHORIZED,
            examples={
                "application/json": {
                    JSON_KEY_DETAIL: AUTH_ERROR_INVALID_OR_MISSING_TOKEN
                }
            },
        ),
    },
)
