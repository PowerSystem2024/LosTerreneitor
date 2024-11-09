class Producto:
  contador_productos = 0
  
  def __init__(self, nombre, precio):
    Producto.contador_productos += 1  # Aumento para la variable de clase
    self._id_producto = Producto.contador_productos  # Asignación desde la variable de clase
    self._nombre = nombre
    self._precio = precio
  
  # Métodos setters and getters
  @property
  def nombre(self):
    return self._nombre
  
  @nombre.setter
  def nombre(self, nombre):
    self._nombre = nombre
  
  @property
  def precio(self):
    return self._precio
  
  @precio.setter
  def precio(self, precio):
    self._precio = precio
  
  # Sobreescribimos el método str()
  def __str__(self):
    return f"ID Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: US${self._precio}"

if __name__ == "__main__":  # Solo será visible si la prueba se ejecuta desde acá.
  producto1 = Producto("Remera", 50)
  print(producto1)
  producto2 = Producto("Bermuda", 75)
  print(producto2)
  producto3 = Producto("Camisa", 120)
  print(producto3)
  producto4 = Producto("Pantalón", 110)
  print(producto4)