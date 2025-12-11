from django.urls import path
from . import views
from .views import ListaMaterias, AgregarMateria, EditarMateria, EliminarMateria

urlpatterns = [
    path('', views.index, name='index'),
    path('materias/', ListaMaterias.as_view(), name='lista_materias'),
    path('materias/agregar/', AgregarMateria.as_view(), name='agregar_materia'),
    path('materias/editar/<int:id>/', EditarMateria.as_view(), name='editar_materia'),
    path('materias/eliminar/<int:id>/', EliminarMateria.as_view(), name='eliminar_materia'),
    # O si prefieres la función simple:
    # path('materias/eliminar/<int:id>/', views.eliminar_materia_simple, name='eliminar_materia'),
    path('validar-codigo/', views.validar_codigo, name='validar_codigo'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
]