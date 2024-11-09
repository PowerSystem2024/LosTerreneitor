# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga dos listas y que a continuación
# cree las siguientes listas (en las que no debe haber repetición)
# 1 lista de palabras que aparecen en las listas
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

lista1 = [3, 2, 5, 4, 3, 5, 2, 4, 2, 3, 5]
lista2 = [3, 6, 7, 4, 3, 6, 8, 4, 6, 8, 7]

# Eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) # Se unen ambos conjuntos
primeraLista = list(conjunto1 - conjunto2) # Solo muestra el conjunto1
segundaLista = list(conjunto2 - conjunto1) # Solo muestra el conjunto2
coincidencia = list(conjunto1 & conjunto2) # Se muestran los elementos que coinciden en ambas listas

print(f"lista de palabras que aparecen en las listas: {union}")
print(f"lista de palabras que aparecen en la primera lista, pero no en la segunda: {primeraLista}")
print(f"lista de palabras que aparecen en la segunda lista, pero no en la primera: {segundaLista}")
print(f"lista de palabras que aparecen en ambas listas: {coincidencia}")