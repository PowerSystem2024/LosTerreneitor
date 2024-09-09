import java.util.Scanner;

public class EjercicioLibro {
    public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            System.out.println("Proporciona el titulo del libro: ");
            String titulo = entrada.nextLine();
            System.out.println("Proporciona el autor: ");
            String autor = entrada.nextLine();
            System.out.println(titulo + "Escrito por " + autor);
        }
    }

}
