from django.shortcuts import render


# Create your views here.

def home(request):

    return render(request,"Proyecto_web/home.html")



def tienda(request):

    return render(request,"Proyecto_web/tienda.html")



def contacto(request):

    return render(request,"Proyecto_web/contacto.html")