# Ciclo while (mientras - durante)

contador = 0
while contador < 51:
    print("Ejecutamos nuestro ciclo while", contador)
    contador += 1
else:
    print("Fin del ciclo while.")


# Ciclo for

cadena = "HelloWorld"

for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")


# Palabra reservada break

for letra1 in "Alemania":
    if letra1 == "a":
        print(f"letra encontrada: {letra1}")
        break
    else:
        print("Fin del ciclo for")


# Palabra reservada continue

for i in range(6):
    if i % 2 == 0:
        print(f"Valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"Valor: {i}")
