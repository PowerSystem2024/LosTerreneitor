package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Homero"; // El valor hexadecimal normalmente empieza con 0x
        persona1.apellido = "Simpson";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Walter";
        persona2.apellido= "Bishop";
        persona2.obtenerInformacion();
    }
}