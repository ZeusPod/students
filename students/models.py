from django.db import models


class Ciudad(models.Model):
     ciudad = models.CharField(max_length=255) 


     def __str__(self) -> str:
         return self.ciudad   


class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    identificacion = models.PositiveIntegerField(blank=False, null=False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre


class Ciclo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)


    def __str__(self):
        return self.nombre


class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name='materias')


    def __str__(self):
        return self.nombre


class Periodo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)


    def __str__(self):
        return self.nombre


class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='notas')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='notas')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name='notas')
    nota = models.FloatField(blank=False, null=False)


    def __str__(self):
        return f'{self.estudiante} - {self.materia} - {self.nota}'



opciones_aprobado =[
    (1, 'si'),
    (2, 'no'),
]

class Resultado(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    desercion = models.IntegerField(null=False, blank=False, choices=opciones_aprobado, default=1)
    
    def __str__(self) -> str:
        return str(self.desercion)


