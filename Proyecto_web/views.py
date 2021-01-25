from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def home(request):

    return render(request,"Proyecto_web/home.html")

    
def servicios(request):

    return render(request,"Proyecto_web/servicios.html")


def tienda(request):

    return render(request,"Proyecto_web/tienda.html")


def blog(request):

    return render(request,"Proyecto_web/blog.html")


def contacto(request):

    return render(request,"Proyecto_web/contacto.html")