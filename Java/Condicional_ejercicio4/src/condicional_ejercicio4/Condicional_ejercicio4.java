package condicional_ejercicio4;

import java.util.Scanner;

public class Condicional_ejercicio4 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        var calificaciones = 3;
        var suma = 0;

        for (var i = 0; i < calificaciones; i++) {
            System.out.println("Digite la " + (i + 1) + "° calificacion: ");
            var nota = Double.parseDouble(entrada.nextLine());
            suma += nota;
        }

        var promedio = suma / 3;
        if (promedio >= 7) {
            System.out.println("La calificacion del alumno es: " + promedio + " está aprobado");
        } else {
            System.out.println("La calificacion del alumno es: " + promedio + " está desaprobado");
        }

    }

}
