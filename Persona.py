import datetime as dt

class Persona:
  def __init__(self, Nombre, CI, FechaNac, FechaIng, Codigo, Correo, Direcc):
    self.Nombre = Nombre
    self.FechaNac = FechaNac
    self.FechaIng = FechaIng
    self.Correo = Correo
    self.CI = CI
    self.__Codigo = Codigo
    self.Direccion = Direcc
    
  def __setCodigo(self, Codigo):
    self.__Codigo = Codigo
    return
  def __getCodigo(self):
    return self.__Codigo
  def setCI(self):
    self.CI = input("Ingrese su CI:")
    return
  def getCI(self):
    return self.CI
  def setNombre(self):
    self.Nombre = input("Ingrese su nombre:")
    return
  def getNombre(self):
    return self.Nombre
  def setFechaNac(self):
    print("Ingrese Fecha de Nacimiento:\n")
    self.FechaNac = [input("\nDía:"), input("\nMes:"), input("\nAño:")]
  def getFechaNac(self):
    return print(self.FechaNac)
  def setFechaIng(self):
    ahora_ = dt.datetime.now()
    ahora = [ahora_.day,ahora_.month,ahora_.year]
    del(ahora_)
    self.FechaIng = ahora
    return
  def getFechaIng(self):
    return self.FechaIng
  def imprimirPersona(self):
    print(f"Nombre: {self.Nombre}\n")
    print(f"Fecha de Nacimiento: {self.FechaNac}\n")
    print(f"Fecha de Ingreso: {self.FechaIng}\n")
    print(f"Correo Electrónico: {self.Correo}\n")
    print(f"CI: {self.CI}")
    print(f"ID de comercio: {self.__Codigo}\n")
    print(f"Domicilio: {self.Direccion}\n")
    return

print('<< Persona is ok! >>')