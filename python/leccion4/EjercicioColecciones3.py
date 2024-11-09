# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del Señor de los Anillos

# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del Norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

# Nombre: Gimli
# Clase: Guerrero
# Raza: Enano

# Nombre: Frodo Baggins
# Clase: Agricultor
# Raza: Hobbit albo

# Nombre: Saruman el Blanco
# Clase: Mago
# Raza: Istar

personajes = []  # Creamos una lista vacía

# Creamos diccionarios
P = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Istar"}
personajes.append(P)  # Agregamos a la lista un personaje

P = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
personajes.append(P)

P = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
personajes.append(P)

P = {"Nombre": "Gimli", "Clase": "Guerrero", "Raza": "Enano"}
personajes.append(P)

P = {"Nombre": "Frodo Baggins", "Clase": "Agricultor", "Raza": "Hobbit albo"}
personajes.append(P)

P = {"Nombre": "Saruman el Blanco", "Clase": "Mago", "Raza": "Istar"}
personajes.append(P)

for personaje in personajes:
  print(personaje)
  print("-" * 30)  # Separador entre personajes
