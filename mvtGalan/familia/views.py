from django.shortcuts import render

from familia.models import Familiares

# Create your views here.
def ver_familia(request):
    
    personas=Familiares.objects.all()
    return render(request, "template_flia.html",{"personas":personas})


def crear_familia(request):
    persona1=Familiares.objects.create(nombre="Marcelo", hijos=3 ,fecha_nac='1985-01-25')
    persona2=Familiares.objects.create(nombre="Guadalupe", hijos=0 ,fecha_nac='1970-12-10')
    persona3=Familiares.objects.create(nombre="Francisco", hijos=1 ,fecha_nac='1990-05-13')
    return render(request,"template_crea.html")