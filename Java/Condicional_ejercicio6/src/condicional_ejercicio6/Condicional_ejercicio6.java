package condicional_ejercicio6;

import java.util.Scanner;
import java.text.MessageFormat;

public class Condicional_ejercicio6 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] numbers = new int[2];

        for (int i = 0; i < 2; i++) {
            System.out.println("Digite el " + (i + 1) + " número: ");
            numbers[i] = input.nextInt();
        }

        int num1 = numbers[0];
        int num2 = numbers[1];
        double result;

        if (num1 == num2) {
            result = num1 * num2;
        } else if (num1 > num2) {
            result = num1 - num2;
        } else {
            result = num1 + num2;
        }

        System.out.println(MessageFormat.format("El resultado es {0}", result));
    }

}
