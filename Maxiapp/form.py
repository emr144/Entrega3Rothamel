from django import forms
from .models import ProveedorCla, ClienteCla, EmpleadoCla


class ClienteForm(forms.ModelForm):
     class Meta:
          model=ClienteCla
          fields=["nombre","apellido","email","telefono","direccion"]


class EmpleadoForm(forms.ModelForm):
     class Meta:
          model=EmpleadoCla
          fields=["nombre","apellido","email","telefono","puesto"]

class ProveedorForm(forms.ModelForm):
     class Meta:
          model=ProveedorCla
          fields=["nombre","email","telefono","rubro","direccion"]


    
    