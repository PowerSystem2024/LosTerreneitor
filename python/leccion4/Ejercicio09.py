# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, 
# Se le devolverá la misma frase pero sin espacios en blanco,
# Y además un contador de cuántos caracteres tiene la frase (sin contar los espacios en blanco)
# Ejemplo:        frase = vivir por siempre en paz
#                 frase final = vivirporsiempreenpaz
#                 Nº de caracteres = 20

frase1 = input("Digite la frase que quiere contar: ")
frase2 = ""

for i in frase1:
  if i != " ":
    frase2 += i
frase1 = frase2

print(f"\nFrase final: {frase1}")
print(f"\nNúmero de caracteres: {len(frase1)}")