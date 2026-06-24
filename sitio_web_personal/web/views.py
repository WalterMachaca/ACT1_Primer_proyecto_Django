from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def acerca(request):
    return render(request, 'acerca.html')

def habilidades(request):
    return render(request, 'habilidades.html')

def contacto(request):
    return render(request, 'contacto.html')
