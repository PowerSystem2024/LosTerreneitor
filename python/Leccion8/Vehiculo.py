class Vehiculo:
  """
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Auto y Bicicleta,
las cuales heredan de la clase padre Vehículo.
La clase padre debe tener los siguientes atributos y métodos:

Vehiculo (clase padre)
- Atributos (color, ruedas)
- Métodos (__init__(color, ruedas)) y __str__())

Auto (clase hija de Vehiculo)
- Atributos (velocidad (km/h))
- Métodos (__init_(color, ruedas, velocidad) y __str())

Bicicleta (clase hija de Vehiculo)
- Atributos (tipo(urbana, montaña, etc.))
- Métodos (__init_(color, ruedas, tipo) y __str())

Crear un objeto de cada clase.
  """

  def __init__(self, color, ruedas):
    self.color = color
    self.ruedas = ruedas
  
  def __str__(self):
    return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)

class Auto(Vehiculo):
  def __init__(self, color, ruedas, velocidad):
    super().__init__(color, ruedas)
    self.velocidad = velocidad
  
  def __str__(self):
    return super().__str__() + ", Velocidad (km/h): " + str(self.velocidad)

class Bicicleta(Vehiculo):
  def __init__(self, color, ruedas, tipo):
    super().__init__(color, ruedas)
    self.tipo = tipo
  
  def __str__(self):
    return super().__str__() + ", tipo: " + self.tipo

# Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo("Rojo", 8)
print(vehiculo)

# Segundo objeto: Clase Auto
auto = Auto("Negro", 4, 150)
print(auto)

# Tercer objeto: Clase Bicicleta
bici = Bicicleta("Violeta", 2, "Urbana")
print(bici)