# Ejercicio 1: Crear una función para sumar los valores recibidos de tipo numéricos,
# Utilizando argumentos variables *args como parámetro de la función y agregar como resultado
# La suma de todos los valores pasados como argumentos.

def sumar_valor(*args):  # Recibimos una cantidad de parámetros indefinidos
  resultado = 0
  # Iteramos cada elemento
  for valor in args:
    resultado += valor
  return resultado

# Llamamos a la función
print(sumar_valor(7, 2, 8, 3, 5))