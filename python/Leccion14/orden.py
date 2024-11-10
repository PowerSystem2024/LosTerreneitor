class Orden:
  
  contador_orden = 0
  
  def __init__(self, computadoras):
    Orden.contador_orden += 1
    self._id_orden = Orden.contador_orden
    self._computadoras = computadoras
  
  def agregar_computadora(self, computadoras):
    self._computadoras.append(computadoras)
  
  @property
  def computadoras(self):
    return self._computadoras
  
  @computadoras.setter
  def computadoras(self, computadoras):
    self._computadoras = computadoras
  
  def __str__(self):
    computadoras_str = ""
    for computadora in self._computadoras:
      computadoras_str += computadora.__str__()
    return f"""
      Orden: {self._id_orden}
      Computadoras: {computadoras_str}
    """