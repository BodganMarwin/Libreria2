from django.shortcuts import render
from publicidad.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from publicidad.forms import FormularioContacto

# Create your views here.

def busquedaProductos(request):
    return render(request, 'busquedaProductos.html')

def mostrarProductos(request):
    if request.GET['nameProduct']:

        producto = request.GET['nameProduct'].upper()
        articulos = Articulos.objects.filter(seccion__icontains=producto)

        # return render(request, 'mostrarProductos.html', {'articulos':request.GET['nameProduct']})
        return render(request, 'mostrarProductos.html', {'articulos':articulos, 'query':producto})
    else:
        return render(request, 'busquedaProductos.html')
    #     return render(request, 'mostrarProductos.html', {'mensaje':'introduce un producto'})

def contacto(request):
    if request.method == 'POST':

        subject=request.POST['asunto']
        message=request.POST['mensaje'] + ' ' + request.POST['email']
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['bflores@comteco.com.bo']
        send_mail(subject,message,email_from,recipient_list)

        return render(request, 'gracias.html')
    return render(request, 'contacto.html')

def contacto2(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)

        if form.is_valid():
            infform=form.cleaned_data
            send_mail(infform['asunto'],infform['mensaje'], infform.get('email',''),['bflores@comteco.com.bo'],)
            return render(request, 'gracias.html')
    else:
        form=FormularioContacto()   
    return render(request, 'contacto2.html',{'formulario':form})