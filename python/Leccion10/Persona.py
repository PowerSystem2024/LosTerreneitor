class Persona:
  contador_personas = 0  # Variable de clase
  
  @classmethod
  def generar_siguiente_valor(cls):
    cls.contador_personas += 1  # Vamos incrementando
    return cls.contador_personas
  
  def __init__(self, nombre, edad):
    Persona.contador_personas += 1  # Vamos incrementando
    self.id_persona = Persona.contador_personas
    self.nombre = nombre
    self.edad = edad
  
  def __str__(self):
    return f"Persona [Numero: {self.id_persona} = Nombre: {self.nombre}, Edad: {self.edad}]"

persona1 = Persona("Juan", 31)
print(persona1)
persona2 = Persona("Sergio", 28)
print(persona2)
persona3 = Persona("Aurelia", 25)
print(persona3)
Persona.generar_siguiente_valor()
persona4 = Persona("Isabella", 21)
print(persona4)

print("")
print(f"Valor contador personas: {Persona.contador_personas}")