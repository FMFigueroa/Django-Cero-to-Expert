from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from.forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

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
@login_required
def contacts(request):
    data = {
        'form': ContactoForm() # Variable que se imprime en la platilla html.
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #data["mensaje"] = "Contacto Enviado"
            messages.success(request, "Su mensaje fue enviado correctamente..!")
        else:
            data["form"] = formulario

    return render(request, 'app/contacts.html', data)
#==================== Productos ==================================
#==================================================================
@permission_required('app1.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm() # Variable que se imprime en la platilla html.
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            #data["mensaje"] = "Producto Agregado"
            messages.success(request, "Su producto fue creado correctamente..!")
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario

    return render(request, 'producto/agregar.html', data)
#=====================================================================
@permission_required('app1.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    #=======================  Paginator  ============================
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 4)
        productos = paginator.page(page)
    except:
        raise Http404
    #================================================================
    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'producto/listar.html', data)
#====================================================================
@permission_required('app1.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, instance=producto ,files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Su producto fue editado correctamente..!")
                return redirect(to="listar_productos")
            else:
                data["form"] = formulario
    
    return render(request, 'producto/modificar.html', data)
#====================================================================
@permission_required('app1.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Su producto fue eliminado correctamente..!")
    return redirect(to="listar_productos")
#====================================================================

#================= Registro de Usuario ==============================
def registro(request):
    data = {
        'form' : CustomUserCreationForm() 
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            messages.success(request, "Su usuario fue creado correctamente..!")
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)