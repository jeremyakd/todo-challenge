from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import auth_views, views
from .task_views import TaskViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("health/", views.health, name="health"),
    path("auth/register/", auth_views.register, name="auth-register"),
    path("auth/login/", auth_views.login, name="auth-login"),
    path("auth/logout/", auth_views.logout, name="auth-logout"),
    path("", include(router.urls)),
]
