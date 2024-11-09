# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir grados Celsius a Fahrenheit y viceversa.
# Investigar las fórmulas

# Función de convertir de Celcius a Fahrenheit
def celsius_a_fahrenheit(celsius):
  return (celsius * 9/5) + 32 # La presedencia de operación: primero la multiplicación y luego la división

# Función de convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = float(input("Digite el valor de grados Celsius que quiere convertir a Fahrenheit:"))
resultado = celsius_a_fahrenheit(celsius)
print(f"{celsius}ºC convertidos a Fahrenheit son: {resultado:.2f}ºF")

fahrenheit = float(input("Digite el valor de grados Fahrenheit que quiere convertir a Celsius: "))
resultado = fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit}ºF convertidos a Celsius son: {resultado:.2f}ºC")