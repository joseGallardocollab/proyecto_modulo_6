from django.urls import path
from .views import *

urlpatterns = [  
    #dashboard
    path('', DashboardView.as_view(), name='dashboard'),    
    #registro de usuario 
    path('registro/', RegistroView.as_view(), name='registro'),
    #proyectos
    path('proyectos/', ProyectoListView.as_view(), name='proyecto_list'),
    path('proyectos/nuevo/', ProyectoCreateView.as_view(), name='proyecto_create'),
    #tareas
    path('proyectos/<int:proyecto_id>/tareas/', TareaListView.as_view(), name='tarea_list'),
    path('proyectos/<int:proyecto_id>/tareas/nueva/', TareaCreateView.as_view(), name='tarea_create'),
    path('proyectos/<int:proyecto_id>/tareas/<int:pk>/editar/', TareaUpdateView.as_view(), name='tarea_update'),
    path('proyectos/<int:proyecto_id>/tareas/<int:pk>/eliminar/', TareaDeleteView.as_view(), name='tarea_delete'),
]