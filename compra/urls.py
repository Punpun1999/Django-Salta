from django.urls import path
from .views import (listado_productos,
                    agregar_producto,
                    lista_proveedores,
                    agregar_proveedor,
                    modificar_producto,
                    eliminar_producto,
                    desactivar_producto,
                    activar_producto,
                    pagina_principal)

urlpatterns=[
    path('listado_productos/',listado_productos,name='listado_productos'),
    path('agregar_producto/',agregar_producto,name='agregar_producto'),
    path('lista_proveedores/',lista_proveedores,name='lista_proveedores'),
    path('agregar_proveedor/',agregar_proveedor,name='agregar_proveedor'),
    path(
    'modificar_producto/<int:producto_id>',
    modificar_producto,
    name='modificar_producto'),
    path('eliminar/<int:producto_id>',eliminar_producto,name='eliminar_producto'),
    path('desactivar/<int:producto_id>',desactivar_producto,name='desactivar_producto'),
    path('activar/<int:producto_id>',activar_producto,name='activar_producto'),
    path('pagina_principal',pagina_principal,name='pagina_principal')
]