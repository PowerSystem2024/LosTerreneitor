package Operaciones;

import javax.swing.JOptionPane;
public class Aritmetica {
    // Atributos de la clase
    int a;
    int b;

    // El constructor es un método especial
    public Aritmetica (){ //constructor 1 vacio
       System.out.println("Se está ejecutando el constructor número 1");
    }
    
    // Sobrecarga de constructores 
    public Aritmetica (int a, int b){ //constructor 2
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
        this.a = arg1; //El argumento a se asigna al atributo this.a 
        this.b = arg2; 
        return this.sumarConRetorno();
    }

    
    public static void main(String[] args) {
        
        Aritmetica operacion = new Aritmetica(5, 3);
        
        
        operacion.sumarNumeros();
        System.out.println("Resultado con retorno: " + operacion.sumarConRetorno());
        
    
        int sumaArgumentos = operacion.sumarConArgumentos(12, 26);
        System.out.println("Resultado de sumarConArgumentos: " + sumaArgumentos);
    }
}