from django import forms

class Formulario_Contacto(forms.Form):

    nombre=forms.CharField(label="Nombre")

    email=forms.EmailField(label="Email")

    contenido=forms.CharField(widget=forms.Textarea,label="Contenido")