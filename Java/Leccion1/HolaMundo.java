import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {

        // Nuestro primer programa
        /*
         * 
         * System.out.println("Hola, mundo!");
         * 
         * int miVariable = 10;
         * System.out.println(miVariable);
         * miVariable = 5;
         * System.out.println(miVariable);
         * // Tipo String
         * String miVariableCadena = "Bienvenidos";
         * System.out.println(miVariableCadena);
         * miVariableCadena = "Sigamos creciendo en programacion";
         * System.out.println(miVariableCadena);
         */
        /*
         * // var - inferencia de tipos en java
         * int mivariableEntera2 = 10;
         * System.out.println("Mi variable Entera 2 = " + mivariableEntera2);
         * var miVariableCadena2 = "Sigamos estudiando con ";
         * System.out.println("Mi variable cadena 2 = " + miVariableCadena2);
         */
        // Reglas para definir una variable en java
        /*
         * var usuario = "Arturo";
         * var titulo = "Dostor";
         * var union = titulo + " " + usuario;
         * System.out.println(union);
         * 
         * var a = 8;
         * var b = 4;
         * System.out.println(usuario + (a + b)); //contexto
         */
        /*
         * // Ejercicio Caracteres Especiales con Java
         * var nombre = "Mirta";
         * System.out.println("\n Nueva Linea \n" + nombre); // diagonal inversa + n
         * System.out.println("tabulador: \t" + nombre); // diagonal inversa + t es el
         * tabulador
         * 
         * System.out.println("\t\t.:MENU:.");
         * 
         * System.out.println("Retroceso:\b\b\b\b ");// Retoceso \b
         * System.out.println("Comillas Simples: \'" + nombre + "\'"); // diagonal
         * inversa + comillas simples
         * System.out.println("Comillas Dobles: \"" + nombre + "\" ");
         * 
         * 
         * // Clase Scanner
         * Scanner entrada = new Scanner(System.in);
         * System.out.println("Digite su nombre: ");
         * var usuario2 = entrada.nextLine();
         * System.out.println("La variable Usuario2 es: " + usuario2);
         * System.out.println("Escriba el titulo: ");
         * var titulo2 = entrada.nextLine();
         * System.out.println("El resultado: " + titulo2 + " " + usuario2);
         * 
         * // estamos aprendiendo algo nuevo
         * byte numEnteroByte = 127;
         * System.out.println("numEnteroByte= " + numEnteroByte );
         * System.out.println("Valor Minimo del byte: " + Byte.MIN_VALUE);
         * System.out.println("Valor Maximo del byte: " + Byte.MAX_VALUE);
         * 
         * System.out.println("");
         * 
         * short numeroEnteroShort = 32767;
         * System.out.println("Numero Entero Short: " + numeroEnteroShort);
         * System.out.println("Valor minimo del Short: " + Short.MIN_VALUE);
         * System.out.println("Valor maximo del Short: " + Short.MAX_VALUE);
         * 
         * System.out.println("");
         * 
         * int numEnteroInt = 2147483647;
         * System.out.println("El Numero Entero Int : " + numEnteroInt);
         * System.out.println("Valor maximo del Int: " + Integer.MAX_VALUE);
         * System.out.println("Valor minimo del Int: " + Integer.MIN_VALUE);
         * 
         * System.out.println("");
         * 
         * long numeroEnteroLong = 9223372036854775807L;
         * System.out.println("El Numero Entero Long : " + numeroEnteroLong);
         * System.out.println("Valor maximo del Long: " + Long.MAX_VALUE);
         * System.out.println("Valor minimo del Long: " + Long.MIN_VALUE);
         * 
         * System.out.println("");
         * 
         * float numeroEnteroFloat = 3.4028235E38F;
         * System.out.println("El Numero Entero Float: " + numeroEnteroFloat);
         * System.out.println("Valor maximo del Float: " + Float.MAX_VALUE);
         * System.out.println("Valor minimo del Float: " + Float.MIN_VALUE);
         * 
         * System.out.println("");
         * 
         * double numeroEnteroDouble = 1.7976931348623157E308;
         * System.out.println("El Numero Entero Double:" + numeroEnteroDouble);
         * System.out.println("Valor maximo del Double: " + Double.MAX_VALUE);
         * System.out.println("Valor minimo del Double: " + Double.MIN_VALUE);
         * 
         * 
         * // Inferencia de tipo var
         * var numEnteroVar = 20;
         * System.out.println("Num entero =" + numEnteroVar);
         * var numFloat = 23.23F;
         * System.out.println("Numero entero =" + numFloat);
         * var numDobble = 23.23;
         * System.out.println("El numero entero = " + numDobble);
         * 
         * 
         * // Tipos primitivos char
         * char miVariableChar = '>';
         * System.out.println("Mi Variable Char= " + miVariableChar);
         * char varCaracter = '\u0024'; // Indicamos a Java la asignacion Unicode
         * System.out.println("Var Caracter= " + varCaracter);
         * char varCaracterDecimal = 64;//Valor decimal del juego de caracteres de
         * unicode
         * System.out.println("Var Caracter Decimal= " + varCaracterDecimal);
         * char varCaracterSimbolo = '$';
         * System.out.println("El caracter Simbolo es= " + varCaracterSimbolo);
         * int varEnteroChar = '•';
         * System.out.println("El Entero Char es= " + varEnteroChar);
         * 
         * 
         * //Tipor Primitivos y Tipos Booleanos
         * boolean varBool = true;
         * System.out.println("Var Bool= " + varBool);
         * if (varBool){
         * System.out.println("La  bandera verde es= " + varBool);
         * }else{
         * System.out.println("La bandera Roja es= " + varBool);
         * }
         * 
         * // Algoritmo es Mayor de edad
         * var edad = 92;
         * var adulto = edad >= 18;
         * if (adulto) {
         * System.out.println("Eres mayor de edad.");
         * } else {
         * System.out.println("No eres mayor de edad.");
         * }
         * 
         * 
         * // Conversion de Tipos Primitivos
         * var edad = Integer.parseInt("39");
         * System.out.println("Edad:" + (edad + 1));
         * var valorPi = Double.parseDouble("3.1416");
         * System.out.println("El valor de Pi es= " + valorPi);
         * // Pedir un valor
         * var entrada = new Scanner(System.in);
         * System.out.println("Digite su edad: ");
         * edad = Integer.parseInt(entrada.nextLine());
         * System.out.println("Edad =" + edad);
         * 
         * // Conversion de tipos primitivos Java2
         * var edadTexto = String.valueOf(10);
         * System.out.println("Edad Texto = " + edadTexto);
         * var fraseChar = "Programadores".charAt(7);
         * System.out.println("Mi frase Char= " + fraseChar);
         * 
         * var entrada = new Scanner(System.in);
         * System.out.println("Digite un caracter =");
         * fraseChar = entrada.nextLine().charAt(3);
         * System.out.println("Frase Char= " + fraseChar);
         */
    }
}
