package Operaciones;

import javax.swing.JOptionPane;

public class Aritmetica {
    // Atributos de la clase
    int a, b;

    // El constructor es un método especial
    public Aritmetica (){ //constructor 1 vacio
       System.out.println("Se está ejecutando el constructor número 1");
    }
    
    // Sobrecarga de constructores 
    public Aritmetica (int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando el constructor número 2");      
    }
    
    // Métodos
    public void sumarNumeros() {
        int resultado = a + b;
        JOptionPane.showMessageDialog(null, resultado);
    }
    
    public int sumarConRetorno() {
        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2) {
        this.a = arg1; 
        this.b = arg2; 
        return this.sumarConRetorno();
    }

    // Main method to run the program
    public static void main(String[] args) {
        // Create an instance using the overloaded constructor
        Aritmetica operacion = new Aritmetica(5, 3);
        
        // Call methods to perform operations
        operacion.sumarNumeros();
        System.out.println("Resultado con retorno: " + operacion.sumarConRetorno());
        
        // Perform sum with arguments
        int sumaArgumentos = operacion.sumarConArgumentos(10, 15);
        System.out.println("Resultado de sumarConArgumentos: " + sumaArgumentos);
    }
}
