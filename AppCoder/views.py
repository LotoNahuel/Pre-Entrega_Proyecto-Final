from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
from django.db.models import Q
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

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "inicio.html")

def buscar(request):
    busqueda = request.GET.get('buscar')
    profesores = Profesor.objects.all()

    if busqueda:
        profesores = Profesor.objects.filter(
            Q(id__icontains = busqueda)
        ).distinct()
    return render(request, "profesores.html", {"profesores":profesores})