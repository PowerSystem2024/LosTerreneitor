/*
    Leer un número e indicar si es positivo o negativo, el proceso se repetirá 
    hasta que se introduzca un cero.
    hacer ejercicio con clase scanner, luego joptionpane
 */

package Ciclos02;
import javax.swing.JOptionPane;

public class Ciclos02 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número:"));
        while (numero != 0) {
            if (numero < 0) {
                JOptionPane.showMessageDialog(null, "El número ingresado es negativo.");
            } else if (numero > 0) {
                JOptionPane.showMessageDialog(null, "El número ingresado es positivo.");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número:"));
        }
      
       JOptionPane.showMessageDialog(null, "Se ha ingresado cero, programa finalizado");
    }
}