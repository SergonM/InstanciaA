# myapp/urls.py
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet

router = DefaultRouter()
router.register(r'', CursoViewSet, basename='curso')  # El nombre base de las rutas de cursos

urlpatterns = router.urls
