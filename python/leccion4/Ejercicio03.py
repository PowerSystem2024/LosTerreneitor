# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario introduzca un número 0, nuestro programa dejaría de insertar.
# Por último, mostrar los números ordenados de menor a mayor.

lista = []
salir = False

while not salir:
  numero = int(input("Digite un número: "))
  if numero == 0:
    salir = True
  else:
    lista.append(numero)

lista.sort()  # Esta función es para ordenar la lista
print(f"\nLista ordenada: \n{lista}")