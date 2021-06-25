from django.shortcuts import render,redirect
from .forms import Formulario_Contacto 
from django.core.mail import send_mail

# Create your views here.

def contacto(request):
    formulario_contacto=Formulario_Contacto()

    if request.method=="POST":
        formulario_contacto=Formulario_Contacto(data=request.POST)

        if formulario_contacto.is_valid():

            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            send_mail(nombre,email,contenido,['juliomederosarias@gmail.com'],)

            return redirect("/contacto/?valido")

    return render(request,"contacto/contacto.html", {'mi_formulario':formulario_contacto})





