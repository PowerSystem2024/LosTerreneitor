/*
    Leer un número e indicar si es positivo o negativo, el proceso se repetira 
    hasta que se introduzca un cero.
 */
package Ciclos02;

import java.util.Scanner;


public class Ejercicio02 {
    public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       int numero = 1;
       
       while (numero != 0){
           System.out.println("Digite un número: ");
           numero = Integer.parseInt(scanner.nextLine());
           if(numero < 0){
               System.out.println("El número ingresado es negativo.");
               
           }
           if (numero > 0){
               System.out.println("El número ingresado es positivo");
           }
       } 
        System.out.println("Se ha ingresado cero, programa finalizado");   
    }
}