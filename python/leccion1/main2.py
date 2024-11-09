# Tipos int, float, string y bool
x = 10
print(x)
print(type(x))
"""
x = 20.2
print (x)
print(type(x))

x = "Hello World"
print(x)
print(type(x))
"""
x = True
print(x)
print(type(x))

x = False
print(x)
print(type(x))


# String
miGrupoFavorito = "La Renga, "
caracteristicas = "la mejor banda de Rock Nacional"
print("Mi grupo favorito es: " + miGrupoFavorito + caracteristicas)

miGrupoFavorito = "La Renga,"
caracteristicas = "la mejor banda de Rock Nacional"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)


numero1 = "6"
numero2 = "9"
print(numero1 + numero2)

"""
numero1 = 6
numero2 = 9
print (numero1 + numero2)
"""

numero1 = "6"
numero2 = "9"
print(int(numero1) + int(numero2))


# Bool
miBooleano = 1 > 2
print(miBooleano)

miBooleano = 3 > 2
print(miBooleano)

miBooleano = 1 > 2
if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

    miBooleano = 3 > 2
if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

    # User Input
resultado = input("Digite un número: ")
print(resultado)

num1 = int(input("Digite un número: "))
num2 = int(input("Digite un número: "))
resultado2 = num1 + num2
print(f"El resultado es: {resultado}")
