


from Orden import Orden
from Producto import Producto


producto1 = Producto("Remera", 50)
producto2 = Producto("Bermuda", 75)
producto3 = Producto("Camisa", 120)
producto4 = Producto("Pantalón", 110)
producto5 = Producto("Buzo", 180)
producto6 = Producto("Campera", 260)

productos1 = [producto1, producto2]  # Lista de productos
orden1 = Orden(productos1)  # Primer objeto orden pasando la lista de productos
orden1.agregar_producto(producto6)
orden1.agregar_producto(producto3)
print(orden1)
print(f"Total de la orden 1: US${orden1.calcular_total()}")
productos2 = [producto3, producto4]
orden2 = Orden(productos2)
orden2.agregar_producto(producto5)
orden2.agregar_producto(producto1)
print(orden2)
print(f"Total de la orden 2: US${orden2.calcular_total()}")