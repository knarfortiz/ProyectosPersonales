from django.urls import path
from .views import cerrarSesion, listarUsuarios, loginUser

urlpatterns = [
    path(
        route = 'listar_usuarios/',
        view = listarUsuarios,
        name = 'listarUsuarios'
    ),
    path(
        route = 'login/',
        view = loginUser,
        name = 'login'
    ),
    path(
        route = 'logout/',
        view = cerrarSesion,
        name = 'logout'
    ),
]
