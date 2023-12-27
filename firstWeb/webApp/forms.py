from django import forms
from .models import Persona,Empresa,Producto

class PersonaForm (forms.ModelForm):
    class Meta:
        Model = Persona
        fields = ['nombre', 'edad']

class EmpresaForm (forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre','direccion']

class ProductoForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'price']


