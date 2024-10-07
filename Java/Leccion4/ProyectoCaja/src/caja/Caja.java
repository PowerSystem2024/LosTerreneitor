package caja;

public class Caja {
    // Atributos
    int ancho;
    int alto;
    int profundo;
    
    // Constructor vacío
    public Caja() {
    }
    
    // Constructor con parámetros
    public Caja(int ancho, int alto, int profundo) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    // Método para calcular el volumen
    public int calcularVolumen() {
        return ancho * alto * profundo;
    }
}
