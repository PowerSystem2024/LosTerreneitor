package cuestionarioclase6;

public class CuestionarioClase6 {

    public static void main(String[] args) {
        //Pregunta 1 ¿Cual es el tipo de dato de esta variable?
        var a = 0;
        System.out.println("El tipo de dato de la variable a es: " + typeOf(a));

        //Pregunta 2 ¿Cual es el rango de tipo Short?
        System.out.println("El rango de tipo short es: " + Short.MIN_VALUE + " a " + Short.MAX_VALUE);

        //Pregunta 3 ¿Cuantos bytes tiene una variable de tipo long?
        System.out.println("La variable long tiene : " + Long.BYTES + " bytes.");

        //Pregunta 4 ¿Cuantos bits toma una variable de tipo int?
        System.out.println("La variable int tiene: " + Integer.SIZE + " bits.");

        //Pregunta 5 ¿Cual es el tipo de dato para esta variable?
        var b = 5.3;
        System.out.println("El tipo de dato de " + b + " es: " + typeOf(b));

        //Pregunta 6 ¿Cuantos bits toma una variable de tipo flotante?
        System.out.println("La variable de tipo float tiene: " + Float.SIZE + "bits");

    }

    public static String typeOf(Object obj) {
        return obj.getClass().getName();
    }

    public static String typeOf(int obj) {
        return "Entero";
    }

    public static String typeOf(double obj) {
        return "Double";
    }

    public static String typeOf(float obj) {
        return "Float";
    }

    public static String typeOf(long obj) {
        return "Long";
    }

    public static String typeOf(short obj) {
        return "Short";
    }

    public static String typeOf(byte obj) {
        return "Byte";
    }

    public static String typeOf(boolean obj) {
        return "Boolean";
    }

    public static String typeOf(char obj) {
        return "Char";
    }
}
