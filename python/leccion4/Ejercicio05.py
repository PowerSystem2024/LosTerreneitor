# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo

num = int(input("Digite un número positivo: "))

while num < 0:  # Mientras el número sea negativo
  print("ERROR, el número debe ser positivo.")
  num = int(input("Digite un número positivo: "))

factorial = 1  # Es la variable para calcular el factorial

for i in range(1,num+1):
  factorial *= i

print(f"\nEl factorial del número ingresado ({num}) es: {factorial}")