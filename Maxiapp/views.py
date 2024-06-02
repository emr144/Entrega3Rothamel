from django.urls import path
from django.shortcuts import render ,redirect
from .models import ClienteCla, EmpleadoCla, ProveedorCla
from django.http import HttpResponse
from .form import ClienteForm, EmpleadoForm , ProveedorForm, Buscar



def inicio(req):
     form = Buscar() 
     return render  (req,"Inicio.html",{'form': form})


def cliente(req):
     cliente=ClienteCla.objects.all()
     return render  (req,"Clientes.html",{"cliente":cliente})

def empleado(req):
     empleado=EmpleadoCla.objects.all()
     return render  (req,"Empleados.html",{"empleado":empleado})

def proveedor(req):
     proveedor=ProveedorCla.objects.all()
     return render  (req,"Proveedores.html",{"proveedor":proveedor})


# Formulario Cliente
def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
     
    return render(request, "formularioCliente.html", {"form": form})

def lista_clientes(request):
    clientes = ClienteCla.objects.all()  
    return render(request, 'listaClientes.html', {'clientes': clientes})


#Formulario Empleado
def nuevo_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EmpleadoForm()
     
    return render(request, "formularioEmpleado.html", {"form": form})

def lista_empleado(request):
    empleado = EmpleadoCla.objects.all()  
    return render(request, 'listaEmpleados.html', {'empleado': empleado})


#Formulario Proveedor
def nuevo_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProveedorForm()
     
    return render(request, "formularioProveedor.html", {"form": form})

def lista_proveedor(request):
    proveedor = ProveedorCla.objects.all()  
    return render(request, 'listaProveedores.html', {'proveedor': proveedor})


def buscar(request):
    form = Buscar(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        category = form.cleaned_data['category']
        if category == 'clientes':
            results = ClienteCla.objects.filter(nombre__icontains=query)
        elif category == 'empleados':
            results = EmpleadoCla.objects.filter(nombre__icontains=query)
        elif category == 'proveedores':
            results = ProveedorCla.objects.filter(nombre__icontains=query)
    return render(request, 'formularioBusqueda.html', {'form': form, 'results': results})



