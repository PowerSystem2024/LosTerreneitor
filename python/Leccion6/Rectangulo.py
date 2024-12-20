class Rectangulo:
  
  """
  Crear una clase llamada rectángulo, debe tener 2 atributos: altura y base
  el nombre del método será calcular_area, utilizando la fórmula: area = base * altura.
  Pero la base y altura deben ser ingresadas por el usuario y los objetos deben ser tres.
  """
  
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  
  def calcular_area(self):
    return self.base * self.altura

base = int(input("Digite el número para la base del rectángulo: "))
altura = int(input("Digite el número para la altura del rectángulo: "))

rectangulo1 = Rectangulo(base, altura)

print(f"El área del rectángulo es: {rectangulo1.calcular_area()}")