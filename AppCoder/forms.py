from django import forms

class ProfesorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)

class CursoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.CharField(max_length=50)

class EntregableForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    fecha_entregable=forms.DateField()
    entregado=forms.BooleanField()

class EstudianteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)