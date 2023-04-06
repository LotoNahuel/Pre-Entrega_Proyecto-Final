from django.shortcuts import render
from .models import *
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

def CursoFormulario(request):
    return render(request, "curso.html")

def cursos(request):
    return render(request, "cursos.html")

def profesores(request):
    profesores = Profesor.objects.all()
    context = {"prefesores": profesores}
    return render(request, "profesores.html", context)

def estudiantes(request):
    return render(request, "estudiantes.html")

def entregables(request):
    return render(request, "entregables.html")

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "inicio.html")