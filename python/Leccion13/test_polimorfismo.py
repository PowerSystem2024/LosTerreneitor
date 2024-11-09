from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalle(objeto):
#  print(objeto)  # De manera indirecta llama al str de la clase Empleado o Gerente
  print(type(objeto))  # Esto es para saber el tipo de dato que recibe
  print(objeto.mostrar_detalles())
  if isinstance(objeto, Gerente):
    print(objeto.departamento)

empleado = Empleado("Javier", 3500)
imprimir_detalle(empleado)

gerente = Gerente("Florencia", 5500, "Sistemas")
imprimir_detalle(gerente)