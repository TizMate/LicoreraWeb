from django.urls import path
from unicodedata import name
from . import views

urlpatterns = [
    path('productos/new', views.crear_producto, name='nuevo_producto'),
    path('productos/<id>/', views.producto_view, name='producto_view'),
    path('productos/', views.listarProductos, name='productos'),
    path('productos/update/<id>/', views.update_producto, name='producto_actualizar'),
    path('productos/delete/<id>/', views.delete_view, name='producto_eliminar'),
    path('',views.index,name='index')
]


