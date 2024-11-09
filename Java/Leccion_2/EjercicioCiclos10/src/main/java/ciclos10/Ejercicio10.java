/*
Ejercicio 10: Pedir 10 números y escribir la suma total
Hacerlo con clase Scanner, y con Joptionpane
*/
package ciclos10;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ejercicio10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero , suma = 0;
        for(int i = 1; i <= 10; i++){
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null, "La suma de todos los números es: " + suma);
    }
}
