from django.shortcuts import render
from . import views
from django.urls import path

#importar librerias
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
#importar modelo y formulario
from .models import Producto
from .forms import ProductoForm





def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context,request))


path('',views.index,name=index)


#Vista para listar productos
def listarProductos(request):
    productos = Producto.objects.all()
    context = {'productos':productos}
    template = loader.get_template('productos/productos.html')
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un producto
def producto_view(request, id):
    context = {}
    context['object'] = Producto.objects.get(id = id)
    return render(request,'productos/producto_detalle.html',context)

#vista para crear productos.
def crear_producto(request):
    context = {}
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('productos')    
    context['form'] = form
    return render(request,'productos/crear_producto.html', context)


#vista para actualizar productos
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_producto(request,id):
    context = {}
    obj = get_object_or_404(Producto, id = id)
    #formulario que contiene la instancia
    form = ProductoForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('productos')    
    context['form'] = form
    return render(request, "productos/actualizar_producto.html", context)


#Vista para eliminar un producto
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Producto, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('productos')    
    return render(request, "productos/eliminar_producto.html", context)