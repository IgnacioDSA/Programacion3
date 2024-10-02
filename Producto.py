import datetime as dt


class Producto:
  def __init__(self, ListProd):
    
    self.ListaProductos = ListProd
    
    self.__Codigo = None

  def CrearProducto(self):
    self.Nombre = input("Ingrese nombre del producto: ")
    self.Marca = input("Ingrese Marca del producto: ")
    self.Modelo = input("Ingrese Marca del producto: ")
    self.Cantidad = input("Ingrese cantidad del producto: ")
    self.Unidad = input("Ingrese unidad del producto: ")
    self.Stock = input("Ingrese stock del producto:")
    self.Precio = input("Ingrese precio del producto: ")
    self.Activo = input("Ingrese si el producto esta activo: ")
    self.FechaVenc = input("Ingrese fecha de vencimiento del producto: ")
    self.FechaFabr = input("Ingrese fecha de fabricacion del producto: ")
    self.__setCodigo()
    TempList = [self.__Codigo, self.Nombre, self.Marca, self.Modelo, self.Cantidad, self.stock, self.Unidad, self.precio, self.Activo, self.FechaVenc, self.FechaFabr]
    self.ListaProductos.append(TempList)
    return
  def __setCodigo(self):
    num_lineas = len(self.ListaProductos)
    self.__Codigo = "P"+str(num_lineas)
    return

  def setStock(self):
    self.Stock = input("Ingrese el stock inicial por favor: ")
    return

  def agregarProducto(self, NewProd):
    self.__setCodigo()
    TempList = [self.__Codigo,NewProd[0],NewProd[1],NewProd[2],NewProd[3],NewProd[4],NewProd[5],NewProd[6],NewProd[7],NewProd[8],NewProd[9]]
    self.ListaProductos.append(TempList)
    return

  def retornarProducto(self, Unidades):
    self.Cantidad -= Unidades
    self.Stock += Unidades
    return
  
  def borrarDatosProducto(self):
    self.__Codigo = None
    self.Nombre = None
    self.Marca = None
    self.Modelo = None
    self.Cantidad = None
    self.Stock = None
    self.Unidad = None
    self.Precio = None
    self.Activo = None
    self.FechaVenc = None
    self.FechaFabr = None

  def setFechaVen(self, Fecha, d, m, a):
    self.FechaVenc = Fecha(d, m, a)
    return

  def getFechaVen(self):
    return self.FechaVenc

  def imprimirProducto(self):
    print(f"Código: {self.__Codigo}\n")
    print(f"Nombre: {self.Nombre}\n")
    print(f"Marca: {self.Marca}\n")
    print(f"Modelo: {self.Modelo}\n")
    print(f"Cantidad: {self.Cantidad}\n")
    print(f"Stock: {self.Stock}\n")
    print(f"Unidad: {self.Unidad}\n")
    print(f"Precio: {self.Precio}\n")
    print(f"Activo: {self.Activo}\n")
    print(f"Fecha de Vencimiento: {self.FechaVenc}\n")
    print(f"Fecha de Fabricación: {self.FechaFabr}\n")

print('<< Producto is ok! >>')