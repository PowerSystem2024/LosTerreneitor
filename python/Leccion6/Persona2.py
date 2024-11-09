class Persona2:
  def __init__(self, nombre, apellido, edad):  # Está encapsulado
    self._nombre = nombre
    self._apellido = apellido
    self._edad = edad
  
  def mostrar_detalles(self):
    print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido}, edad {self._edad}")
  
  # Método Getter     MUESTRA
  @property  # Decorador
  def nombre(self):
    print("Estamos utilizando el método get")
    return self._nombre
  
  # Método Setter     MODIFICA
  @nombre.setter
  def nombre(self, nombre):
    print("Estamos utilizando el método set, se modifica el atributo")
    self._nombre = nombre
  
  @property
  def apellido(self):
    return self._apellido
  
  @apellido.setter
  def apellido(self, apellido):
    self._apellido = apellido
  
  @property
  def edad(self):
    return self._edad
  
  @edad.setter
  def edad(self, edad):
    self._edad = edad
  
  def __del__(self):
    print(f"De la clase Persona2: {self._nombre} {self._apellido} {self._edad}")

if __name__ == "__main__":
  persona1 = Persona2("Pedro", "Rodriguez", 29)
  print(persona1.nombre, persona1.apellido, persona1.edad)  # Llamamos al método getter

  persona1.nombre = "Fernando"  # Llamamos el método setter
  persona1.apellido = "Pérez"
  persona1.edad = 39
  print(persona1.nombre, persona1.apellido, persona1.edad)  # Otra vez con el método getter

  print(persona1.mostrar_detalles())  # Llamamos el método mostrar detalles

  # Atributo read-only sería la edad porque no tiene el método set.
  print(persona1.edad)


  # Crear tres objetos más, utilizando los métodos getter and setter, para mostrar y modificar los cambios.
  persona2 = Persona2("Romina", "García", 28)
  print(persona2.nombre)
  print(persona2.apellido)
  print(persona2.edad)
  persona2.nombre = "Pamela"
  persona2.apellido = "Miranda"
  persona2.edad = 23
  print(persona2.mostrar_detalles())

  persona3 = Persona2("Jorge", "Quintana", 49)
  print(persona3.nombre)
  print(persona3.apellido)
  print(persona3.edad)
  persona3.nombre = "Ruben"
  persona3.apellido = "Ramallo"
  persona3.edad = 52
  print(persona3.mostrar_detalles())

  persona4 = Persona2("Pablo", "Quiroz", 35)
  print(persona4.nombre)
  print(persona4.apellido)
  print(persona4.edad)
  persona4.nombre = "Agustín"
  persona4.apellido = "Battaglia"
  persona4.edad = 28
  print(persona4.mostrar_detalles())

  print(__name__)