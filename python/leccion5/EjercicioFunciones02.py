# Ejercicio 2: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos de tipo numérico,
# Utilizando argumentos variables *args como parámetro de la función y regresar como resultado
# La multiplicación de todos los valores pasados como argumento

#Definimos la función para multiplicar
def multiplicar_valores(*args):
  resultado = 1
  for numero in args:
    resultado *= numero
  return resultado

# Llamamos la función
print(multiplicar_valores(2, 8, 9, 5))  # Le pasamos los argumentos