from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):

    return render(request,"Proyecto_web/home.html")



def tienda(request):

    return render(request,"Proyecto_web/tienda.html")


def blog(request):

    return render(request,"Proyecto_web/blog.html")


def contacto(request):

    return render(request,"Proyecto_web/contacto.html")