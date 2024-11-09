# Ejercicio 3: Función recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el número 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan números negativos, no imprime nada.

def imprimir_numeros_recursivos(numero):
  if numero >= 1:  # Caso base
    print(numero)
    imprimir_numeros_recursivos(numero -1)  # Caso recursivo
  elif numero == 0:
    return  # Finaliza la ejecución en 0.
  elif numero < 0:
    print("Valor ingresado incorrecto.")

imprimir_numeros_recursivos(int(input("Ingrese un número positivo: ")))