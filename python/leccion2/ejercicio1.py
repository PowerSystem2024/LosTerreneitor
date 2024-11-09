#Sacar el área y perímetro de un rectángulo
alto = int(input("Ingrese un número para el alto del rectángulo: "))
ancho = int(input("Ingrese un número para el ancho del rectángulo: "))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es:{perimetro}")


#Número par o impar
num = int(input("Digite un número para saber si es par o impar: "))

if num % 2 == 0:
 print(f"El número ingresado es par.")
else:
  print(f"El número ingresado es impar.")


 #Determinar si es mayor de edad o no
edad = int(input("Ingrese su edad para saber si es mayor o no: "))

if edad >= 18:
  print(f"Eres mayor de edad.")
else:
  print(f"No eres mayor de edad.")


#Valor dentro de un rango
num = int(input("Digite un número para saber si se encuentra entre los valores 0 y 5: "))

if num >= 0 and num <= 5:
  print(f"El valor ingresado se encuentra entre 0 y 5.")
else:
  print(f"El valor ingresado NO se encuentra entre los valores 0 y 5.")

  #También puede ser:
num = int(input("Digite un número para saber si se encuentra entre los valores 0 y 5: "))
numMinimo = 0
numMaximo = 5
dentroRango = num >= numMinimo and num <= numMaximo
if dentroRango:
  print(f"El número {num} está dentro del rango.")
else:
  print(f"El número {num} no está dentro del rango.")


#Un padre puede ir al juego o no
Vacaciones = True
diaLibre = True

if not (Vacaciones or diaLibre):
  print(f"No tiene descando, por ende no puede asistir al juego del hijo.")
else:
  print(f"Puede asistir al juego del hijo.")


#Rango entre las edades 20 y 30 años.
Edad = int(input("Coloque su edad para saber si entá dentro del rango: "))
Veinte = Edad >= 20 and Edad <= 30
Treinta = Edad <= 30 and edad >= 20

if Veinte or Treinta:
  print("Estás dentro del rango de los 20 a 30 años.")
else:
  print("No estás dentro del rango de los 20 a 30 años.")

#También se podría haber hecho ( con el and y sin el or) de esta manera:
Edad = int(input("Coloque su edad para saber si está dentro del rango: "))

if Edad >= 20 and Edad <= 30:
  print("Estás dentro del rango de los 20 a 30 años.")
else:
  print("No estás dentro del rango de los 20 a 30 años.")

Edad = int(input("Coloque su edad para saber si entá dentro del rango: "))

#Otra opción, sin el and y con el or
if (20 <= Edad <= 30) or (30 <= Edad < 20):
  print("Estás dentro del rango de los 20 a 30 años.")
else:
  print("No estás dentro del rango de los 20 a 30 años.")


#El mayor de dos números
num1 = int(input("Digite el valor del primer número: "))
num2 = int(input("Digite el valor del segundo número: "))

if num1 > num2:
  print("El primer número que colocó es el mayor")
elif num2 > num1:
  print("El segundo número que colocó es el mayor.")
else:
  print("Los números que colocó son iguales.")


#Tienda de libros
print("Ingrese los siguentes datos del libro:")
Libro = input("Coloque el nombre del libro: ")
ID = int(input("Coloque el ID del libro: "))
Precio = float(input("Coloque el precio del libro: "))
envioGratuito = input("Indicar si el envío es gratuito o no (SI o NO): ")

if envioGratuito == "SI":
  envioGratuito = True
elif envioGratuito == "NO":
  envioGratuito = False
else:
  print("La respuesta es incorrecta, debe colocar SI o NO.")

print(f'''
Nombre: {Libro}
ID: {ID}
Precio: {Precio}
¿Envio gratuito?: {envioGratuito}
      ''')