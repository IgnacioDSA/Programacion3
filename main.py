import io
from Fecha import Fecha
from Fecha import FechaFactura
from Menu import Menu
from Persona import Persona
from Producto import Producto
from Compra import Compra
from Cliente import Cliente
from Save_Load import Save_Load

db = "dbProductos.txt"
ListProducts = Save_Load(db).cargar_productos()
print(ListProducts)

ListCompras = ['manzana',4324]

test1 = Compra(ListProducts, ListCompras)
test2 = test1.getCodigo()
print("\n")
print(test2)

test3 = ['P0', 'P2']
test2 = test1.obtenerProductos_ID(test3)
print(test2)


"""
while(1):
  unMenu = Menu()
  Opcion = unMenu.menu()
  if Opcion == 1:
    Opcion = unMenu.menuConsultar()
  elif Opcion == 2:
    SubOpcion = unMenu.menuCrear()
    #if SubOpcion == 1:
      #unCliente = Cliente()
    if SubOpcion == 3:
     unProducto = Producto(None, None, None, None, None, None, None, None, None, None)
     unProducto.CrearProducto()
  elif Opcion == 3:
    unMenu.menuBorrar()
  elif Opcion == 4:
    unMenu.menuComprar()
  elif Opcion == 5:
    A = input("Ingrese nombre del archivo")
    unMenu.mostrarArchivo(A)
      
  elif Opcion == 0:
    print("Gracias por usar el programa")
    exit()
  else:
    print("Opcion no válida")
  

  
"""