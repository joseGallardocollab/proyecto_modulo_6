from django.db import models
from django.conf import settings


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                    on_delete=models.CASCADE,
                                    related_name='proyectos')
    creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    )

    PRIORIDADES = (
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    )

    proyecto = models.ForeignKey(Proyecto, 
                                 on_delete=models.CASCADE, 
                                 related_name='tareas')
    titulo = models.CharField(max_length=150)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default='media')
    fecha_limite = models.DateTimeField(null=True, blank=True)
    asignado_a = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                   on_delete=models.CASCADE, 
                                   related_name='tareas_asignadas',
                                   blank=True, 
                                   null=True)

    def __str__(self):
        return self.titulo
