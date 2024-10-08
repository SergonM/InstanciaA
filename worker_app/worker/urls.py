# myapp/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, health_check

router = DefaultRouter()
router.register(r'', CursoViewSet, basename='curso')  # El nombre base de las rutas de cursos

urlpatterns = [
    path('health/', health_check, name='health_check'),  # Ruta para el health check
]

urlpatterns += router.urls