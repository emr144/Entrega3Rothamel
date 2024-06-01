from django.urls import path
from Maxiapp.views import inicio,cliente, empleado, proveedor
from Maxiapp.views import nuevo_cliente, nuevo_empleado, nuevo_proveedor
from Maxiapp.views import lista_clientes, lista_empleado, lista_proveedor



urlpatterns = [

    path('Maxiapp/inicio/', inicio,name="inicio"),
    path('Maxiapp/cliente/', cliente,name="cliente"),
    path('Maxiapp/empleado/', empleado,name="empleado"),
    path('Maxiapp/proveedor/', proveedor,name="proveedor"),
    path('cliente/nuevo/', nuevo_cliente, name='nuevo_cliente'),
    path('empleado/nuevo/', nuevo_empleado, name='nuevo_empleado'),
    path('proveedor/nuevo/', nuevo_proveedor, name='nuevo_proveedor'),
    path('cliente/lista/', lista_clientes, name='lista_clientes'),
    path('cliente/lista/', lista_empleado, name='lista_empleado'),
    path('cliente/lista/', lista_proveedor, name='lista_proveedor')
]