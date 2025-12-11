from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Materia(models.Model):
    # Opciones para los campos de selección
    SEMESTRES = [
        (1, '1er Semestre'),
        (2, '2do Semestre'),
        (3, '3er Semestre'),
        (4, '4to Semestre'),
        (5, '5to Semestre'),
        (6, '6to Semestre'),
        (7, '7mo Semestre'),
        (8, '8vo Semestre'),
        (9, '9no Semestre'),
        (10, '10mo Semestre'),
    ]
    
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
    ]
    
    HORARIOS = [
        ('M', 'Matutino (7:00-12:00)'),
        ('V', 'Vespertino (12:00-17:00)'),
        ('N', 'Nocturno (17:00-22:00)'),
    ]
    
    DIFICULTAD = [
        (1, 'Muy Fácil'),
        (2, 'Fácil'),
        (3, 'Moderada'),
        (4, 'Difícil'),
        (5, 'Muy Difícil'),
    ]
    
    # Campos del modelo
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Materia")
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código de la Materia")
    semestre = models.IntegerField(choices=SEMESTRES, verbose_name="Semestre Actual")
    profesor = models.CharField(max_length=100, verbose_name="Nombre del Profesor")
    creditos = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Créditos"
    )
    dia_clase = models.CharField(max_length=3, choices=DIAS_SEMANA, verbose_name="Día de Clase")
    horario = models.CharField(max_length=1, choices=HORARIOS, verbose_name="Horario")
    dificultad = models.IntegerField(choices=DIFICULTAD, verbose_name="Nivel de Dificultad")
    comentarios = models.TextField(verbose_name="Comentarios sobre la Materia")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    activa = models.BooleanField(default=True, verbose_name="Materia Activa")
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"
        ordering = ['semestre', 'nombre']