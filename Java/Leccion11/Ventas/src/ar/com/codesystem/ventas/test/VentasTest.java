
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Chaqueta", 13200.00);
        Producto producto2 = new Producto("Botines", 17500.00);

        Orden orden1 = new Orden();
        // Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        // Tarea: crear más objetos de tipo producto = 10 mínimo
        Producto producto3 = new Producto("Gorra", 2200.00);
        Producto producto4 = new Producto("Bufanda", 3200.00);
        Producto producto5 = new Producto("Chaleco", 10500.00);
        Producto producto6 = new Producto("Mochila", 8500.00);
        Producto producto7 = new Producto("Reloj", 4500.00);
        Producto producto8 = new Producto("Sandalias", 3300.00);
        Producto producto9 = new Producto("Camisa", 7100.00);
        Producto producto10 = new Producto("Short", 2900.00);
        Producto producto11 = new Producto("Bolso", 5200.00);
        Producto producto12 = new Producto("Sombrero", 2700.00);

        // Crear más objetos de tipo orden = 2 mínimo
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.mostrarOrden();

        Orden orden3 = new Orden();
        orden3.agregarProducto(producto6);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto11);
        orden3.agregarProducto(producto12);
        orden3.mostrarOrden();
    }
}