public class CuestionarioClase6 {
    public static void main(String[] args) {
        // Pregunta N° 1: ¿Cual es el tipo de dato de esta variable?
        var a = 0;
        System.out.println("El tipo de dato de la variable es: " + typeOf(a));
        // Pregunta N° 2: ¿Cual es el rango de tipo short?
        System.out.println("El rango del short es: " + Short.MIN_VALUE + " a " + Short.MAX_VALUE);
        //Pregunta N°3: ¿Cuantos bytes tiene una variable de tipo long?
        System.out.println("La variable long tiene: " + Long.BYTES + " bytes.");
        //Pregunta N°4: ¿Cuantos bytes toma una variable de tipo int?
        System.out.println("La variable int tiene: " + Integer.SIZE + " bytes.");
        //Pregunta N°5 ¿Cual es el tipo de dato para esta variable?
        var b = 5.3;
        System.out.println("El tipo de datos de " + b + " es " + typeOf(b));
        //Pregunta N° 6: ¿Cuantos bytes toma una variable de tipo flotante?
        System.out.println("La variable tipo float tiene: " + Float.SIZE + " bytes.");
    }

    public static String typeOf(Object obj) {
        return obj.getClass().getName();
    }

    public static String typeOf(int obj) {
        return "int";
    }

    public static String typeOf(double obj) {
        return "double";
    }

    public static String typeOf(long obj) {
        return "long";
    }

    public static String typeOf(float obj) {
        return "float";
    }

    public static String typeOf(char obj) {
        return "char";
    }

    public static String typeOf(short obj){
        return "short";
    }

    public static String typeOf(byte obj){
        return "byte";

    }
    public static String typeOf(boolean obj){
        return "boolean";
    }
}
