from django.urls import path
from Maxiapp.views import inicio, cliente, empleado, proveedor, formularioCliente



urlpatterns = [

    path('Maxiapp/inicio/', inicio,name="inicio"),
    path('Maxiapp/cliente/', cliente,name="cliente"),
    path('Maxiapp/empleado/', empleado,name="empleado"),
    path('Maxiapp/proveedor/', proveedor,name="proveedor"),
    path('Maxiapp/formularioCliente', formularioCliente ,name="formulacioCliente"),
    path('cliente/nuevo/', formularioCliente, name='nuevo_cliente'),
]
