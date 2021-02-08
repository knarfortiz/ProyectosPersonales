from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    """ Categoria de Tareas """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    """ Tareas o Subtareas """
    ESTADOS = (
        ('P', 'Pendiente'),
        ('A', 'Activo'),
        ('T', 'Terminado'),
    )
    TIPO = (
        ('PRI', 'Principal'),
        ('SUB', 'SubTarea'),
    )
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=1, choices=ESTADOS)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    fecha_caducidad = models.DateField()
    tipo = models.CharField(max_length=3, choices=TIPO)
    publico = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titulo


class Notificaciones(models.Model):
    """ Notificaciones de Asignacion de tareas """
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Tarea, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

