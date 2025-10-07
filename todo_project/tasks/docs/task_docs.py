from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..constants import (
    AUTH_ERROR_FORBIDDEN,
    AUTH_ERROR_INVALID_OR_MISSING_TOKEN,
    AUTH_ERROR_NOT_FOUND,
    JSON_KEY_DETAIL,
    SWAGGER_DESC_CREATE_TASK,
    SWAGGER_DESC_DELETE_TASK,
    SWAGGER_DESC_LIST_TASKS,
    SWAGGER_DESC_RETRIEVE_TASK,
    SWAGGER_DESC_UPDATE_TASK,
    SWAGGER_EXAMPLE_TASK_DESCRIPTION,
    SWAGGER_EXAMPLE_TASK_TITLE,
    SWAGGER_HEADER_AUTHORIZATION,
    SWAGGER_PARAM_AUTH_TOKEN_DESC,
    SWAGGER_RESPONSE_TASK_CREATED,
    SWAGGER_RESPONSE_TASK_DELETED,
    SWAGGER_RESPONSE_TASK_LIST,
    SWAGGER_RESPONSE_TASK_RETRIEVED,
    SWAGGER_RESPONSE_TASK_UPDATED,
    SWAGGER_RESPONSE_VALIDATION_ERROR,
    SWAGGER_SUMMARY_CREATE_TASK,
    SWAGGER_SUMMARY_DELETE_TASK,
    SWAGGER_SUMMARY_LIST_TASKS,
    SWAGGER_SUMMARY_RETRIEVE_TASK,
    SWAGGER_SUMMARY_UPDATE_TASK,
    SWAGGER_TAG_TASKS,
)

TASK_RESPONSE_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        "title": openapi.Schema(
            type=openapi.TYPE_STRING, example=SWAGGER_EXAMPLE_TASK_TITLE
        ),
        "description": openapi.Schema(
            type=openapi.TYPE_STRING, example=SWAGGER_EXAMPLE_TASK_DESCRIPTION
        ),
        "is_completed": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),
        "created": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_DATETIME,
            example="2025-01-01T12:00:00Z",
        ),
        "updated": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_DATETIME,
            example="2025-01-01T12:30:00Z",
        ),
    },
)

TASK_CREATE_UPDATE_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "title": openapi.Schema(
            type=openapi.TYPE_STRING, example=SWAGGER_EXAMPLE_TASK_TITLE
        ),
        "description": openapi.Schema(
            type=openapi.TYPE_STRING, example=SWAGGER_EXAMPLE_TASK_DESCRIPTION
        ),
        "is_completed": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),
    },
    required=["title"],
)

AUTH_HEADER_PARAMETER = openapi.Parameter(
    SWAGGER_HEADER_AUTHORIZATION,
    openapi.IN_HEADER,
    description=SWAGGER_PARAM_AUTH_TOKEN_DESC,
    type=openapi.TYPE_STRING,
    required=True,
)

UNAUTHORIZED_RESPONSE = openapi.Response(
    description=AUTH_ERROR_INVALID_OR_MISSING_TOKEN,
    examples={
        "application/json": {JSON_KEY_DETAIL: AUTH_ERROR_INVALID_OR_MISSING_TOKEN}
    },
)

FORBIDDEN_RESPONSE = openapi.Response(
    description=AUTH_ERROR_FORBIDDEN,
    examples={"application/json": {JSON_KEY_DETAIL: AUTH_ERROR_FORBIDDEN}},
)

NOT_FOUND_RESPONSE = openapi.Response(
    description=AUTH_ERROR_NOT_FOUND,
    examples={"application/json": {JSON_KEY_DETAIL: AUTH_ERROR_NOT_FOUND}},
)


list_tasks_schema = swagger_auto_schema(
    tags=SWAGGER_TAG_TASKS,
    operation_summary=SWAGGER_SUMMARY_LIST_TASKS,
    operation_description=SWAGGER_DESC_LIST_TASKS,
    manual_parameters=[AUTH_HEADER_PARAMETER],
    responses={
        200: openapi.Response(
            description=SWAGGER_RESPONSE_TASK_LIST,
            schema=openapi.Schema(type=openapi.TYPE_ARRAY, items=TASK_RESPONSE_SCHEMA),
        ),
        401: UNAUTHORIZED_RESPONSE,
    },
)


create_task_schema = swagger_auto_schema(
    tags=SWAGGER_TAG_TASKS,
    operation_summary=SWAGGER_SUMMARY_CREATE_TASK,
    operation_description=SWAGGER_DESC_CREATE_TASK,
    manual_parameters=[AUTH_HEADER_PARAMETER],
    request_body=TASK_CREATE_UPDATE_SCHEMA,
    responses={
        201: openapi.Response(
            description=SWAGGER_RESPONSE_TASK_CREATED,
            schema=TASK_RESPONSE_SCHEMA,
        ),
        400: openapi.Response(description=SWAGGER_RESPONSE_VALIDATION_ERROR),
        401: UNAUTHORIZED_RESPONSE,
    },
)


retrieve_task_schema = swagger_auto_schema(
    tags=SWAGGER_TAG_TASKS,
    operation_summary=SWAGGER_SUMMARY_RETRIEVE_TASK,
    operation_description=SWAGGER_DESC_RETRIEVE_TASK,
    manual_parameters=[AUTH_HEADER_PARAMETER],
    responses={
        200: openapi.Response(
            description=SWAGGER_RESPONSE_TASK_RETRIEVED,
            schema=TASK_RESPONSE_SCHEMA,
        ),
        401: UNAUTHORIZED_RESPONSE,
        403: FORBIDDEN_RESPONSE,
        404: NOT_FOUND_RESPONSE,
    },
)


update_task_schema = swagger_auto_schema(
    tags=SWAGGER_TAG_TASKS,
    operation_summary=SWAGGER_SUMMARY_UPDATE_TASK,
    operation_description=SWAGGER_DESC_UPDATE_TASK,
    manual_parameters=[AUTH_HEADER_PARAMETER],
    request_body=TASK_CREATE_UPDATE_SCHEMA,
    responses={
        200: openapi.Response(
            description=SWAGGER_RESPONSE_TASK_UPDATED,
            schema=TASK_RESPONSE_SCHEMA,
        ),
        400: openapi.Response(description=SWAGGER_RESPONSE_VALIDATION_ERROR),
        401: UNAUTHORIZED_RESPONSE,
        403: FORBIDDEN_RESPONSE,
        404: NOT_FOUND_RESPONSE,
    },
)


partial_update_task_schema = swagger_auto_schema(
    tags=SWAGGER_TAG_TASKS,
    operation_summary=SWAGGER_SUMMARY_UPDATE_TASK,
    operation_description=SWAGGER_DESC_UPDATE_TASK,
    manual_parameters=[AUTH_HEADER_PARAMETER],
    request_body=TASK_CREATE_UPDATE_SCHEMA,
    responses={
        200: openapi.Response(
            description=SWAGGER_RESPONSE_TASK_UPDATED,
            schema=TASK_RESPONSE_SCHEMA,
        ),
        400: openapi.Response(description=SWAGGER_RESPONSE_VALIDATION_ERROR),
        401: UNAUTHORIZED_RESPONSE,
        403: FORBIDDEN_RESPONSE,
        404: NOT_FOUND_RESPONSE,
    },
)


delete_task_schema = swagger_auto_schema(
    tags=SWAGGER_TAG_TASKS,
    operation_summary=SWAGGER_SUMMARY_DELETE_TASK,
    operation_description=SWAGGER_DESC_DELETE_TASK,
    manual_parameters=[AUTH_HEADER_PARAMETER],
    responses={
        204: openapi.Response(
            description=SWAGGER_RESPONSE_TASK_DELETED,
            examples={"application/json": {}},
        ),
        401: UNAUTHORIZED_RESPONSE,
        403: FORBIDDEN_RESPONSE,
        404: NOT_FOUND_RESPONSE,
    },
)
