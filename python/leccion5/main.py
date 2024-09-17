# Desempaquetado de listas, tuplas o diccionarios o List unpacking
def show(name, last_name):
    print(name + " " + last_name)


person = ["Gabriel", "Calcagni"]
show(person[0], person[1])  # Pasamo uno por uno los datos de la lista

# Otra forma resumida, se le pasa todo junto
person2 = ["Mario", "Meza"]
show(*person2)

# Mostramos los elementos de un diccionario
person3 = {"last_name": "Calcagni", "name": "Agustin"}
show(**person3)

# for else
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    if n == 3:
        break  # Esta es la única manera de que no se ejecute el else
    print(n)
else:
    print("Esto termina")

# Lista de compresión / List comprehension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
along_p = [p for p in names if p[0] == "P"]
print(along_p)

beers = [
    {"name": "Quilmes", "country": "Argentina"},
    {"name": "Corona", "country": "México"},
    {"name": "Stella Artois", "country": "Belgica"},
]

arg = [b for b in beers if b["country"] == "Argentina"]
print(arg)
print(beers)

# Funciones con paso de argumentos


def funcion_2(name, lastname):
    print("Saludos desde la consola de Python!")
    print(f"Nombre: {name}, Apellido: {lastname}")


funcion_2("Juan", "Carlo")


# La palabra return en funciones
def sumar(a, b):
    return a + b


resultado = sumar(6, 9)
print(f"El resultado es {resultado}")
