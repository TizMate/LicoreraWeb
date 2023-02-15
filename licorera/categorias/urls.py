from django.urls import path
from unicodedata import name
from . import views

urlpatterns = [
    path('categorias/new', views.crear_categoria, name='nuevo_categoria'),
    path('categorias/<id>/', views.categoria_view, name='categoria_view'),
    path('categorias/', views.listarCategorias, name='categorias'),
    path('categorias/update/<id>/', views.update_categoria, name='categoria_actualizar'),
    path('categorias/delete/<id>/', views.delete_view, name='categoria_eliminar')

]