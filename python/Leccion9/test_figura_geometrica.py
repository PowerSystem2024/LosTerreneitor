from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("")
print("Creación de objeto clase Cuadrado".center(50, "-"))
print("")

cuadrado1 = Cuadrado(3, "Rojo")
cuadrado1.alto = 5
cuadrado1.ancho = 5
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)

print("")
print("Creación de objeto clase Rectángulo".center(50, "-"))
print("")

rectangulo1 = Rectangulo(7, 4, "Negro")
rectangulo1.ancho = 8
print(f"Cálculo del área del rectángulo: {rectangulo1.calcular_area()}")
print(rectangulo1)

# figura1 = FiguraGeometrica()  # No se puede instanciar, es abstracta

print(Cuadrado.mro())