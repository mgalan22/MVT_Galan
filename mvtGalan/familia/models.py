from django.db import models

class Familiares(models.Model):
    nombre=models.CharField(max_length=40)
    hijos=models.IntegerField()
    fecha_nac=models.DateField()
