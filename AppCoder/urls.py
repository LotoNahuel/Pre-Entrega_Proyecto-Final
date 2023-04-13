from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioApp, name="inicio App"),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
    path("buscarProfesor/", buscarProfesor, name="buscarProfesor"),
    path("buscarComision/", buscarComision, name="buscarComision"),
    path("buscarEstudiante/", buscarEstudiante, name="buscarEstudiante"),
    path("buscarEntregable/", buscarEntregable, name="buscarEntregable"),
]