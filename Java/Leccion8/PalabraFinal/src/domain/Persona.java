

package domain;


public class Persona {
    public final static int CONSTANTE_AQUI = 15; // Constante en mayúscula
    private String nombre;

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    
    
    public void imprimir(){
        System.out.println("this = " + this);
    }
}