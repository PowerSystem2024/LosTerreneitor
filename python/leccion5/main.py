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
