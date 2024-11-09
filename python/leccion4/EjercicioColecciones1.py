# Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

# Creamos una lista
lista = [3, 55, 22, 7, "HolaMundo", 3, 22,"somos", 55, "HolaMundo", "Los Terreneitor", 7, "somos"]
lista = list(set(lista)) # La conversión en una sóla línea de código

# El ejercicio un poco más extenso:
#conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set()
#lista = list(conjunto) # Convertimos el conjunto en una lista

print(lista)