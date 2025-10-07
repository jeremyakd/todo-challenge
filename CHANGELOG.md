# Changelog

## [Unreleased]

- Proyecto Django `todo_project` inicializado con app `tasks` y API `GET /api/health/`.
- Configuración de Swagger (`/swagger/`) y Redoc (`/redoc/`).
- Se agregó `.gitignore` para caches, entornos virtuales y artefactos de build.
- Se movió `SECRET_KEY` a `.env`, se agregó soporte con `python-dotenv` y `.env` quedó fuera del control de versiones.
- Autenticación por token con `rest_framework.authtoken`, endpoints `/api/auth/*` (register/login/logout) y protección global con `TokenAuthentication` y `IsAuthenticated`.
- CRUD de tareas autenticado, con `TaskViewSet`, serializer dedicado, documentos Swagger y respuesta filtrada por usuario.
