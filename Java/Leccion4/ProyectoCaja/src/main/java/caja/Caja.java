/*
Proyecto caja:
Ejercicio 1: Crear un proyecto segun las especificaciones
mostradas a continuacion.
La formula es: voluman = ancho x alto x profundidad
 */
package caja; // package


public class Caja { //Clase pública caja
    // Atributos 
    int ancho;
    int alto;
    int profundo;
    // Métodos y constructores
    public Caja() {  // Constructor1  = vacio  
        
    }
    // Constructor con parametros
    public Caja(int ancho, int alto, int profundo){
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen() {
        return ancho * alto * profundo;
    }

    
}

