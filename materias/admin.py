from django.contrib import admin
from .models import Materia  # Importa tu modelo

# Registra el modelo para que aparezca en el admin
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista
    list_display = ('codigo', 'nombre', 'semestre', 'profesor', 'activa', 'fecha_registro')
    
    # Filtros en la barra lateral
    list_filter = ('semestre', 'activa', 'dificultad', 'dia_clase')
    
    # Campos de búsqueda
    search_fields = ('nombre', 'codigo', 'profesor', 'comentarios')
    
    # Orden por defecto
    ordering = ('-fecha_registro', 'semestre')
    
    # Campos editables directamente en la lista
    list_editable = ('activa',)
    
    # Campos que aparecen en el formulario de edición
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'codigo', 'semestre', 'profesor')
        }),
        ('Detalles Académicos', {
            'fields': ('creditos', 'dia_clase', 'horario', 'dificultad')
        }),
        ('Información Adicional', {
            'fields': ('comentarios', 'activa')
        }),
    )