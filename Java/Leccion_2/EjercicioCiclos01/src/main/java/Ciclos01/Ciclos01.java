/* Ejercicio 1 */

package Ciclos01;

import java.util.Scanner;

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int numero, cuadrado;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(input.nextLine());
        
        while (numero >= 0) {
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número " + numero + " elevado al cuadrado es: " + cuadrado);
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(input.nextLine());
        }
        
        System.out.println("El programa ha finalizado por el ingreso de un número negativo.");
    }
}