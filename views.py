from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Materia
from .forms import MateriaForm

# 1. Vista para la página principal
def index(request):
    """Página de inicio"""
    return render(request, 'materias/index.html')

# 2. Vista para listar materias (ListView)
class ListaMaterias(ListView):
    """Lista todas las materias"""
    model = Materia
    template_name = 'materias/lista_materias.html'
    context_object_name = 'materias'
    
    def get_queryset(self):
        return Materia.objects.all().order_by('semestre', 'nombre')

# 3. Vista para agregar materia (CreateView)
class AgregarMateria(CreateView):
    """Agrega una nueva materia"""
    model = Materia
    form_class = MateriaForm
    template_name = 'materias/agregar_materia.html'
    success_url = reverse_lazy('lista_materias')
    
    def form_valid(self, form):
        messages.success(self.request, 'Materia agregada exitosamente!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrige los errores en el formulario.')
        return super().form_invalid(form)

# 4. Vista para editar materia (UpdateView)
class EditarMateria(UpdateView):
    """Edita una materia existente"""
    model = Materia
    form_class = MateriaForm
    template_name = 'materias/editar_materia.html'
    success_url = reverse_lazy('lista_materias')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Materia, id=id_)
    
    def form_valid(self, form):
        messages.success(self.request, 'Materia actualizada exitosamente!')
        return super().form_valid(form)

# 5. Vista para eliminar materia (DeleteView)
class EliminarMateria(DeleteView):
    """Elimina una materia"""
    model = Materia
    template_name = 'materias/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_materias')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Materia, id=id_)
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Materia eliminada exitosamente!')
        return super().delete(request, *args, **kwargs)

# 6. Función alternativa para eliminar (más simple)
def eliminar_materia_simple(request, id):
    """Función simple para eliminar materia"""
    materia = get_object_or_404(Materia, id=id)
    if request.method == 'POST':
        materia.delete()
        messages.success(request, 'Materia eliminada exitosamente!')
        return redirect('lista_materias')
    return redirect('lista_materias')

# 7. Validación AJAX para código único
def validar_codigo(request):
    """Valida si un código de materia ya existe"""
    if request.method == 'GET' and 'codigo' in request.GET:
        codigo = request.GET.get('codigo')
        existe = Materia.objects.filter(codigo=codigo).exists()
        return JsonResponse({'existe': existe})
    return JsonResponse({'error': 'Solicitud inválida'})

# 8. Vista para estadísticas
def estadisticas(request):
    """Muestra estadísticas de las materias"""
    total_materias = Materia.objects.count()
    materias_activas = Materia.objects.filter(activa=True).count()
    materias_inactivas = total_materias - materias_activas
    
    # Estadísticas por semestre
    semestres = {}
    for semestre_num, semestre_nombre in Materia.SEMESTRES:
        count = Materia.objects.filter(semestre=semestre_num).count()
        if count > 0:
            semestres[semestre_nombre] = count
    
    # Estadísticas por dificultad
    dificultades = {}
    for dificultad_num, dificultad_nombre in Materia.DIFICULTAD:
        count = Materia.objects.filter(dificultad=dificultad_num).count()
        if count > 0:
            dificultades[dificultad_nombre] = count
    
    context = {
        'total_materias': total_materias,
        'materias_activas': materias_activas,
        'materias_inactivas': materias_inactivas,
        'semestres': semestres,
        'dificultades': dificultades,
    }
    
    return render(request, 'materias/estadisticas.html', context)