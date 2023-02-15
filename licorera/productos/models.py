from django.db import models
from categorias.models import Categoria
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    imagen = models.CharField(max_length=300, null = True)
