from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioApp, name="inicio App"),
    path("crear_curso/", crear_curso),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
]