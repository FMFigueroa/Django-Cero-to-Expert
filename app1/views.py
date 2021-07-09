from django.shortcuts import render
from .models import Producto
from.forms import ContactoForm, ProductoForm

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data) # luego de templates, colocar path que deseamos ver. 

def products(request):
    return render(request, 'app/products.html')

def projects(request):
    return render(request, 'app/projects.html')

def courses(request):
    return render(request, 'app/courses.html')

def blog(request):
    return render(request, 'app/blog.html')

#===========================================================
#====================== Forms ==============================
def contacts(request):
    data = {
        'form': ContactoForm() # Variable que se imprime en la platilla html.
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Enviado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacts.html', data)

#==================================================================
def agregar_producto(request):
    data = {
        'form2': ProductoForm() # Variable que se imprime en la platilla html.
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto Agregado"
        else:
            data["form"] = formulario

    return render(request, 'producto/agregar.html', data)

#=====================================================================
def listar_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'producto/listar.html', data)