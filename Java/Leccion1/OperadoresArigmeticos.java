public class OperadoresArigmeticos {
    public static void main(String[] args) {
        int num1 = 5, num2 = 4;

        var solucion = num1 + num2;
        System.out.println("El resultado es: " + solucion);

        solucion = num1 - num2;
        System.out.println("La resta es: " + solucion);

        solucion = num1 * num2;
        System.out.println("La multiplicacion es: " + solucion);

        solucion = num1 / num2;
        System.out.println("La division es: " + solucion);

        var solucion2 = 3.4 / num2;
        System.out.println("La solucion es: " + solucion2);

        solucion = num1 % num2;
        System.out.println("La respuesta es: " + solucion);

        if (num2 % 2 == 0) {
            System.out.println("El resultado es par!");

        } else {
            System.out.println("El resultado es impar!");
        }
    }

}
