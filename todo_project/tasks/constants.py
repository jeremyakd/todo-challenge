"""Shared constants for authentication views and documentation."""

# Error messages
AUTH_ERROR_MISSING_CREDENTIALS = "Username and password are required."
AUTH_ERROR_USER_EXISTS = "User already exists."
AUTH_ERROR_INVALID_CREDENTIALS = "Invalid credentials."
AUTH_ERROR_INVALID_OR_MISSING_TOKEN = "Invalid or missing token."

# Swagger metadata
SWAGGER_TAG_AUTH = ["Authentication"]

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

# Common JSON keys
JSON_KEY_DETAIL = "detail"
JSON_KEY_TOKEN = "token"
