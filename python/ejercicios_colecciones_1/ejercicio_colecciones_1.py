"""
Ejercicio 1: Eliminar duplicados de una lista.
Crear un programa donde tenga una lista y que a continuación
elimine los elemnetos repetidos, por último mostrar la lista
"""

lista = [
    "Juan Pablo",
    "Gabriel",
    "Franco",
    "Maximiliano",
    "Agustín",
    "Elias",
    "Daniela",
    "Marina",
    "Cinthia",
    "Daniela",
    "Marina",
]

print(
    f"""
      Lista con integrantes repetidos
      """
)
print(len(lista))

for el in lista:
    if el == el in lista:
        lista.remove(el)
        print(
            f"""
              Integrantes: {el}
              """
        )
