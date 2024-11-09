# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menú de opciones:
#                 1. Ingresar el dineron en la cuenta
#                 2. Retirar dinero de la cuenta
#                 3. Mostrar dinero disponible
#                 4. Salir

saldo = 1000

while True:
  print("\t.:MENÚ:.")
  print("1. Ingresar el dinero en la cuenta")
  print("2. Retirar dinero de la cuenta")
  print("3. Mostrar dinero disponible")
  print("4. Salir")
  opcion = int(input("Digite una opción del menú: "))
  print()
  
  if opcion == 1:
    print(f"Su saldo actual es de: u$s{saldo}")
    extra = float(input("Ingrese el monto que desea depositar: "))
    saldo += extra
    print(f"Su saldo actual es de: u$s{saldo}")
  elif opcion == 2:
    print(f"Su saldo actual es de: u$s{saldo}")
    retirar = float(input("Ingrese el monto que desea retirar: "))
    if retirar > saldo:
      print("Dinero insuficiente")
    else:
      saldo -= retirar
      print(f"Su saldo actual es de: u$s{saldo}")
  elif opcion == 3:
    print(f"Su saldo actual es de: u$s{saldo}")
  elif opcion == 4:
    print("Gracias por utilizar nuestros cajeros automáticos. Vuelva pronto.")
    break
  else:
    print("Error, se equivocó de opción de menú. Vuelva a intentarlo.")
    print()