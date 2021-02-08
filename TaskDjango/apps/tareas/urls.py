from django.urls import path
from .views import listarTareas

urlpatterns = [
    path(
        route = 'listar_tareas/',
        view = listarTareas,
        name = 'listarTareas'
    ),
]
