from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
  
  contador_teclado = 0
  
  def __init__(self, marca, tipo_entrada):
    Teclado.contador_teclado += 1
    self._id_teclados = Teclado.contador_teclado
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
    return f"ID: {self._id_teclados}, Marca: {self._marca}, Tipo entrada: {self._tipo_entrada}"

if __name__ == "__main__":
  teclado1 = Teclado("HyperX", "USB")
  print(teclado1)
  teclado2 = Teclado("Logitech", "Bluetooth")
  print(teclado2)