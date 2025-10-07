"""Shared constants for authentication views and documentation."""

# Error messages
AUTH_ERROR_MISSING_CREDENTIALS = "Username and password are required."
AUTH_ERROR_USER_EXISTS = "User already exists."
AUTH_ERROR_INVALID_CREDENTIALS = "Invalid credentials."
AUTH_ERROR_INVALID_OR_MISSING_TOKEN = "Invalid or missing token."
AUTH_ERROR_FORBIDDEN = "You do not have permission to perform this action."
AUTH_ERROR_NOT_FOUND = "Task not found."

# Swagger metadata
SWAGGER_TAG_AUTH = ["Authentication"]
SWAGGER_TAG_TASKS = ["Tasks"]

SWAGGER_SUMMARY_REGISTER = "Register user"
SWAGGER_DESC_REGISTER = "Creates a new user and returns an authentication token."
SWAGGER_RESPONSE_REGISTER_CREATED = "User successfully created."
SWAGGER_RESPONSE_REGISTER_INVALID = "Invalid input or username already exists."

SWAGGER_SUMMARY_LOGIN = "Login user"
SWAGGER_DESC_LOGIN = (
    "Authenticates a user and returns a token if credentials are valid."
)
SWAGGER_RESPONSE_LOGIN_OK = "User successfully authenticated."
SWAGGER_RESPONSE_LOGIN_MISSING = "Missing username or password."
SWAGGER_RESPONSE_LOGIN_INVALID = AUTH_ERROR_INVALID_CREDENTIALS

SWAGGER_SUMMARY_LOGOUT = "Logout user"
SWAGGER_DESC_LOGOUT = "Deletes the user's authentication token."
SWAGGER_HEADER_AUTHORIZATION = "Authorization"
SWAGGER_PARAM_AUTH_TOKEN_DESC = "Authentication token. Format: `Token <key>`"
SWAGGER_RESPONSE_LOGOUT_SUCCESS = "Logout successful."
SWAGGER_RESPONSE_LOGOUT_UNAUTHORIZED = "Unauthorized or invalid token."

SWAGGER_EXAMPLE_USERNAME = "jere"
SWAGGER_EXAMPLE_PASSWORD = "1234"
SWAGGER_EXAMPLE_EMAIL = "jere@mail.com"
SWAGGER_EXAMPLE_TOKEN = "abc123xyz"
SWAGGER_EXAMPLE_TASK_TITLE = "Buy groceries"
SWAGGER_EXAMPLE_TASK_DESCRIPTION = "Pick up milk, eggs, and bread."

SWAGGER_SUMMARY_LIST_TASKS = "List tasks"
SWAGGER_DESC_LIST_TASKS = "Returns tasks owned by the authenticated user."

SWAGGER_SUMMARY_CREATE_TASK = "Create task"
SWAGGER_DESC_CREATE_TASK = "Creates a new task for the authenticated user."

SWAGGER_SUMMARY_RETRIEVE_TASK = "Retrieve task"
SWAGGER_DESC_RETRIEVE_TASK = "Retrieves a single task owned by the authenticated user."

SWAGGER_SUMMARY_UPDATE_TASK = "Update task"
SWAGGER_DESC_UPDATE_TASK = "Updates an existing task owned by the authenticated user."

SWAGGER_SUMMARY_DELETE_TASK = "Delete task"
SWAGGER_DESC_DELETE_TASK = "Deletes an existing task owned by the authenticated user."

SWAGGER_RESPONSE_TASK_LIST = "List of tasks returned successfully."
SWAGGER_RESPONSE_TASK_CREATED = "Task created successfully."
SWAGGER_RESPONSE_TASK_RETRIEVED = "Task retrieved successfully."
SWAGGER_RESPONSE_TASK_UPDATED = "Task updated successfully."
SWAGGER_RESPONSE_TASK_DELETED = "Task deleted successfully."
SWAGGER_RESPONSE_VALIDATION_ERROR = "Validation error."

# Common JSON keys
JSON_KEY_DETAIL = "detail"
JSON_KEY_TOKEN = "token"
