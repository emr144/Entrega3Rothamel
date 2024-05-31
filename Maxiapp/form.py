from django import forms

class FormularioCliente(forms.Form):
    apellido = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)

# class FormularioEmpleado(forms.Form):
#     apellido = forms.CharField(max_length=100)
#     nombre = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     telefono = forms.CharField(max_length=15)

# class FormularioProveedor(forms.Form):
#     nombre = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     telefono = forms.CharField(max_length=15)
#     direccion = forms.CharField(widget=forms.Textarea, required=False)