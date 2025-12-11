from django import forms
from .models import Materia

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Programación Avanzada'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PROG301'
            }),
            'semestre': forms.Select(attrs={
                'class': 'form-control'
            }),
            'profesor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Dr. Juan Pérez'
            }),
            'creditos': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10
            }),
            'dia_clase': forms.Select(attrs={
                'class': 'form-control'
            }),
            'horario': forms.Select(attrs={
                'class': 'form-control'
            }),
            'dificultad': forms.Select(attrs={
                'class': 'form-control'
            }),
            'comentarios': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tus comentarios, observaciones o sugerencias sobre esta materia...'
            }),
            'activa': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }