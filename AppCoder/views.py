from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def crear_curso(request):
    nombre_curso="Python"
    comision_curso="51325"

    curso=Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta=f"Curso Creado --- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)