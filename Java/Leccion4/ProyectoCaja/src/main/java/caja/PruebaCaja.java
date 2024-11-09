/*
Proyecto caja:
Ejercicio 1: Crear un proyecto segun las especificaciones
mostradas a continuacion.
La formula es: voluman = ancho x alto x profundidad
 */
package caja; // package


public class PruebaCaja {

    public static void main(String[] args) { // Método Main
       // Variable Locales
       int medidaAncho = 3; // valores ingresados en codigo puro
       int medidaAlto = 2;
       int medidaProf =6;
       
       Caja caja1 = new Caja(); // Instanciamos el objeto , constructor vacio
       caja1.ancho = medidaAncho;
       caja1.alto = medidaAlto;
       caja1.profundo = medidaProf;
       int resultado = caja1.calcularVolumen(); // Llamammos al método
       // Primer Resultado
        System.out.println("Resultado volumen caja 1: " + resultado);
        
        Caja caja2 = new Caja(2, 4, 6); // Llamamos al constructor 2 con nuevos argumentos 
        // Llamamos con el nuevo objeto al método para un nuevo cálculo 
        System.out.println("Resultado volumen caja 2: " + caja2.calcularVolumen());
    } 
}

