from django.shortcuts import render,HttpResponse
from .models import *
from django.db.models import Subquery, Count, OuterRef, Max
# Create your views here.
def index(request):
    varEstudianteGrupo1 = Estudiante.objects.filter(grupo=1)
    varEstudianteGrupo4 = Estudiante.objects.filter(grupo=4)
    
    edad_counts = Estudiante.objects.values('edad').annotate(count=Count('edad')).filter(count__gt=1)
    max_count = edad_counts.aggregate(max_count=Max('count'))['max_count']
    edades = Subquery(edad_counts.filter(count=max_count).values('edad'))

    varEstudianteEdad = Estudiante.objects.filter(edad__in=edades)
    apellidos_counts = Estudiante.objects.values('apellidos').annotate(count=Count('apellidos')).filter(count__gt=1)
    max_count = apellidos_counts.aggregate(max_count=Max('count'))['max_count']
    estudiantes1 = Estudiante.objects.filter(apellidos__in=apellidos_counts.filter(count=max_count).values('apellidos'))
    estudiantes3 = Estudiante.objects.filter(grupo__exact=3, edad__exact=22)
    todoestudiantes = Estudiante.objects.all()
    return render(request,'index.html',{'varEstudianteGrupo1':varEstudianteGrupo1,'varEstudianteGrupo4':varEstudianteGrupo4,'varEstudianteApellido':estudiantes1,'varEstudianteEdad':varEstudianteEdad,'varTodo':todoestudiantes,'var3':estudiantes3})
