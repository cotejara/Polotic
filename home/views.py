from django.shortcuts import redirect, render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Categoria, Producto
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group


# Create your views here.
def home(request):
    #tareas = Tarea.objects.all() #para obtener todoslos registros de la tabla
    context = {"lista_categorias": Categoria.objects.all(), "listado_productos": Producto.objects.order_by('-id')}
    users_in_group = Group.objects.get(name="comunes").user_set.all()
    return render(request,'home/index.html', context) 

def producto(request,  producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    context = {"producto": un_producto}
    context = {"lista_categorias": Categoria.objects.all(), "listado_productos": Producto.objects.order_by('-id')}
    return render(request,'home/producto.html', context) 

@login_required()
def detalle_producto(request,  producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    context = {"producto": un_producto}    
    return render(request,'home/detalle_producto.html', context) 

def filtro_secciones(request, categoria_id):
    una_categoria = get_object_or_404(Categoria, id=categoria_id)
    busca_producto = Producto.objects.all()
    busca_producto = busca_producto.filter(categoria=una_categoria)

    return render(request,"home/producto.html", {
        "listado_productos": busca_producto,
        "lista_categorias": Categoria.objects.all(),
        "categoria_seleccionada": una_categoria
    })

def busca_producto(request):
    print('Entro a busca_producto')
    if 'q' in request.GET:
        q = request.GET['q']
        print(q)
        if q != '':
            busca_producto= Producto.objects.filter(description__contains=q)
            if busca_producto.count() > 0:
                print('Encontro producto:', str(busca_producto))
        else:
            busca_producto =''
            
    context = {"listado_productos": busca_producto}
            
    return render(request,'home/busca_producto.html', context)     

def acerca(request):
    return render(request,'home/acerca.html')     

#@permission_required('home:view_agregar')
def agregar(request):
    if request.method == "POST":        
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            context = {"lista_categorias": Categoria.objects.all(), "listado_productos": Producto.objects.order_by('-id')}
            return redirect("index")
        else:
            print('error al querer grabar')
    else:
        form = ProductoForm()
        context = {'form': form}
        return render(request,'home/agregar.html', context) 


def contacto(request):
    if request.method == 'POST':
        subject = request.POST["asunto"]
        mensaje = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER 
        recibe_list = ['josejararojas@gmail.com']
        send_mail(subject, mensaje, email_from, recibe_list)

        context = {"lista_categorias": Categoria.objects.all(), "listado_productos": Producto.objects.order_by('-id')}
        return render(request,'home/index.html', context)

    return render(request,'home/contacto.html')          


@permission_required('home.change_producto')
def editar(request, producto_id):
    un_producto = Producto.objects.get(id=producto_id)
    if request.method == "POST":        
        form = ProductoForm(request.POST, request.FILES, instance = un_producto)
        if form.is_valid():
            form.save() 
            context = {"lista_categorias": Categoria.objects.all(), "listado_productos": Producto.objects.order_by('-id')}
            return redirect("index")
        else:
            print('error al querer grabar')
    else:
        form = ProductoForm(instance = un_producto)
        context = {'form': form}
        return render(request,'home/editar.html', context) 


def eliminar(request, producto_id):
    un_producto = Producto.objects.get(id=producto_id)  #get_object_or_404(Producto, id=producto_id) #
    un_producto.delete()
    context = {"lista_categorias": Categoria.objects.all(), "listado_productos": Producto.objects.order_by('-id')}
    return redirect("index")

