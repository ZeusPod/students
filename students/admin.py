from django.contrib import admin

# Register your models here.
from .models import Estudiante, Ciclo, Materia, Nota, Periodo, Ciudad, Resultado

class MateriaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'ciclo',
    )
    list_filter=('ciclo',)


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre','identificacion', 'ciudad')


class NotaAdmin(admin.ModelAdmin):
    list_display = ('estudiante',
                    'materia', 
                    'periodo', 
                    'nota')

    list_filter = ('estudiante', 'periodo')


class CiudadAdmin(admin.ModelAdmin):
    list_display =('ciudad',)


class ResultadoAdmin(admin.ModelAdmin):
    list_display =('estudiante', 'desercion')


admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Ciclo)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Nota, NotaAdmin)
admin.site.register(Periodo)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Resultado, ResultadoAdmin)