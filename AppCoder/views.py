from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
from django.db.models import Q
# Create your views here.

def CursoFormulario(request):
    return render(request, "curso.html")

def cursos(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():            
            curso = Curso()
            curso.nombre = form.cleaned_data["nombre"]
            curso.comision = form.cleaned_data["comision"]
            curso.save()
            form = CursoForm()
    else:
        form = CursoForm()

    cursos = Curso.objects.all()
    context = {"cursos": cursos, "form" : form}
    return render(request, "cursos.html", context)

def buscarComision(request):
    comision = request.GET["comision"]
    if comision != "":
        cursos= Curso.objects.filter(comision = comision)
        return render (request, "cursos.html", {"cursos": cursos})
    else:
        return render (request, "cursos.html", {"mensaje": "Campo Requerido a completar"})

def profesores(request):
    
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():            
            profesor = Profesor()
            profesor.nombre = form.cleaned_data["nombre"]
            profesor.apellido = form.cleaned_data["apellido"]
            profesor.email = form.cleaned_data["email"]
            profesor.save()
            form = ProfesorForm()
    else:
        form = ProfesorForm()

    profesores = Profesor.objects.all()
    context = {"profesores": profesores, "form" : form}
    return render(request, "profesores.html", context)

def buscarProfesor(request):
    id = request.GET["id"]
    if id != "":
        profesores = Profesor.objects.filter(id = id)
        return render(request, "profesores.html", {"profesores": profesores})
    else:
        return render(request, "profesores.html", {"mensaje": "Campo requerido a completar"})

def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():            
            estudiante = Estudiante()
            estudiante.nombre = form.cleaned_data["nombre"]
            estudiante.apellido = form.cleaned_data["apellido"]
            estudiante.email = form.cleaned_data["email"]
            estudiante.save()
            form = EstudianteForm()
    else:
        form = EstudianteForm()

    estudiantes = Estudiante.objects.all()
    context = {"estudiantes": estudiantes, "form" : form}
    return render(request, "estudiantes.html", context)

def buscarEstudiante(request):
    id = request.GET["id"]
    if id != "":
        estudiantes= Estudiante.objects.filter(id = id)
        return render (request, "estudiantes.html", {"estudiantes": estudiantes})
    else:
        return render (request, "estudiantes.html", {"mensaje": "Campo Requerido a completar"})


def entregables(request):
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():            
            entregable = Entregable()
            entregable.nombre = form.cleaned_data["nombre"]
            entregable.fecha_entregable = form.cleaned_data["fecha_entregable"]
            entregable.entregado = form.cleaned_data["entregado"]
            entregable.save()
            form = EntregableForm()
    else:
        form = EntregableForm()

    entregables = Entregable.objects.all()
    context = {"entregables": entregables, "form" : form}
    return render(request, "entregables.html", context)

def buscarEntregable(request):
    nombre = request.GET["nombre"]
    if nombre != "":
        entregables= Entregable.objects.filter(nombre = nombre)
        return render (request, "entregables.html", {"entregables": entregables})
    else:
        return render (request, "entregables.html", {"mensaje": "Campo Requerido a completar"})

def inicio(request):
    return render (request, "inicio.html")

def inicioApp(request):
    return render(request, "inicio.html")