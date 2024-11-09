# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde en una lista su tabla de multiplicar hasta el 10
# Por ejemplo: Si digita el 5, la lista tendrá: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50.

num = int(input("Digite el número que desea multiplicar: "))
lista = []  # Creamos una lista vacía

for i in range(1,11):
  lista.append(i * num)

print(f"\nEl número {num} tiene como tabla de multiplicar: {lista}\n")


for indice, i in enumerate(lista):
  print(f"{num} x {i} = {lista[indice]}")