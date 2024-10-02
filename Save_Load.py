import csv


class Save_Load:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar_productos(self, productos):

        with open(self.archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(productos)

    def cargar_productos(self):

        productos = []
        with open(self.archivo, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                productos.append(fila)
        return productos

    def guardar_clientes(self, clientes):

        with open(self.archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(clientes)

    def cargar_clientes(self):

        clientes = []
        with open(self.archivo, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                clientes.append(fila)
        return clientes

    def guardar_vendedores(self, vendedores):
        
        with open(self.archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(vendedores)
            
    def cargar_vendedores(self):
        
        vendedores = []
        with open(self.archivo, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                vendedores.append(fila)
        return vendedores
    
    def guardar_ventas(self, ventas):
        
        with open(self.archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(ventas)
      
print('<< [db_Gestor] is ok! >>')