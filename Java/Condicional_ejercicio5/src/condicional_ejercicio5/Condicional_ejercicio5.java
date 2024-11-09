package condicional_ejercicio5;

import java.util.Scanner;
import java.text.MessageFormat;

public class Condicional_ejercicio5 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite el monto de la compra: ");
        var compra = input.nextInt();
        double descuento;

        if (compra > 100) {
            descuento = compra * 0.2;
        } else {
            descuento = 0;
        }
        var precioFinal = compra - descuento;
        System.out.println(MessageFormat.format("El precio a pagar es: {0}", precioFinal));
    }

}
