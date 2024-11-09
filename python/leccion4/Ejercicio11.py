# Ejercicio 11: Agenda telefónica
# Hacer un programa que simule una agenda de contactos.
# Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono
# El programa tendrá el siguiente menú de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir

agenda = { }

while True:
  print("\t.:MENÚ:.")
  print("1. Nuevo contacto")
  print("2. Borrar contacto")
  print("3. Ver contactos existentes")
  print("4. Salir")
  opcion = int(input("Digite una opción del menú: "))
  if opcion == 1:
    nombre = input("Digite el nombre del contacto: ")
    telefono = int(input("Digite el número de teléfono: "))
    if nombre not in agenda:
      agenda[nombre] = telefono
      print("¡Contacto agendado exitosamente!")
    else:
      print("Este contacto ya existe.")
  elif opcion == 2:
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
      del (agenda[nombre])
      print("El contacto se ha eliminado correctamente.")
    else:
      print("Contacto inexistente.")
  elif opcion == 3:
    print("Agenda de contactos")
    for clave, valor in agenda.items():
      print(f"Nombre: {clave} | Teléfono: {valor}")
  elif opcion == 4:
    print("Gracias por utilizar su agenda de contactos.")
    break
  else:
    print("Se equivocó de opción de menú. Vuelva a intentarlo.")