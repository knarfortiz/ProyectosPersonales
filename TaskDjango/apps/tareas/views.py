from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tarea

# Tareas -------------------------------------------------------------------------------
@login_required
def listarTareas(request):
    """ listar tareas """
    tareas = Tarea.objects.filter(tipo='PRI')
    subtareas = Tarea.objects.filter(tipo='SUB')

    contex = {
        'tareas' : tareas,
        'subtareas' : subtareas,
    }
    return render(request, 'tareas/listarTareas.html', contex)

def nuevaTarea(request):
    """ Crear nueva tarea """
    pass

def editarTarea(request):
    """ Editar Tareas """
    pass

def eliminarTarea(request):
    """ Eliminar Tareas """
    pass

# Categorias ----------------------------------------------------------------------------

# Notificaciones ------------------------------------------------------------------------

