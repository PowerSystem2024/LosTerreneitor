# Colecciones en Python
# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores.

# lista = Agus, Elias, Juan, Maxi

nombres = ["Agus", "Eli", "Juan", "Maxi"]

print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2]) # Solo muestra el índice 0, 1 pero no el índice 2.

# Ir del inicio de la lista al índice (sin incluirlo)
print(nombres [ :3]) # Indices a mostrar 0, 1 y 2

# Desde el índice indicado hasta el final
print(nombres [1: ])

# Modificamos un valor
nombres[2] = "Juan Pablo"
nombres[0] = "Agustín"
print(nombres)

# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
  print(nombre)
else:
  print("Se acabaron los elementos de la lista.")

# Preguntamos cuantos elementos tiene una lista
print(len(nombres)) # Le pasamos como parámetro la lista

# Agregamos el elemento
nombres.append("Ariel")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(6)
print(nombres)

# Insertar un elemento en un índice específico
nombres.insert(1, "Osvaldo")
print(nombres)
nombres.insert(3, "Natalia")
print(nombres)

# Eliminamos un elemento
nombres.remove("Natalia")
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminamos un índice específico
del nombres[1] # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar, limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar lista
del nombres
# print(nombres) # Acá nos muestra un error.

# Definimos una tupla
cocina = ("Cuchara", "Chuchillo", "Tenedor")
print(cocina)
print(len(cocina)) # Para saber el largo o la cantidad de elementos que contiene una tupla

# Acceder a un elemento, para esto utilizamos corchetes, no paréntesis
print(cocina[0])
# De manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ("Papa",) # La tupla, aunque sea de un elemento, necesita la coma. De lo contrario, sería un tipo str cadena.

# Recorremos los elementos de la tupla
for cocinar in cocina:
  print(cocinar, end = " ") # Print está usando \n para saltos de línea. Para que sea contínuo y eliminar estos saltos, debemos utilizar "end ="

# Para modificar una tupla (no es una buena práctica):
cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n", cocina)

# Para eliminar una tupla
# del cocina
# print(cocina) # Acá nos muestra un error

# Tipo set
planetas = {"Júpiter", "Venus", "Marte"}
print(planetas)

print(len(planetas)) # Nos muestra el largo o la cantidad que están dentro del set o conjunto.

# Revisar si un elemento existe dentro de set
print("Júpiter" in planetas)
print("Jupiter" in planetas)

print("Júpiter" not in planetas)

#Agregar un elemento
planetas.add("Tierra") # add es una función. No se puede agregar elementos duplicados.
print(planetas)

### La colección de tipo set nos sirve para evitar elementos duplicados en una lista de datos. (DNI, Nombre y apellido, matrícula, etc.)

# Eliminar elementos, puede arrojar un error si el elemento no existe.
planetas.remove("Júpiter")
print(planetas)

#planetas.remove("Venu") # No lo ejecuta, hay un error, el nombre no es el correcto
#print(planetas)

planetas.discard("tierra") # No nos tira ningún error, el código sigue corriendo
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
#del planetas
#print(planetas) # Nos muestar error, ya no existe.

# Colección Diccionario
# Messi : 10 - Un diccionario está compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key, value)

diccionario = {
  "IDE" : "Integrated Development Environment",
  "POO" : "Programación Orientada a Objetos",
  "SABD" : "Sistema de Administración de Base de Datos"
}
print(diccionario)

print(len(diccionario)) # Nos muestra el largo o la cantidad que están dentro del set o conjunto.

# Acceder a un diccionario con la llave (key)
print(diccionario["IDE"])
# print(diccionario["IDe"]) # Hay que colocar bien el detalle, ya que si no se pone igual nos da un error.

# Otra forma de recuperar un elemento
print(diccionario.get("SABD"))
print(diccionario.get("POO"))
print(diccionario.get("POo")) # Si no lo ponemos igual, el programa se ejecuta normalmente, sólo nos dice "none".

# Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Cómo recorrer los elementos
for termino in diccionario: # Recorremos solo mostrando las llaves
  print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
  print(termino, valor)

# Otras maneras de recorrer a un diccionario
for termino in diccionario.keys(): # Estamos usando una función
  print(termino) # Muestra solo las llaves.

for valor in diccionario.values(): # Usamos una función para acceder a su valor
  print(valor)

# Comprobar la existencia de algún elemento.
print("IDE" in diccionario) # Devuelve un valor booleano
print("Ide" in diccionario) # Debe estar escrito tal cual anteriormente

# Agregar elemento
diccionario["PK"] = "Primary Key" # No permite agregar llaves duplicadas, si agregamos una llave existente, se graba con el nuevo valor.
print(diccionario)

# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
#del diccionario
#print(diccionario) # Nos muestar error, ya no existe.

# Concatenamos listas
lista1 = [1, 2, 3, 3]
lista2 = [4, 5, 6, 3]
lista3 = lista1+lista2 # Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 3]) # Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Función para ubicar en qué índice está el valor ingresado.
# print(lista3.index(20)) # Esto nos da un error porque el elemento ingresado no se encuentra en la lista.

# Cómo saber cuántos valores repetidos hay dentro de una lista
print(lista3.count(3)) # Cuenta cuántos valores iguales hay dentro de la lista

# Para poner al revés una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)

lista3.sort(reverse=True) # Ordena los elementos descendentemente
print(lista3)

# Repaso de tuplas
tupla = (13, "Papa Frita", [32, 45, 3], 20.30, "Papa Frita", 20.30) # Se puede tener diferentes tipos de datos dentro
print(tupla)

print(13 in tupla) # Acción booleana, su respuesta es de tipo booleana.
# Lo que podemos utilizar dentro de tuplas es: index, count, len
# En tupla se puede convertir de tupla a lista y de lista a tupla.

# Repaso de set o conjunto
# Para definir un conjunto: Son grupo de elementos desordenados, donde su principal característica es que no puede haber duplicados. También puede tener diferente tipos de datos.

conjunto2 = set()
conjunto1 = {"Hola",} # Vacío no se le puede añadir nada. Para iniciarlo con las llaves debemos agregar un elemento para que lo caracterice como un conjunto. Solo sirve con el set()
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("Chau")
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el número 3 NO está en el conjunto1

# Cómo hacer la igualdad de dos conjuntos
print(conjunto2 == conjunto1) # Nos devuelve como respuesta un valor booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La línea une a los dos conjuntos
print(conjunto3) # No se puede repetir los elementos, los borra y queda uno.

conjunto3 = conjunto1 & conjunto2 # Elemento que tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que está en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Preguntamos si un conjunto es un subconjunto (dentro) de otro
print(conjunto3.issubset(conjunto1)) # El valor es booleano
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 están dentro del 3
print(conjunto1.issuperset(conjunto3)) # Si es verdadero, quiere decir que el conjunto3 es un: 
print(conjunto3.issuperset(conjunto2)) # Superconjunto
print(conjunto2.issuperset(conjunto3))

# Cómo saber si ambos conjuntos son disconexos, esto quiere decir que no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2))

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso de Diccionarios
diccionarioNuevo = {"Azul" : "Blue", "Rojo" : "Red", "Verde" : "Green", "Amarillo" : "Yellow"}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar distintos tipos de datos
diccionario2 = {"Juan" : {"Edad" : 30, "Altura" : 1.85}, "Pedro" : [35, 180], "Andrés" : [40, 175]}
print(diccionario2)


seleccionArgentina = {
  10: {"Nombre": "Lionel Messi", "Edad": 37, "Altura": 1.70, "Valor": "50 Millones", "Posición": "Extremo derecho"},
  11: {"Nombre": "Ángel Di María", "Edad": 36, "Altura": 1.80, "Valor": "12 Millones", "Posición": "Extremo derecho"},
  21: {"Nombre": "Paulo Dybala", "Edad": 30, "Altura": 1.77, "Valor": "35 Millones", "Posición": "Media punta"},
  19: {"Nombre": "Nicolás Otamendi", "Edad": 36, "Altura": 1.83, "Valor": "3.5 Millones", "Posición": "Defensor central"},
  1: {"Nombre": "Franco Armani", "Edad": 37, "Altura": 1.89, "Valor": "3.5 Millones", "Posición": "Arquero"},
  7: {"Nombre": "Rodrigo de Paul", "Edad": 30, "Altura": 1.80, "Valor": "13 Millones", "Posición": "Volante central"},
  24: {"Nombre": "Enzo Fernández", "Edad": 23, "Altura": 1.78, "Valor": "35 Millones", "Posición": "Volante central"},
  9: {"Nombre": "Julián Álvarez", "Edad": 24, "Altura": 1.70, "Valor": "40 Millones", "Posición": "Delantero"},
  22: {"Nombre": "Lautaro Martínez", "Edad": 27, "Altura": 1.74, "Valor": "40 Millones", "Posición": "Delantero"},
}

for llave, valor in sorted(seleccionArgentina.items()): # Utilizamos la función sorted() para ordenar la lista de menor a mayor, según el número de dorsal.
  print(llave, valor)

print("En el diccionario tenemos", (len(seleccionArgentina)), "jugadores cargados.")


# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
pila.pop()
print(pila)

elementoBorrado = pila.pop() # Elimina el último elemento y lo agrega a la variable.
print(f"Sacamos el elemento: {elementoBorrado}")
print(f"La pila ahora quedó con: {pila}")

# Colas con listas
# Estructuras de datos tipo fifo (first input / first output) (primero en entrar y primero en salir)
cola = ["Alfredo", "Román", "Rubén", "Alfonsina"]

# Agregamos elementos al final de la cola
cola.append("Raquel")
cola.append("Enrique")
cola.append("Marisa")
print("Estado inicial de la cola:",cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f"Se retira: {seRetira}")
print(cola)

#Sacamos elementos de la cola utilizando un bucle
for i in range(len(cola)):
    seRetira = cola.pop(0)  # Retiramos siempre el primer elemento
    print(f"Se retira: {seRetira}")
    print("Estado de la cola:", cola)

# Cómo recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
  print(f"{i} -> {seleccionArgentina[i]}")