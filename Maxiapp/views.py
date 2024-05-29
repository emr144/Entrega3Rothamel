from django.urls import path
from django.shortcuts import render
from .models import Cliente, Empleado, Proveedor
from django.http import HttpResponse


def inicio(req):
     return render  (req,"Inicio.html",{})

def cliente(req):
     cliente=Cliente.objets.all()
     return render  (req,"Clientes.html",{"cliente":cliente})

def empleado(req):
     empleado=Empleado.objects.all()
     return render  (req,"Empleados.html",{"empleado":empleado})

def proveedor(req):
     proveedor=Proveedor.objets.all()
     return render  (req,"Proveedores.html",{"proveedor":proveedor})

