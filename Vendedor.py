from Persona import Persona

class Vendedor(Persona):
  def __init__(self, Sueldo, Horarios, Nombre, CI, FechaNac, FechaIng, Codigo, Correo, Direcc):
    super().__init__(Nombre, CI, FechaNac, FechaIng, Codigo, Correo, Direcc)
    self.Sueldo = Sueldo
    self.Horarios = Horarios
    
    def imprimirVendedor(self):
      print(f"Nombre: {self.Nombre}\n")
      print(f"CI: {self.CI}\n")
      print(f"Fecha de Nacimiento: {self.FechaNac}\n")
      print(f"Fecha de Ingreso: {self.FechaIng}")
      print(f"Codigo: {self.__Codigo}\n")
      print(f"Correo: {self.Correo}\n")
      print(f"Domicilio: {self.Direccion}\n")
      print(f"Sueldo: {self.Sueldo}\n")
      print(f"Horarios: {self.Horarios}\n")

    def eliminarDatosVendedor(self):
      OP = str(input("Está seguro que desea eliminar al vendedor? y/n\n"))
      if OP == 'y':
        print("Eliminanco operario...")
        del(self.Nombre)
        del(self.CI)
        del(self.FechaNac)
        del(self.FechaIng)
        del(self.__Codigo)
        del(self.Correo)
        del(self.Direccion)
        del(self.Sueldo)
        del(self.Horarios)
        print("Proceso finalizado.")
        return
      elif OP == 'n':
        print("Abortando eliminación...\n")
        return
      else: 
        print("Ingrese una opción válida.\n")

print('<< Vendedor is ok! >>')