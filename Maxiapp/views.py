from django.urls import path
from django.shortcuts import render
from .models import Cliente, Empleado, Proveedor
from django.http import HttpResponse
from Maxiapp.form import FormularioCliente     #, FormularioEmpleado, FormularioProveedor

def inicio(req):
     return render  (req,"Inicio.html",{})

def cliente(req):
     cliente=Cliente.objects.all()
     return render  (req,"Clientes.html",{"cliente":cliente})

def empleado(req):
     empleado=Empleado.objects.all()
     return render  (req,"Empleados.html",{"empleado":empleado})

def proveedor(req):
     proveedor=Proveedor.objects.all()
     return render  (req,"Proveedores.html",{"proveedor":proveedor})

def formularioCliente(request):
    if request.method == "POST":

        miFormulario = FormularioCliente(request.POST)
        if miFormulario.is_valid():
           
            informacion = miFormulario.cleaned_data
            cliente = Cliente(
                apellido=informacion["apellido"],
                nombre=informacion["nombre"],
                email=informacion["email"],
                telefono=informacion["telefono"]
            )
            cliente.save()
            
            return redirect('inicio')
    else:
        
        miFormulario = FormularioCliente()
    
    
    return render(request, "Maxiapp/formularioCliente.html", {"miFormulario": miFormulario})