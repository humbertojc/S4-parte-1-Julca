from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
# Create your views here.
layout = """"""
def integrantes(request):
    integrantes = ['Jose Flores Chamba','Edson Alva Chanta','Miguel Angel Motta Mendoza']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Bienvenidos',
        'mensaje':'Proyecto para la Unidad de Competencia 04 (UC04)'
    })