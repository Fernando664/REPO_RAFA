# materias/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Materia
from .forms import MateriaForm

# Vista simple para la página principal
def index(request):
    return render(request, 'materias/index.html', {
        'total_materias': Materia.objects.count(),
        'titulo': 'Sistema de Gestión de Materias'
    })

# Vistas basadas en clase
class ListaMaterias(ListView):
    model = Materia
    template_name = 'materias/lista_materias.html'
    context_object_name = 'materias'

class AgregarMateria(CreateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'materias/agregar_materia.html'
    success_url = reverse_lazy('lista_materias')

class EditarMateria(UpdateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'materias/agregar_materia.html'  # Puede usar el mismo template
    success_url = reverse_lazy('lista_materias')
    
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Materia, id=id)

class EliminarMateria(DeleteView):
    model = Materia
    success_url = reverse_lazy('lista_materias')
    
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Materia, id=id)

# Vistas de función adicionales
def validar_codigo(request):
    """Validar si un código de materia ya existe (para AJAX)"""
    codigo = request.GET.get('codigo', '')
    existe = Materia.objects.filter(codigo=codigo).exists()
    return JsonResponse({'existe': existe})

def estadisticas(request):
    """Página de estadísticas"""
    total = Materia.objects.count()
    if total > 0:
        creditos_promedio = sum(m.creditos for m in Materia.objects.all()) / total
    else:
        creditos_promedio = 0
    
    return render(request, 'materias/estadisticas.html', {
        'total_materias': total,
        'creditos_promedio': round(creditos_promedio, 2),
        'materias': Materia.objects.all()[:10]
    })