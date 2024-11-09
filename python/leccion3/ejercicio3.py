calificacion = float(input("Digite su calificación (1 - 10): "))

if calificacion >= 9 and calificacion <= 10:
  print("A")
elif calificacion <= 8.99 and calificacion >=8:
  print("B")
elif calificacion <= 7.99 and calificacion >=7:
  print("C")
elif calificacion <= 6.99 and calificacion >=6:
  print("D")
elif calificacion <=5.99 and calificacion >= 0:
  print("F")
else:
  print("El valor ingresado es incorrecto.")