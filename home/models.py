from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return  f"{self.descripcion}"

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos')
    description = models.CharField(max_length=500)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Carrito(models.Model):
    usuario = models.CharField(max_length=50)
    lista_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    total_carrito = models.IntegerField()

    def __str__(self):
        return self.usuario    
