from django.contrib import admin

# Register your models here.
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion')  # Campos que quieres mostrar en la lista de admin
