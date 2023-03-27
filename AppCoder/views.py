from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def crear_curso(request):
    nombre_curso="Python"
    comision_curso="51325"
    print("Creando curso")

    curso=Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta=f"Curso Creado --- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)

def cursos(request):
    return render(request, "cursos.html")

def profesores(request):
    return render(request, "profesores.html")

def estudiantes(request):
    return render(request, "estudiantes.html")

def entregables(request):
    return render(request, "entregables.html")

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "inicio.html")