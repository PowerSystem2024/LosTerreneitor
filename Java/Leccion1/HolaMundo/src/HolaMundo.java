
public class HolaMundo {
    public static void main(String[] args) {
        /*
         * System.out.println("Hola Mundo desde Java");
         * 
         * int miVariable = 10;
         * System.out.println(miVariable);
         * miVariable = 5;
         * System.out.println(miVariable);
         * // Tipo string
         * String miVariableCadena = "Bienvenidos";
         * System.out.println(miVariableCadena);
         * miVariableCadena = "Sigamos aprendiendo programación";
         * System.out.println(miVariableCadena);
         * 
         * // var - Inferencia de tipos de Java
         * 
         * int miVariableEntera2 = 10;
         * System.out.println("miVariableEntera2 = " + miVariableEntera2);
         * var miVariableCadena2 = "Seguimos estudiando";
         * System.out.println("miVariableCadena2 = " + miVariableCadena2);
         * 
         * //Reglas para definir una variable en Java
         * 
         * var usuario = "Osvaldo";
         * var titulo = "Ingeniero";
         * var union = titulo + " " + usuario;
         * System.out.println("Union = " + union);
         * 
         * var a = 8;
         * var b = 4;
         * System.out.println(usuario + " " + (a+b));
         * 
         * //Ejercicio: caracteres especiales con Java
         * 
         * var nombre = "Natalia";
         * System.out.println("\nNueva linea \n" + nombre); //Diagonal inversa más letra
         * n
         * System.out.println("tabulador: \t" + nombre); //Diagonal inversa más letra t
         * System.out.println("Retroceso: \b\b" + nombre); //Diagonal inversa más letra
         * b
         * System.out.println("Comillas simples: \'" + nombre + "\'"); //Diagonal
         * inversa más comilla simple
         * System.out.println("Comillas dobles: \"" + nombre + "\""); //Diagonal inversa
         * más comilla doble
         * 
         * Scanner entrada = new Scanner(System.in);
         * System.out.println("Digite su nombre: ");
         * var usuario2 = entrada.nextLine();
         * System.out.println("Usuario2 : " + usuario2);
         * System.out.println("Escriba el titulo: ");
         * var titulo2 = entrada.nextLine();
         * System.out.println("Resultado: " + titulo2 + " " + usuario2);
         * 
         * 
         * // Byte
         * byte numEnteroByte = 127;
         * System.out.println("numEnteroByte = " + numEnteroByte);
         * System.out.println("Valor minimo del byte: " + Byte.MIN_VALUE);
         * System.out.println("Valor máximo del byte: " + Byte.MAX_VALUE);
         * 
         * // Short
         * short numEnteroShort = 32767;
         * System.out.println("numEnteroShort = " + numEnteroShort);
         * System.out.println("Valor minimo del short: " + Short.MIN_VALUE);
         * System.out.println("Valor máximo del short: " + Short.MAX_VALUE);
         * 
         * // Int
         * int numEnteroInt = 2147483647;
         * System.out.println("numEnteroInt = " + numEnteroInt);
         * System.out.println("Valor minimo del Int: " + Integer.MIN_VALUE);
         * System.out.println("Valor máximo del Int: " + Integer.MAX_VALUE);
         * 
         * // Long
         * long numEnteroLong = 9223372036854775807L;
         * System.out.println("numEnteroLong = " + numEnteroLong);
         * System.out.println("Valor minimo del Long: " + Long.MIN_VALUE);
         * System.out.println("Valor máximo del Long: " + Long.MAX_VALUE);
         * 
         * // Float
         * float numEnteroFloat = 3.4028235E38F;
         * System.out.println("numEnteroFloat = " + numEnteroFloat);
         * System.out.println("Valor minimo del Float: " + Float.MIN_VALUE);
         * System.out.println("Valor máximo del Float: " + Float.MAX_VALUE);
         * 
         * // Double
         * double numEnteroDouble = 1.7976931348623157E308;
         * System.out.println("numEnteroDouble = " + numEnteroDouble);
         * System.out.println("Valor minimo del Double: " + Double.MIN_VALUE);
         * System.out.println("Valor máximo del Double: " + Double.MAX_VALUE);
         * 
         * 
         * 
         * //inferencia de tipos var y tipos primitivos
         * 
         * var numEntero = 20;
         * System.out.println("Numero entero igual a: " + numEntero);
         * var numFLoat = 33.3F;
         * System.out.println("Numero flotante igual a: " + numFLoat);
         * var numDouble = 33.3;
         * System.out.println("Numero double es igual a: " + numDouble);
         * 
         * 
         * // Tipos primitivos char
         * 
         * char miVariableChar = 'a';
         * System.out.println("Mi variable char = " + miVariableChar); // Indicamos a
         * Java la signación unicode
         * char varCaracter = '\u0024';
         * System.out.println("varCaracter = " + varCaracter); // Valor decimal del
         * juego de caracteres de unicode
         * char varCaracterDecimal = 36;
         * System.out.println("varCaracterDecimal = " + varCaracterDecimal); // Caracter
         * especial simbolo $
         * var caracter1 = '\u0024';
         * System.out.println("caracter1 = " + caracter1);
         * var caracterDecimal = (char) 36;
         * System.out.println("caracterDecimal = " + caracterDecimal); // Conversion con
         * char
         * int varEnteroChar = '$';
         * System.out.println("varEnteroChar = " + varEnteroChar);
         * int caracterChar = '•';
         * System.out.println("caracterChar = " + caracterChar);
         * 
         * 
         * 
         * //Tipos primitivos, tipos booleanos
         * 
         * boolean varBool = true;
         * System.out.println("varBool = " + varBool);
         * if (varBool) {
         * System.out.println("La bandera es verde: " + varBool);
         * } else {
         * System.out.println("La bandera es roja: " + varBool);
         * }
         * 
         * //Algoritmo es mayor de edad?
         * 
         * var edad = 27;
         * var adulto = edad >= 18;
         * if (adulto){
         * System.out.println("Es mayor de edad: " + edad);
         * } else {
         * System.out.println("No es mayor de edad: " + edad);
         * }
         * 
         * 
         * // Conversion de tipos primitivos
         * 
         * var edad = Integer.parseInt("27");
         * System.out.println("Edad: " + (edad+1));
         * var valorPI = Double.parseDouble("3.1416");
         * System.out.println("valorPi = " + valorPI);
         * 
         * // Pedir un valor al usuario
         * 
         * 
         * 
         * Scanner entrada = new Scanner(System.in);
         *  System.out.println("Digite su edad: ");
         *  var edad = Integer.parseInt(entrada.nextLine());
         *  System.out.println("Edad = " + edad);
         * 
         * Conversion de tipos primitivos en Java parte 2
         * 
         * var edadTexto = String.valueOf((10));
         * System.out.println("edadTexto = " + edadTexto);
         * 
         * var fraseChar = "Programadores".charAt(12);
         * System.out.println("fraseChar = " + fraseChar);
         * 
         * System.out.println("Digite un caracter: ");
         * fraseChar = entrada.nextLine().charAt(0);
         * System.out.println("fraseChar = " + fraseChar);
         * 
         */
    }
}
