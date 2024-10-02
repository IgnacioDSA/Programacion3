
class Menu:
    def __init__(self):
        pass
    def menu(self):
        print("1 - Consultar informaciones")
        print("2 - Crear informacion")
        print("3 - Borrar informacion")
        print("4 - Nueva compra")
        print("5 - Mostrar Archivo")
        print("0 - Salir")
        return int(input("Ingrese una opcion: "))
    def menuConsultar(self):
        print("1 - Listar clientes")
        print("2 - Listar funcionarios")
        print("3 - Listar productos")
        print("4 - Listar compras")
        print("0 - Volver")
        return int(input("Ingrese una opcion: "))
    def menuCrear(self):
        print("1 - Crear cliente")
        print("2 - Crear funcionario")
        print("3 - Crear producto")
        print("0 - Volver")
        return int(input("Ingrese una opcion: "))
    def menuBorrar(self):
        print("1 - Borrar cliente")
        print("2 - Borrar funcionario")
        print("3 - Borrar producto")
        print("0 - Volver")
        int(input("Ingrese una opcion: "))
        return int(input("Ingrese una opcion: "))
    def menuComprar(self):
        print("1 - Crear compra")
        print("2 - Suspender compra")
        print("0 - Volver")
        return int(input("Ingrese una opcion: "))
    def mostrarArchivo(self, archivo):
        arch = open(archivo, 'rt')
        for linea in arch.readlines():
            print(linea)
        arch.close()
    
print('<< Menu is ok! >>')