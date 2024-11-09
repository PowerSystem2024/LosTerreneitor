# Tarea: Encapsular los atributos y agregar los métodos getters and setters.
# Crear otro objeto, pasar los datos para nombre, edad y sueldo.
# Mostrar estos datos, luego modificar y mostrar nuevamente.

class Persona:  # Esta clase hereda de la clase Object
  def __init__(self, nombre, edad):
    self._nombre = nombre
    self._edad = edad
  
  @property
  def nombre(self):
    print("Estamos utilizando el método get")
    return self._nombre
  
  @nombre.setter
  def nombre(self, nombre):
    print("Estamos utilizando el método set, se modifica el atributo")
    self._nombre = nombre
  
  @property
  def edad(self):
    return self._edad
  
  @edad.setter
  def edad(self, edad):
    self._edad = edad
  
  def __str__(self):  # Override = Sobreescribir
    return f"Persona: [Nombre: {self._nombre}, Edad: {self._edad}]"

class Empleado(Persona):  # Esta clase es hija de la clase Persona
  def __init__(self, nombre, edad, sueldo):
    super().__init__(nombre, edad)
    self._sueldo = sueldo
  
  @property
  def sueldo(self):
    return self._sueldo
  
  @sueldo.setter
  def sueldo(self, sueldo):
    self._sueldo = sueldo
  
  def __str__(self):
    return f"Empleado: [Sueldo: {self._sueldo}] {super().__str__()}"

empleado1 = Empleado("Pedro", 26, 456123)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

empleado2 = Empleado("Inés", 38, 759135)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado2.nombre = "Francisco"
empleado2.edad = 23
empleado2.sueldo = 809423
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)