package Operaciones;

import javax.swing.JOptionPane;

public class Aritmetica {
    // Atributos de la clase
    int a, b;

    // Métodos
    public void sumarNumeros() {
        int resultado = a + b;
        JOptionPane.showMessageDialog(null, resultado);
    }
    
    public int sumarConRetorno() {
        // int resultado = a + b;
        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2) {
        this.a = arg1; // El argumento a se asigna al atributo this.a
        this.b = arg2; // El operador this hace que se diferencien los atributos de los argumentos
        //return a + b;
        return this.sumarConRetorno();
    }
}
