class Persona:  # Creamos una persona
  
  def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama método Init Dunder
    self.nombre = nombre
    self.apellido = apellido
    self._dni = dni  # Este atributo está encapsulado de una manera sugerida.
    self.edad = edad
    self.args = args
    self.kwargs = kwargs
  
  def mostrar_detalle(self):  # self es igual a this (se le puede cambiar el nombre, pero python recomienda esta palabra reservada)
    print(f"La clase Persona tiene los siguientes datos: Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self._dni}, edad: {self.edad} años, dirección: {self.args}, datos importantes: {self.kwargs}")

persona1 = Persona("Pedro", "Picapiedra", 3232153, 33)  # Necesitamos enviar argumentos
print(f"El objeto1 de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es de {persona1.edad} años.")

persona2 = Persona("Pablo", "Mármol", 3312425, 32)
print(f"El objeto2 de la clase persona es: {persona2.nombre} {persona2.apellido} y su edad es de {persona2.edad} años.")

persona1.nombre = "Vilma"
persona1.apellido = "Picapiedra"
persona1.edad = "30"
print(f"El objeto1 modificado, de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es de {persona1.edad} años.")


# Los atributos son: Características.
# Los métodos son: El comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle()  # La referencia se pasa de manera automática
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1)  # Debemos pasarle una referencia para el self, de lo contrario dará error.

persona1.telefono = "1154886687"  # Hemos creado un atributo de un objeto
print(f"El teléfono de {persona1.nombre} es: {persona1.telefono}")

#print(persona2.telefono)  # el objeto persona2 no tiene este atributo, da error.

persona3 = Persona("Ismael", "Aranda", 32314326, 27, "Telefono", "153308864056", "Calle Pinedo", 678, "Manzana", 9, "Casa", 10, Altura= 1.77, Peso=80, CFavorito="Celeste", Auto="Peugeot", Modelo=2023)
persona4 = Persona("Rodrigo", "Martínez", 32543786, 29, "Telefono", "1554389543", "Calle Sin Salida", 123, "Manzana", 4, "Casa", 5, Altura= 1.87, Peso=92, CFavorito="Rojo", Auto="Citroën", Modelo=2024)

persona3.mostrar_detalle()
#print(persona3._dni)  # No se debería usar en python (está encapsulado), esto dice que lo desconocemos.
persona4.mostrar_detalle()

#persona3.__nombre  # Está totalmente encapsulado, es la manera de hacerlo estrictamente. Tampoco acepta ningún tipo de cambio.