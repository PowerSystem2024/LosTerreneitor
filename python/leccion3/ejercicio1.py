mes = int(input("Escriba el mes del año que desee saber su estación (1 - 12): "))

estacion = None

if mes == 1 or mes == 2 or mes == 3:
  estacion = "Verano."
elif mes == 4 or mes == 5 or mes == 6:
  estacion = "Otoño."
elif mes == 7 or mes == 8 or mes == 9:
  estacion = "Invierno."
elif mes == 10 or mes == 11 or mes == 12:
  estacion = "Primavera."
else:
  estacion = "El mes ingresado no es el correcto."

print(f"Para el mes {mes} la estación es: {estacion}")