from django.shortcuts import render
from . import views
from django.urls import path

#importar librerias
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
#importar modelo y formulario
from .models import Categoria
from .forms import CategoriaForm


# Create your views here.


#Vista para listar categorias
def listarCategorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias':categorias}
    template = loader.get_template('categorias/categorias.html')
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un categoria
def categoria_view(request, id):
    context = {}
    context['object'] = Categoria.objects.get(id = id)
    return render(request,'categorias/categoria_detalle.html',context)

#vista para crear categorias.
def crear_categoria(request):
    context = {}
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categorias')    
    context['form'] = form
    return render(request,'categorias/crear_categoria.html', context)


#vista para actualizar categorias
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_categoria(request,id):
    context = {}
    obj = get_object_or_404(Categoria, id = id)
    #formulario que contiene la instancia
    form = CategoriaForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('categorias')    
    context['form'] = form
    return render(request, "categorias/actualizar_categoria.html", context)


#Vista para eliminar un categoria
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Categoria, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('categorias')    
    return render(request, "categorias/eliminar_categoria.html", context)