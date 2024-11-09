from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
  def __init__(self, lado, color):
    # super.__init__(lado)  # En la herencia múltiple no se utiliza el super(), porque se puede generar una confusión
    FiguraGeometrica.__init__(self, lado, lado)
    Color.__init__(self, color)
  
  def calcular_area(self):
    return self.alto * self.ancho
  
  def __str__(self):
    return f"{FiguraGeometrica.__str__(self)} {Color.__str__(self)}"