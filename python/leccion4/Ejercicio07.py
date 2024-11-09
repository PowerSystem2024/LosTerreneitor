# Ejercicio 7: Adivina el número
# Realizar un juego para adivinar un número.
# Para ello se debe generar un número aleatorio entre 1 - 100, y luego ir pidiendo números
# Indicando si es "mayor" o "menor" según lo sea con respecto a N.
# El proceso termina cuando el usuario acierta y allí se debe mostrar el número de intentos.

import random

#print("\t.:JUEGO ADIVINA EL NÚMERO:.")

#aleatorio = random.randint(0, 100)  # Los números que se encuentran dentro de radiant() se toman literal, en este caso de 0 a 100. Generamos un número aleatorio.
#contador = 0

#while True:
#  numero = int(input("Digite un número: "))
#  contador += 1
#  if numero > aleatorio:
#    print("\tNo es el número correcto, digite uno menor")
#  elif numero < aleatorio:
#    print("\tNo es el número correcto, digite uno mayor")
#  else:
#    print("¡FELICIDADES!. Acabas de adivinar el número.")
#    print(f"El número correcto era: {aleatorio}")
#    break  # Rompe el ciclo y bucle

#print(f"\nEl número de intentos fue de: {contador}")

# Si queremos realizar este ejercicio con un número X de intentos:

print("\t.:JUEGO ADIVINA EL NÚMERO:.")

aleatorio = random.randint(0, 100)  # Los números que se encuentran dentro de radiant() se toman literal, en este caso de 0 a 100. Generamos un número aleatorio.
contador = 0
max_intentos = 5

while contador < max_intentos:
  numero = int(input("Digite un número: "))
  contador += 1
  
  if numero > aleatorio:
    print("\tNo es el número correcto, digite uno menor")
  elif numero < aleatorio:
    print("\tNo es el número correcto, digite uno mayor")
  else:
    print("¡FELICIDADES!. Acabas de adivinar el número.")
    print(f"El número correcto era: {aleatorio}")
    print(f"\nEl número de intentos fue de: {contador}")
    break  # Rompe el ciclo y bucle

else:
  print(f"Haz alcanzado el número máximo de intentos ({max_intentos}). El número correcto era: {aleatorio}")