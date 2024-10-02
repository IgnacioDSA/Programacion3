from Producto import Producto

class Compra(Producto):
      def __init__(self, ListProd, ListComp):
            self.ListaProductos = ListProd
            self.ListaCompras = ListComp
            self.__Codigos = []
            self.nFactura = None
            self.fechaCompra = None
            self.fechaVencFactura = None
            self.modoPago = None
            self.listProductos = None
            self.Valido = None
            self.total = None
    
      def getCodigo(self):
        for compra in self.ListaCompras:
            for producto in self.ListaProductos:
                if str(compra) == producto[1]:  # Comparar el nombre de la compra con el nombre del producto
                    self.__Codigos.append(producto[0])
        return self.__Codigos
    
      def obtenerProductos(self, ids):
        
        productos_encontrados = []
        for producto in self.ListaProductos:
            if producto[0] in ids:
                productos_encontrados.append(producto)
        return productos_encontrados
        return None

      def nFactura(self):
          
          return
      
  
      


print('<< Persona is ok! >>')