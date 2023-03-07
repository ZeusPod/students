from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Estudiante, Nota, Ciudad, Resultado, Materia
from django.db.models import Count
from django.db.models.functions import Coalesce
from django.db.models import Count, Q
import json


#class for Listview page home 
class EstudianteView(LoginRequiredMixin, generic.ListView):
    model = Estudiante
    template_name = 'bases/home.html'
    context_object_name = 'estudiante'
    login_url = 'students:login'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes_count'] = Estudiante.objects.count()
        context['deserciones_count'] = Resultado.objects.filter(desercion=2).count()
        context['ciudades_count'] = Ciudad.objects.count()
        return context

    

#class for detailView for students 
class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Estudiante
    template_name = 'detail.html'
    context_object_name = 'estudiante'
    login_url = 'students:login'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['notas'] = Nota.objects.filter(estudiante=self.object)
        return context


def desercion(request):
    results = Resultado.objects.filter(desercion=2).select_related('estudiante__ciudad')
    estudiantes = [result.estudiante for result in results]
    context = {
        'estudiantes': estudiantes,
    }
    return render(request, 'desercion.html', context)


def view_deserciones_por_ciudad(request):
    results = Resultado.objects.filter(desercion=2) \
        .values('estudiante__ciudad__ciudad') \
        .annotate(deserciones=Count('estudiante__ciudad__ciudad'))

    context = {
        'deserciones': results,
    }
    return render(request, 'desercion_ciudad.html', context)


def view_estudiantes_por_materia(request):
    resultados = Materia.objects.annotate(num_estudiantes=Count('notas__estudiante', distinct=True))
    labels = [resultado.nombre for resultado in resultados]
    data = [resultado.num_estudiantes for resultado in resultados]

    context = {
        'labels': labels,
        'data': data,
    }
    return render(request, 'estudiantes_por_materia.html', context)


# materias con alumnos reprobados

def materia_notas_reprobadas(request):
    notas_reprobadas = Nota.objects.filter(nota__lt=5).values('materia__nombre').annotate(cantidad=Count('id')).order_by('-cantidad')[:10]
    labels = [nota['materia__nombre'] for nota in notas_reprobadas]
    data = [nota['cantidad'] for nota in notas_reprobadas]

    context = {
        'labels': labels,
        'data': data
    }

    return render(request, 'materia_notas_reprobadas.html', context)