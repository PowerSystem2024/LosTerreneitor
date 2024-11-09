class Empleado:  # Hereda de la clase object
  def __init__(self, nombre, sueldo):
    self.nombre = nombre
    self.sueldo = sueldo
  
  def __str__(self):
    return f"Empleado: [{self.nombre}, Sueldo: US${self.sueldo}]"
  
  def mostrar_detalles(self):
    return self.__str__()