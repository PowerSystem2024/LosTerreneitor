import java.util.Scanner;

public class CalculadoraMateriales {
    public static void main(String[] args) {
        System.out.println("|------------------------------------|");
        System.out.println("|    CALCULADORA DE MATERIALES       |");
        System.out.println("|------------------------------------|");
        System.out.println();
        menu();
    }

    public static void menu() {
        Scanner scanner = new Scanner(System.in);
        int opcion;

        while (true) {
            System.out.println("|-|-------------------------------|");
            System.out.println("| |  Seleccione una opción:       |");
            System.out.println("|-|-------------------------------|");
            System.out.println("|1| Calcular muro de ladrillos    |");
            System.out.println("|2| Calcular viga de hormigón     |");
            System.out.println("|3| Calcular columnas de hormigón |");
            System.out.println("|4| Calcular contrapisos          |");
            System.out.println("|5| Calcular techo                |");
            System.out.println("|6| Calcular pisos                |");
            System.out.println("|7| Calcular pintura              |");
            System.out.println("|8| Calcular iluminación          |");
            System.out.println("|9| Salir                         |");
            System.out.println("|-|-------------------------------|");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    calcularMuros();
                    break;
                case 2:
                    calcularViga();
                    break;
                case 3:
                    calcularColumna();
                    break;
                case 4:
                    calcularContrapisos();
                    break;
                case 5:
                    calcularTecho();
                    break;
                case 6:
                    calcularPisos();
                    break;
                case 7:
                    calcularPintura();
                    break;
                case 8:
                    calcularIluminacion();
                    break;
                case 9:
                    salir();
                    return;
                default:
                    System.out.println("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|");
                    System.out.println("| Opción inválida, vuelva a intentarlo.|");
                    System.out.println("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|");
            }
        }
    }

    public static void calcularMuros() {
        System.out.println("|------------------------------------|");
        System.out.println("|        MURO DE LADRILLO            |");
        System.out.println("|------------------------------------|");
        Scanner scanner = new Scanner(System.in);
        String respuesta = "s";
        
        double superficieMuroTotal = 0;
        int ladrillosTotal = 0;
        double cementoTotal = 0;
        double arenaTotal = 0;
        
        while (respuesta.equalsIgnoreCase("s")) {
            System.out.println("Digite la altura del muro en metros:");
            double alturaMuro = scanner.nextDouble();

            System.out.println("Digite el ancho del muro en metros:");
            double anchoMuro = scanner.nextDouble();

            double superficieMuro = alturaMuro * anchoMuro;

            int espesorMuro;
            do {
                System.out.println("Digite los centímetros de espesor del muro a construir (20cm/30cm):");  
                espesorMuro = scanner.nextInt();
                
                if (espesorMuro != 20 && espesorMuro != 30) {
                    System.out.println("Espesor incorrecto. Por favor, vuelva a ingresar el espesor:");
                }
            } while (espesorMuro != 20 && espesorMuro != 30);

            int ladrillosFinal;
            double cementoFinal, arenaFinal;

            if (espesorMuro == 20) {
                ladrillosFinal = (int) (60 * superficieMuro);
                cementoFinal = 10.9 * superficieMuro;
                arenaFinal = 0.09 * superficieMuro;
            } else {
                ladrillosFinal = (int) (70 * superficieMuro);
                cementoFinal = 15.2 * superficieMuro;
                arenaFinal = 0.115 * superficieMuro;
            }

            System.out
                    .println("|------------------------------------CALCULO DEL MURO-------------------------------------|");
            System.out.printf("| La superficie total del muro es: %.2f m²\n", superficieMuro);
            System.out.println("| Para su construcción necesitará: ");
            System.out.printf("| * Cemento: %.2f kg\n", cementoFinal);
            System.out.printf("| * Ladrillos: %d\n", ladrillosFinal);
            System.out.printf("| * Espesor muro: %d cm\n", espesorMuro);
            System.out.printf("| * Arena: %.3f m³\n", arenaFinal);
            System.out
                    .println("|-----------------------------------------------------------------------------------------|");

            superficieMuroTotal += superficieMuro;
            ladrillosTotal += ladrillosFinal;
            cementoTotal += cementoFinal;
            arenaTotal += arenaFinal;

            do {
                System.out.println("¿Desea calcular otro muro? (s/n): ");
                respuesta = scanner.next().toLowerCase();
                
                if (!respuesta.equals("s") && !respuesta.equals("n")) {
                    System.out.println("Opción inválida. Por favor, vuelva a intentarlo.");
                }
            } while (!respuesta.equals("s") && !respuesta.equals("n"));
        }
        
        System.out.println("|--------------------------------RESUMEN TOTAL DE MUROS----------------------------------|");
        System.out.printf("| La superficie total de todos los muros es: %.2f m²\n", superficieMuroTotal);
        System.out.println("| Total de materiales necesarios: ");
        System.out.printf("| * Cemento: %.2f kg\n", cementoTotal);
        System.out.printf("| * Ladrillos: %d\n", ladrillosTotal);
        System.out.printf("| * Arena: %.3f m³\n", arenaTotal);
        System.out.println("|--------------------------------------------------------------------------------------|");
    }

    public static void calcularViga() {
        System.out.println("|------------------------------------|");
        System.out.println("|        VIGA DE HORMIGÓN            |");
        System.out.println("|------------------------------------|");
        Scanner scanner = new Scanner(System.in);
        double totalCemento = 0, totalArena = 0, totalPiedra = 0, totalHierro = 0;
        String respuesta = "s";

        while (respuesta.equalsIgnoreCase("s")) {
            System.out.println("Ingrese el largo de la viga en metros: ");
            double largo = scanner.nextDouble();

            double cemento = largo * 9;
            double arena = largo * 0.02;
            double piedra = largo * 0.02;
            double hierro = largo * 4;

            System.out.println("Materiales necesarios para una viga de " + largo + " metros:");
            System.out.printf("* Cemento (kg): %.2f\n", cemento);
            System.out.printf("* Arena (m3): %.3f\n", arena);
            System.out.printf("* Piedra (m3): %.3f\n", piedra);
            System.out.printf("* Hierro del 4 (metros): %.2f\n", hierro);

            totalCemento += cemento;
            totalArena += arena;
            totalPiedra += piedra;
            totalHierro += hierro;

            do {
                System.out.println("¿Desea calcular los materiales de otra viga? (s/n): ");
                respuesta = scanner.next().toLowerCase();
                
                if (!respuesta.equals("s") && !respuesta.equals("n")) {
                    System.out.println("Opción inválida. Por favor, vuelva a intentarlo.");
                }
            } while (!respuesta.equals("s") && !respuesta.equals("n"));
        }

        System.out.println(
                "|------------------------------------CALCULO DE LA VIGA-------------------------------------|");
        System.out.printf("| * Cemento (kg): %.2f\n", totalCemento);
        System.out.printf("| * Arena (m3): %.3f\n", totalArena);
        System.out.printf("| * Piedra (m3): %.3f\n", totalPiedra);
        System.out.printf("| * Hierro del 4 (metros): %.2f\n", totalHierro);
        System.out.println(
                "|-------------------------------------------------------------------------------------------|");
    }

    public static void calcularColumna() {
        System.out.println("|------------------------------------|");
        System.out.println("|      COLUMNA DE HORMIGÓN           |");
        System.out.println("|------------------------------------|");
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el largo de la columna en metros: ");
        double largoColumna = scanner.nextDouble();

        System.out.println("Ingrese el ancho de la columna en metros: ");
        double anchoColumna = scanner.nextDouble();

        System.out.println("Ingrese la cantidad de columnas: ");
        double cantidadColumna = scanner.nextDouble();

        double columnaTotal = largoColumna * anchoColumna * cantidadColumna;

        double cemento = 7.5 * columnaTotal;
        double arena = 0.016 * columnaTotal;
        double piedra = 0.016 * columnaTotal;
        double hierro10 = 6 * columnaTotal;
        double hierro4 = 3 * columnaTotal;

        System.out.println(
                "|------------------------------------CALCULO DE LA COLUMNA-------------------------------------|");
        System.out.printf("| Para %.2f columna/s de %.2f metros de largo y %.2f metros de ancho se necesitarán:\n",
                cantidadColumna, largoColumna, anchoColumna);
        System.out.printf("| * Cemento: %.2f kg\n", cemento);
        System.out.printf("| * Arena: %.3f m³\n", arena);
        System.out.printf("| * Piedra: %.3f m³\n", piedra);
        System.out.printf("| * Hierro del 10: %.2f m\n", hierro10);
        System.out.printf("| * Hierro del 4: %.2f m\n", hierro4);
        System.out.println(
                "|-----------------------------------------------------------------------------------------------|");
    }

    public static void calcularContrapisos() {
        System.out.println("|------------------------------------|");
        System.out.println("|         CONTRAPISOS                |");
        System.out.println("|------------------------------------|");
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el espesor del contrapiso en centímetros:");
        double espesor = scanner.nextDouble() * 0.01;

        System.out.println("Ingrese el ancho del contrapiso en metros:");
        double ancho = scanner.nextDouble();

        System.out.println("Ingrese el largo del contrapiso en metros:");
        double largo = scanner.nextDouble();

        double volumenCemento = espesor * ancho * largo * 105;
        double volumenArena = espesor * ancho * largo * 0.45;
        double volumenPiedra = espesor * ancho * largo * 0.9;

        System.out.println(
                "|------------------------------------CALCULO DE CONTRAPISO-------------------------------------|");
        System.out.printf(
                "| Para un contrapiso de %.2f metros de espesor, %.2f metros de ancho y %.2f metros de largo se necesitan:\n",
                espesor, ancho, largo);
        System.out.printf("| * Cemento: %.2f kg\n", volumenCemento);
        System.out.printf("| * Arena: %.3f m³\n", volumenArena);
        System.out.printf("| * Piedra: %.3f m³\n", volumenPiedra);
        System.out.println(
                "|----------------------------------------------------------------------------------------------|");
    }

    public static void calcularTecho() {
        System.out.println("|------------------------------------|");
        System.out.println("|            TECHO                   |");
        System.out.println("|------------------------------------|");
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el espesor del techo en metros: ");
        double espesor = scanner.nextDouble();

        System.out.println("Ingrese el ancho del techo en metros: ");
        double ancho = scanner.nextDouble();

        System.out.println("Ingrese el largo del techo en metros: ");
        double largo = scanner.nextDouble();

        double areaTecho = largo * ancho;

        double cantidadCemento = 33 * areaTecho;
        double cantidadArena = 0.072 * areaTecho;
        double cantidadPiedra = 0.072 * areaTecho;
        double cantidadHierro8 = 7 * areaTecho;
        double cantidadHierro6 = 4 * areaTecho;

        System.out.println(
                "|------------------------------------CALCULO DEL TECHO-------------------------------------|");
        System.out.printf("| Para construir el techo necesitarás:\n");
        System.out.printf("| * Cemento: %.2f kg\n", cantidadCemento);
        System.out.printf("| * Arena: %.3f m³\n", cantidadArena);
        System.out.printf("| * Piedra: %.3f m³\n", cantidadPiedra);
        System.out.printf("| * Hierro del 8: %.2f m\n", cantidadHierro8);
        System.out.printf("| * Hierro del 6: %.2f m\n", cantidadHierro6);
        System.out.println(
                "|------------------------------------------------------------------------------------------|");
    }

    public static void calcularPisos() {
        System.out.println("|------------------------------------|");
        System.out.println("|            PISOS                   |");
        System.out.println("|------------------------------------|");
        Scanner scanner = new Scanner(System.in);

        // Establecemos el espesor predeterminado de 0.1 metros (10 cm)
        double espesor = 0.1;

        System.out.println("Ingrese el ancho del piso en metros: ");
        double ancho = scanner.nextDouble();

        System.out.println("Ingrese el largo del piso en metros: ");
        double largo = scanner.nextDouble();

        double areaPiso = largo * ancho;

        double cantidadCemento = 33 * areaPiso;
        double cantidadArena = 0.09 * areaPiso;
        double cantidadPiedra = 0.072 * areaPiso;

        System.out
                .println("|------------------------------------CALCULO DEL PISO-------------------------------------|");
        System.out.printf("| Para construir el piso de %.2f cm de espesor necesitarás:\n", espesor * 100);
        System.out.printf("| * Cemento: %.2f kg\n", cantidadCemento);
        System.out.printf("| * Arena: %.3f m³\n", cantidadArena);
        System.out.printf("| * Piedra: %.3f m³\n", cantidadPiedra);
        System.out
                .println("|-----------------------------------------------------------------------------------------|");
    }

    public static void calcularPintura() {
        System.out.println("|------------------------------------|");
        System.out.println("|           PINTURA                  |");
        System.out.println("|------------------------------------|");
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese la altura de la pared en metros: ");
        double alturaPared = scanner.nextDouble();

        System.out.println("Ingrese el largo de la pared en metros: ");
        double largoPared = scanner.nextDouble();

        double areaPared = alturaPared * largoPared;
        double litrosPintura = areaPared * 0.1;

        System.out
                .println("|------------------------------------CALCULO DE PINTURA-----------------------------------|");
        System.out.printf("| Para pintar una pared de %.2f m² necesitarás:\n", areaPared);
        System.out.printf("| * Pintura: %.2f litros\n", litrosPintura);
        System.out
                .println("|-----------------------------------------------------------------------------------------|");
    }

    public static void calcularIluminacion() {
        System.out.println("|------------------------------------|");
        System.out.println("|         ILUMINACIÓN                |");
        System.out.println("|------------------------------------|");
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el ancho del área en metros: ");
        double ancho = scanner.nextDouble();

        System.out.println("Ingrese el largo del área en metros: ");
        double largo = scanner.nextDouble();

        double area = ancho * largo;
        double iluminacion = area * 100;

        System.out.println(
                "|----------------------------------CALCULO DE ILUMINACION----------------------------------|");
        System.out.printf("| Para iluminar un área de %.2f m² necesitas:\n", area);
        System.out.printf("| * Iluminación: %.2f lúmenes\n", iluminacion);
        System.out
                .println("|-----------------------------------------------------------------------------------------|");
    }

    public static void salir() {
        System.out.println("|====================|");
        System.out.println("| PROGRAMA TERMINADO.|");
        System.out.println("|====================|");
        System.out.println("          /\\_/\\  ");
        System.out.println("         ( o.o ) ");
        System.out.println("          > ^ <  ");
    }
}
