class Aritmetica:
  """
  El nombre de este tipo de comentario es: DocString
  esto es documentación de la clase en python
  Vamos hacer en esta clase algunas operaciones de: suma, resta, multiplicación y más.
  """
  
  def __init__(self, operandoA, operandoB):
    self.operandoA = operandoA
    self.operandoB = operandoB
  
  # Método de sumar
  def sumar(self):
    return self.operandoA + self.operandoB
  
  def resta(self):
    return self.operandoA - self.operandoB
  
  def multiplicar(self):
    return self.operandoA * self.operandoB
  
  def dividir(self):
    return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(3,12)  # Le pasamos los argumentos para los operandos
print(f"La suma de los números es: {aritmetica1.sumar()}")

print(f"La resta de los números es: {aritmetica1.resta()}")
print(f"La multiplicación de los numeros es: {aritmetica1.multiplicar()}")
print(f"La división de los números es: {aritmetica1.dividir():.2f}")