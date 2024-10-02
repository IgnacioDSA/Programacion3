from Persona import Persona

class Cliente(Persona):
  def __init__(self, Puntos, Nombre, CI, FechaNac, FechaIng, Codigo, Correo, Direcc):
    super().__init__(Nombre, CI, FechaNac, FechaIng, Codigo, Correo, Direcc)
    self.Puntos = Puntos

  def imprimirCliente(self):
    print(f"Nombre: {self.Nombre}\n")
    print(f"CI: {self.CI}\n")
    print(f"Fecha de Nacimiento: {self.FechaNac}\n")
    print(f"Fecha de Ingreso: {self.FechaIng}")
    print(f"Codigo: {self.__Codigo}\n")
    print(f"Correo: {self.Correo}\n")
    print(f"Domicilio: {self.Direccion}\n")
    print(f"Puntos obtenidos: {self.Puntos}\n")

  def eliminarDatosCliente(self):
    OP = str(input("Está seguro que desea eliminar al usuario? y/n\n"))
    if OP == 'y':
      print("Eliminanco cliente...")
      del(self.Nombre)
      del(self.CI)
      del(self.FechaNac)
      del(self.FechaIng)
      del(self.__Codigo)
      del(self.Correo)
      del(self.Direccion)
      del(self.Puntos)
      print("Proceso finalizado.")
      return
    elif OP == 'n':
      print("Abortando eliminación...\n")
      return
    else: 
      print("Ingrese una opción válida.\n")

print('<< Persona is ok! >>')