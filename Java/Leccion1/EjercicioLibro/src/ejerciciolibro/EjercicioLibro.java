

package ejerciciolibro;
import java.util.Scanner;
public class EjercicioLibro {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Proporcione el título del libro: ");
        String titulo = entrada.nextLine();
        System.out.println("Proporcione el autor: ");
        String autor = entrada.nextLine();
        System.out.println(titulo + " fue escrito por " + autor);
    }
    
}
