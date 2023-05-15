from django.contrib import admin

# Register your models here.
from compra.models import Proveedor,Producto

class ProveedorAdmin(admin.ModelAdmin):
    model=Proveedor
    list_display=['id','nombre','apellido','dni']
    search_fields=[
        'dni',
    ]
class ProductoAdmin(admin.ModelAdmin):
    model=Producto
    list_display=['id','nombre','precio','stock_actual','proveedor']
    search_fields=[
        'nombre',
        'proveedor__nombre'
    ]

#registrar modelos
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto,ProductoAdmin)