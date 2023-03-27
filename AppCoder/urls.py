from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioApp),
    path("crear_curso/", crear_curso),
    path("cursos/", cursos),
    path("profesores/", profesores),
    path("estudiantes/", estudiantes),
    path("entregables/", entregables),
]