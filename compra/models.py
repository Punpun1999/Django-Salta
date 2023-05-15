from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField(default=0)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField(default=0)
    stock_actual=models.IntegerField(default=1)
    proveedor=models.ForeignKey(
        Proveedor,related_name='productos',
        on_delete=models.CASCADE
)
    activo=models.BooleanField(default=True)
