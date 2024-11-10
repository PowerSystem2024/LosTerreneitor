from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
  
  contador_ratones = 0
  
  def __init__(self, marca, tipo_entrada):
    Raton.contador_ratones += 1
    self._id_raton = Raton.contador_ratones
    super().__init__(marca, tipo_entrada)
  
  @property
  def marca(self):
    return self._marca
  
  @marca.setter
  def marca(self, marca):
    self._marca = marca
  
  @property
  def tipo_entrada(self):
    return self._tipo_entrada
  
  @tipo_entrada.setter
  def tipo_entrada(self, tipo_entrada):
    self._tipo_entrada = tipo_entrada
  
  def __str__(self):
    return f"ID: {self._id_raton}, Marca: {self._marca}, Tipo entrada: {self._tipo_entrada}"


# Hacemos pruebas
if __name__ == "__main__":
  raton1 = Raton("HyperX", "USB")
  print(raton1)
  raton2 = Raton("SteelSeries", "Bluetooth")
  print(raton2)