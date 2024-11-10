from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora:
  
  contador_computadoras = 0
  
  def __init__(self, nombre, monitor, teclado, raton):
    Computadora.contador_computadoras += 1
    self._id_computadora = Computadora.contador_computadoras
    self._nombre = nombre
    self._monitor = monitor
    self._teclado = teclado
    self._raton = raton
  
  @property
  def nombre(self):
    return self._nombre
  
  @nombre.setter
  def nombre(self, nombre):
    self._nombre = nombre
  
  @property
  def monitor(self):
    return self._monitor
  
  @monitor.setter
  def monitor(self, monitor):
    self._monitor = monitor
  
  @property
  def teclado(self):
    return self._teclado
  
  @teclado.setter
  def teclado(self, teclado):
    self._teclado = teclado
  
  @property
  def raton(self):
    return self._raton
  
  @raton.setter
  def raton(self, raton):
    self._raton = raton
  
  
  def __str__(self):
    return f"""
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Ratón: {self._raton}
    """

if __name__ == "__main__":
  teclado1 = Teclado("Logitech", "USB")
  monitor1 = Monitor("Samsung", "27 Pulgadas")
  raton1 = Raton("SteelSeries", "USB")
  computadora1 = Computadora("Asus", monitor1, teclado1, raton1)
  print(computadora1)
  
  teclado2 = Teclado("HyperX", "Bluetooth")
  monitor2 = Monitor("LG", "24 Pulgadas")
  raton2 = Raton("Logitech", "Bluetooth")
  computadora2 = Computadora("Asus", monitor2, teclado2, raton2)
  print(computadora2)