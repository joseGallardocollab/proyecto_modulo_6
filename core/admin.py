from django.contrib import admin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):  
    list_display = (
        'nombre', 
        'propietario', 
        'creado'
    )

    search_fields = (
        'nombre', 
        'propietario__username'
    )

    list_filter = (
        'creado',
    )

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo', 
        'proyecto', 
        'estado', 
        'prioridad', 
        'fecha_limite', 
        'asignado_a'
    )
    
    search_fields = (
        'titulo', 
        'proyecto__nombre', 
        'asignado_a__username'
    )

    list_filter = (
        'estado', 
        'prioridad', 
        'fecha_limite'
    )