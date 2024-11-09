# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro de un rango, por ejemplo:
# suma de números pares del 2 al 30. Suma = 240

num1 = (int(input("Digite desde dónde va a comenzar la suma: ")))
num2= (int(input("Digite hasta dónde va a finalizar la suma: ")))

suma = 0

for i in range(num1,num2+1):
  if i % 2 == 0:  # Esto es si el número es par
    suma += i

print(f"\nLa suma de números pares dentro del rango es: {suma}")