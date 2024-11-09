import java.util.Scanner;
        
public class Ejercicio_5 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Ingrese la primera calificación: ");
            int calificacion1 = scanner.nextInt();
            
            System.out.print("Ingrese la segunda calificación: ");
            int calificacion2 = scanner.nextInt();
            
            System.out.print("Ingrese la tercera calificación: ");
            int calificacion3 = scanner.nextInt();
            
            int suma = calificacion1 + calificacion2 + calificacion3;
            
            System.out.println("La suma de las tres calificaciones es: " + suma);
        }
    }
}