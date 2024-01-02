from django.shortcuts import render
from .forms import PersonaForm, EmpresaForm, ProductoForm
from .models import Persona,Empresa,Producto

def index(request):
    return render(request, 'index.html')

def insertData (request):
    if request.method == 'POST':
        personaForm = PersonaForm(request.POST)
        empresaForm = EmpresaForm(request.POST)
        productoForm = ProductoForm(request.POST)

        if personaForm.is_valid:
            personaForm.save()

        if empresaForm.is_valid:
            empresaForm.save()

        if productoForm.is_valid:
            productoForm.save()

    else:
        personaForm = PersonaForm()
        empresaForm = EmpresaForm()
        productoForm = ProductoForm()

    return render(request, 'insertData.html', {'personaForm': personaForm, 'empresaForm': empresaForm, 'productoForm': productoForm})

def search(request):
    people = None
    businesses = None
    products = None

    if request.method == 'POST':
        wordSearch = request.POST.get("wordSearch,''")
        people = Persona.objects.filter(nombre__icontains= wordSearch)
        businesses = Empresa.objects.filter(nombre__icontains= wordSearch)
        products = Producto.objects.filter(nombre__contains= wordSearch)
    
    return render(request, 'search.html',{
        'personas' : people,
        'empresas' : businesses,
        'productos' : products
    })


