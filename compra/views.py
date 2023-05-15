from django.shortcuts import render,HttpResponse,redirect

from compra.models import Proveedor,Producto

# Create your views here.
def listado_productos(request):
    lista_productos= Producto.objects.all()
    
    context={
        'listado_productos':lista_productos
    }
    return render(
        request,
        'compra/listado_productos.html',
        context
    )
def agregar_producto(request):
    listado_Proveedor= Proveedor.objects.all()

    context={
        'listado_Proveedor':listado_Proveedor
    }
    if request.POST:
        nombre_producto=request.POST['nombre']
        precio_producto=request.POST['precio']
        stock_producto=request.POST['stock']
        proveedor_id=request.POST['proveedor']

        Producto.objects.create(
            nombre=nombre_producto,
            precio=precio_producto,
            stock_actual=stock_producto,
            proveedor_id=proveedor_id,

        )
        return redirect('listado_productos')

    return render(
        request,
        'compra/agregar_producto.html',
        context
    )
def lista_proveedores(request):
    listados_Proveedor= Proveedor.objects.all()

    context={
        'lista_proveedor':listados_Proveedor
    }
    return render(
        request,
        'compra/lista_proveedor.html',
        context
    )
def agregar_proveedor(request):
    lista_proveedor = Proveedor.objects.all()

    context = {
        "listado_proveedor": lista_proveedor
    }

    if request.POST:
        nombre_proveedor = request.POST["nombre"]
        apellido_proveedor = request.POST["apellido"]
        dni_proveedor = request.POST["dni"]
        
       
        Proveedor.objects.create(
            nombre=nombre_proveedor,
            apellido=apellido_proveedor,
            dni=dni_proveedor,
            
        )
    return render(
        request,
        "compra/agregar_proveedor.html",
        context
    )
def modificar_producto(request,producto_id):
    listado_Proveedor= Proveedor.objects.all()
    producto= Producto.objects.get(id=producto_id)

    context={
        'listado_Proveedor':listado_Proveedor,
        'producto': producto
    }
    if request.POST:
        nombre_producto = request.POST["nombre"]
        precio_producto = request.POST["precio"]
        proveedor_id = request.POST["proveedor"]

        producto.nombre = nombre_producto
        producto.precio = precio_producto
        producto.proveedor_id = proveedor_id

        producto.save()

        return redirect('listado_productos')


    return render(
        request,
        'compra/modificar_producto.html',
        context
    )
def eliminar_producto(request,producto_id):
    try:
        producto=Producto.objects.get(id=producto_id)
        producto.delete()
    except:
        return HttpResponse('No existe el producto')
    return redirect('listado_productos')
def desactivar_producto(request,producto_id):
    producto=Producto.objects.get(id=producto_id)
    producto.activo = False
    producto.save()

    return redirect('listado_productos')

def activar_producto(request,producto_id):
    producto=Producto.objects.get(id=producto_id)
    producto.activo = True
    producto.save()
    
    return redirect('listado_productos')
def pagina_principal(request):
    return render(
        request,
        'compra/home.html',
    )