from django.urls import path
from . import views

app_name = 'materias'

urlpatterns = [
    path('', views.index, name='index'),
    path('materias/', views.ListaMaterias.as_view(), name='lista_materias'),
    path('materias/agregar/', views.AgregarMateria.as_view(), name='agregar_materia'),
    path('materias/editar/<int:id>/', views.EditarMateria.as_view(), name='editar_materia'),
    path('materias/eliminar/<int:id>/', views.EliminarMateria.as_view(), name='eliminar_materia'),
    path('materias/validar_codigo/', views.validar_codigo, name='validar_codigo'),
    path('materias/estadisticas/', views.estadisticas, name='estadisticas'),
]