Todo Project API

Proyecto base con Django y Django REST Framework.
Incluye autenticación por token, CRUD de tareas y documentación Swagger.
Está preparado para ejecutarse tanto localmente como en contenedores Docker.

---

## Requisitos

* Python 3.13
* Docker y Docker Compose
* (Opcional) entorno virtual con venv

---

## Instalación local

```
git clone https://github.com/jeremyakd/todo-project.git
cd todo-project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Crear el archivo `.env` dentro de `todo_project/` con lo mínimo:

```
DJANGO_SECRET_KEY=alguna_clave_segura
DEBUG=True
ALLOWED_HOSTS=*
```
Si no tienens clave segura puedes obtener una de aqui => https://djecrety.ir/

Luego aplicar migraciones y levantar el servidor:

```
python todo_project/manage.py migrate
python todo_project/manage.py runserver
```

La API queda disponible en [http://localhost:8000](http://localhost:8000).

---

## Endpoints principales

| Método | Ruta                | Descripción                   | Auth |
| :----- | :------------------ | :---------------------------- | :--- |
| POST   | /api/auth/register/ | Crear usuario nuevo           | No   |
| POST   | /api/auth/login/    | Obtener token                 | No   |
| POST   | /api/auth/logout/   | Cerrar sesión (elimina token) | Sí   |
| GET    | /api/tasks/         | Listar tareas del usuario     | Sí   |
| POST   | /api/tasks/         | Crear tarea                   | Sí   |
| GET    | /api/tasks/{id}/    | Ver detalle                   | Sí   |
| PUT    | /api/tasks/{id}/    | Actualizar completa           | Sí   |
| PATCH  | /api/tasks/{id}/    | Actualizar parcial            | Sí   |
| DELETE | /api/tasks/{id}/    | Eliminar                      | Sí   |

Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
Redoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## Tests

Los tests usan pytest y factory_boy.

```
pytest --cov=tasks --cov-report=term-missing
```

El proyecto llega al 100 % de cobertura.

---

## Docker

### Construir y ejecutar localmente

```
docker compose up --build
```

### Usar la imagen publicada

```
docker compose -f docker-compose.image.yml up -d
```

El servicio se expone en el puerto 8000.

---

## CI/CD

Hay un workflow configurado para GitHub Actions que:

1. Ejecuta los tests.
2. Construye la imagen Docker.
3. La publica en Docker Hub con la etiqueta `latest`.

Variables requeridas en los Secrets del repositorio:

```
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
DJANGO_SECRET_KEY
DEBUG
ALLOWED_HOSTS
```

---

## Estructura del proyecto

```
todo_project/
├── tasks/
│   ├── auth_views.py
│   ├── task_views.py
│   ├── serializers.py
│   ├── constants.py
│   ├── docs/
│   └── urls.py
│
├── tests/
│   ├── factories/
│   ├── integrations/
│   └── conftest.py
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Dockerfile
├── docker-compose.yml
├── docker-compose.image.yml
└── requirements.txt
```

---

## Notas

* TokenAuthentication global con IsAuthenticated por defecto.
* Swagger es público (AllowAny).
* TaskViewSet filtra por request.user.
* Archivos estáticos servidos con whitenoise.
* DEBUG se maneja como texto ("True" / "False").
* No hay dependencias de base de datos externas; usa SQLite.
