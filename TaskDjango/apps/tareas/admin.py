from .models import Categoria, Notificaciones, Tarea
from django.contrib import admin

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tarea)
admin.site.register(Notificaciones)
