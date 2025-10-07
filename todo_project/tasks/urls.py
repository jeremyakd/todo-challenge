from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import auth_views
from .task_views import TaskViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("auth/register/", auth_views.register, name="auth-register"),
    path("auth/login/", auth_views.login, name="auth-login"),
    path("auth/logout/", auth_views.logout, name="auth-logout"),
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
