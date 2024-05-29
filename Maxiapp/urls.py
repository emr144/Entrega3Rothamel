from django.urls import path
from Maxiapp.views import inicio, cliente, empleado, proveedor



urlpatterns = [

    path('/Maxiapp/inicio/', inicio,name="inicio"),
    path('/Maxiapp/cliente/', cliente,name="cliente"),
    path('/Maxiapp/empleado/', empleado,name="empleado"),
    path('/Maxiapp/proveedor/', proveedor,name="proveedor"),
]
