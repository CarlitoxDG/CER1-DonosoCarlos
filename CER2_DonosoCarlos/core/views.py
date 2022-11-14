from django.shortcuts import render
from django.http import HttpResponse
from .models import Correspondencia
from django.db.models import Q
from .models import Residencia

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def verCorrespondencia(request):
    correspondenciaListada=Correspondencia.objects.all()
    filtrar = request.GET.get('buscar')

    if filtrar != '' and filtrar is not None:
        correspondenciaListada = Correspondencia.objects.filter(Q(residencia = filtrar))
    return render(request,'core/porteria.html',{"correspondencias":correspondenciaListada})