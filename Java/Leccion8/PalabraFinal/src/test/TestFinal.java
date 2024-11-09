/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde 
se aplique:
          variables: Evita cambiar de valor que almacena la variable
          métodos: Evita que se modifique la definción de un método desde una subclase (hija)
          clases: Evita que se creen clases hijas
Otra caracteristica es que normalmente, cuando trabajamos con variables se combina 
con el modificador de acceso estático para convertir una variable en una constante,
es decir que no se puede modificar su valor,el ejemplo de esto es la clase Math en 
la cual todos sus atributos son del tipo static y final, es por esto que la variable 
pi* se conoce como una constante
*/
package test;

import domain.Persona;


public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39555278;
        System.out.println("miDni = " + miDni);
        // miDni = 20312321; No se puede modificar
        // Persona.CONSTANTE_AQUI = 9; No se puede modificar
        System.out.println("Mi atributo constante es: " +Persona.CONSTANTE_AQUI );
        
        final Persona persona1 = new Persona();
        // persona1 = new Persona(); No se puede asignar una nueva referencia
        persona1.setNombre("Ariel Betancud");
        System.out.println("persona1 = " + persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona1 = " + persona1.getNombre());
        // Podemos modificar el valor del atributo pero no hacer 
        // una nueva referencia usando la palbra reservada final
    }
}