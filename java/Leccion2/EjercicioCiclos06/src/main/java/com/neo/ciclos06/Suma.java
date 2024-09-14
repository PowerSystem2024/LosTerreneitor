package com.neo.ciclos06;

public class Suma {
    private int suma = 0;

    public void agregarNumero(int num) {
        this.suma += num;
    }

    public int obtenerResultado() {
        return this.suma;
    }
}
