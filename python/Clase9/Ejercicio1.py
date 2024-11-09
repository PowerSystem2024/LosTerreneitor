print("Programa para determinar si un año es bisiesto o no.")


def anio_bisiesto(num):
    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        print(f"El año {num} es bisiesto.")
    else:
        print(f"El año {num} no es bisiesto.")


opcion = 1

while opcion == 1:
    num = int(input("Ingrese un año: "))
    anio_bisiesto(num)
    opcion = int(
        input(
            "Para probar otro año digite la opción 1, de lo contrario para salir elija otro número: "
        )
    )
