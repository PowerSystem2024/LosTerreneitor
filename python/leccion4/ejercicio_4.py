"""
Sumar números pares dentro de un rango.
Hacer un programa para sumar números pares
dentro de un rango.
EJEMPLO: suma de números pares del 2 al 30
         suma = 240
"""

print("\n|---------------------|")
print("|Suma de números pares|")
print("|---------------------|\n")
num = int(
    input(
        "Ingrese un rango de números para hacer la suma de pares\nEjemplo(10 - 20 - 30, etc): "
    )
)
format_num = num + 1
print()


def sumar_pares(num):
    el = []
    for i in range(1, num):
        if i % 2 == 0:
            el.append(i)
    return sum(el)


print(
    f"La suma de todos los pares de {format_num - 1} resulta en {sumar_pares(format_num)}"
)
