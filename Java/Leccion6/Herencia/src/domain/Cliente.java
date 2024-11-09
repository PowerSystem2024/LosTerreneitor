
package domain;

import java.util.Date;

public class Cliente extends Persona{
    private Date fechaRegistro;
    private double idCliente;
    private boolean vip;
    private static int contadorClientes; 
    
    // Constructor

    public Cliente(String nombre, char genero, int edad, String direccion, boolean vip) {
        super(nombre, genero, edad, direccion);
        this.vip = vip;
        this.idCliente = ++Cliente.contadorClientes;
        this.fechaRegistro = new Date();
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public double getIdCliente() {
        return this.idCliente;
    }

    public boolean isVip() {
        return this.vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{");
        sb.append("fechaRegistro=").append(fechaRegistro);
        sb.append(", idCliente=").append(idCliente);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
   
}