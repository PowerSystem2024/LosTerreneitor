/*
Ejercicio 15: Leer 10 enteros ordenados crecientemente. Leer N y buscarlo en la
tabla. Se debe mostrar la posicion en que se encuentra. Si no esta, indicarlo
con un mensaje.
*/

package arreglo_ejercicios_15;

import java.util.Scanner;

public class Arreglo_Ejercicios_15 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        boolean creciente;

        System.out.println("Llenar el arreglo en orden creciente:");

        do {
            creciente = true;
            for (int i = 0; i < 10; i++) {
                System.out.print(i + ". Digite un numero: ");
                arreglo[i] = entrada.nextInt();
            }

            for (int i = 0; i < 9; i++) {
                if (arreglo[i] > arreglo[i + 1]) {
                    creciente = false;
                    System.out.println("\nEl arreglo está desordenado, vuelva a ingresar los numeros.");
                    break;
                }
            }
        } while (!creciente);

        System.out.print("\nDigite un numero para buscar en el arreglo: ");
        int numero = entrada.nextInt();

        int i = 0;
        while (i < 10 && arreglo[i] < numero) {
            i++;
        }

        if (i < 10 && arreglo[i] == numero) {
            System.out.println("\nNumero encontrado en la posicion: " + i);
        } else {
            System.out.println("\nNumero no encontrado");
        }
    }
}