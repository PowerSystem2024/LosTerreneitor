from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado


teclado1 = Teclado("Logitech", "USB")
monitor1 = Monitor("Samsung", "27 Pulgadas")
raton1 = Raton("SteelSeries", "USB")
computadora1 = Computadora("Asus", monitor1, teclado1, raton1)
print(computadora1)

teclado2 = Teclado("HyperX", "Bluetooth")
monitor2 = Monitor("LG", "24 Pulgadas")
raton2 = Raton("Logitech", "Bluetooth")
computadora2 = Computadora("Asus", monitor2, teclado2, raton2)
print(computadora2)

teclado3 = Teclado("Crossair", "Bluetooth")
monitor3 = Monitor("ViewSonic", "24 Pulgadas")
raton3 = Raton("Genius", "Bluetooth")
computadora3 = Computadora("MSI", monitor3, teclado3, raton3)

teclado4 = Teclado("Red Dragon", "Bluetooth")
monitor4 = Monitor("Asus", "22 Pulgadas")
raton4 = Raton("Razer", "USB")
computadora4 = Computadora("Gigabyte", monitor4, teclado4, raton4)

teclado5 = Teclado("Logitech", "USB")
monitor5 = Monitor("Zowie", "27 Pulgadas")
raton5 = Raton("Logitech", "USB")
computadora5 = Computadora("Asus", monitor5, teclado5, raton5)

computadora6 = Computadora("Asus", monitor2, teclado4, raton5)
computadora7 = Computadora("MSI", monitor1, teclado3, raton4)

computadoras1 = [computadora1, computadora2, computadora5, computadora7]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora6)
print(orden1)

computadoras2 = [computadora3, computadora4, computadora6]
orden2 = Orden(computadoras2)
orden2.agregar_computadora(computadora1)
print(orden2)