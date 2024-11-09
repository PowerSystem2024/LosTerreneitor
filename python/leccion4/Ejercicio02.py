# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10, luego modificar los elementos de la lista
# multiplicándolos por un valor ingresado por el usuario

lista = list(range(1,11))
print("Lista original")

print("-".join(map(str, lista))) # Esto es para que no aparezca el "-" al final de la secuencia

valor = int(input("\nDigite un valor a multiplicar: "))

# Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):  # Función para modificar los índices de la lista
  lista[indice] *= valor  # El iterador solo recorre los índices, en ésta línea se multiplica

print(f"Lista final con los elementos multiplicados por {valor}")
print("-".join(map(str, lista)))