from apps.usuarios.forms import LoginForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


# Usuarios ----------------------------------------------------------------------------
def listarUsuarios(request):
    """ listar usuarios """
    pass

def nuevoUsuario(request):
    """ Crear usuario """
    pass

def editarUsuario(request):
    """ Editar usuario """
    pass

def eliminarUsuario(request):
    """ Eliminar usuario """
    pass

# Auth ----------------------------------------------------------------------------
def loginUser(request):
    """ login de usuario """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tareas:listarTareas')

    contex = {
            'loginForm' : LoginForm,
    }
    return render(request, 'usuarios/login.html', contex)


@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('usuarios:login')
