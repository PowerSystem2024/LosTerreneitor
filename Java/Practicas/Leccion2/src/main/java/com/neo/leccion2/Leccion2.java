package com.neo.leccion2;

import java.util.Scanner;

public class Leccion2 {

    public static void main(String[] args) {
        // var condicion = true;
        // if (!condicion) {
        // System.out.println("La condicion es verdadera: " + condicion);
        // } else {
        // System.out.println("La condicion es falsa: " + condicion);
        // }
        /*
         * var numero = 9;
         * var numeroTexto = "Número desconocido";
         * if (numero == 1) {
         * numeroTexto = "Número uno";
         * } else if (numero == 2) {
         * numeroTexto = "Número dos";
         * } else if (numero == 3) {
         * numeroTexto = "Número tres";
         * } else if (numero == 4) {
         * numeroTexto = "Número cuatro";
         * } else {
         * numeroTexto = "Número no encontrado";
         * }
         * System.out.println("numeroTexto = " + numeroTexto);
         */
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero del 1 al 4: ");
        var numero = Integer.parseInt((entrada.nextLine()));
        var numeroTexto = "Valor desconocido";
        switch (numero) {
            case 1:
                numeroTexto = "Numero uno";
                break;
            case 2:
                numeroTexto = "Numero dos";
                break;
            case 3:
                numeroTexto = "Numero tres";
                break;
            case 4:
                numeroTexto = "Numero cuatro";
                break;
            default:
                numeroTexto = "Numero no encontrado";
                break;
        }
        System.out.println("numeroTexto = " + numeroTexto);
    }
}
