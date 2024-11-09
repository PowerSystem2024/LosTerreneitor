# Comenzamos con Funciones

# Definimos una Función.

#mi_funcion()  # No se puede llamar antes de definir una función.
def mi_funcion():  # def es la palabra reservada
  print("Saludos a todos los chicos de Los Terreneitor.")

mi_funcion()  # Estamos llamando a la función
mi_funcion()  # Se puede llamar a una función N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
  print(name+" "+lastName)

person = ["Martín", "Pescador"]
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la función
show(*person)  # Esto es lo mismo que la anterior, pero lo pasamos todo junto.

person2 = ("Pedro", "Picapiedra")  # Desempaquetamos a través de una tupla.
show(*person2)

person3 = {"lastName": "Simpson", "name": "Homero"}  # Diccionario
show(**person3)


numbers = [1, 2, 3, 4, 5]  # Aún con la lista vacía se va a ejecutar el else.
for n in numbers:
  print(n)
  if n == 3:
    break  # Ésta es la única manera para que no se ejecute el else
else:
  print("Esto se terminó.")

# List comprehension, lista de comprensión
names = ["Pedro", "Andrés", "Julián", "Pablo", "Marisa"]
alongP = [p for p in names if p[0] == "P"]  # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]

Arg = [b for b in bottleC if b["country"] == "Arg"]

print(Arg)
print(bottleC)


# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
  print("Aguante Los Terreneitor!")
  print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Batallón Costa", "Juan Pablo")
mi_funcion2("Jacob", "Elías")
mi_funcion2("Salinas", "Agustín")
mi_funcion2("Tomio", "Maximiliano")


# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
  return a + b
#resultado = sumar(78, 22)
#print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(35, 65)}")

def sumar2(a = 0, b = 0):
  return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 33)}")


# Argumentos, variables en funciones
def listarNombres(*nombres):  # Normalmente se utiliza:  *args
  for nombre in nombres:  # Se va a convertir en una tupla
    print(nombre)
listarNombres("Andrés", "Mario", "Juliana", "Verónica", "Ismael")
listarNombres("Pedro", "Romina", "José", "Carlos", "Josefina")


def listarTerminos(**terminos):  # Normalmente se utiliza el argumento de **kwargs (significa key word argument)
  for llave, valor in terminos.items():
    print(f"{llave}: {valor}")

listarTerminos()  # Al no recibir argumentos (), no se va a mostrar nada en consola.
listarTerminos(IDE = "Integrated Development Enviroment", PK = "Primary Key")
#listarTerminos(10 = "Lionel Messi")  # Puede recibir un tipo de dato en el valor, pero no en la llave.


def desplegarNombres(nombres):
  for nombre in nombres:
    print(nombre)

nombres2 = ["José", "Ezequiel", "Elba"]
desplegarNombres(nombres2)
desplegarNombres("Roxana")
#desplegarNombres(20, 30)  # No es un objeto iterable
desplegarNombres((20, 30))  # Se convierte a una tupla iterable (los parentesis corresponden a las tuplas). Un solo elemento aunque pongamos () no lo convierte en tupla, no hay que olvidarse de la , (coma)
desplegarNombres([33, 77])  # Se convierte en una lista ([])


# Funciones recursivas
def factorial(numero):
  if numero == 1:  # Caso base
    return 1
  else:
    return numero * factorial(numero-1)  # Caso recursivo

num = int(input("Ingres el número que desee saber su factorial: "))
resultado = factorial(num)

#resultado = factorial(5)  # Lo hacemos en código duro
print(f"El factorial del número {num} es: {resultado}")

