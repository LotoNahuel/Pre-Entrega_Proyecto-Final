from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse
from .forms import ProfesorForm
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
    return render(request, "cursos.html")

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
    return render(request, "estudiantes.html")

def entregables(request):
    return render(request, "entregables.html")

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