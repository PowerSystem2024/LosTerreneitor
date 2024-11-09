class Persona {
    static contadorPersonas = 0;

    static get MAX_OBJ() {
        return 4;
    }

    constructor(nombre,apellido,edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        if(Persona.contadorPersonas < Persona.MAX_OBJ) {
            Persona.contadorPersonas++;
            this.idPersona = Persona.contadorPersonas;
        } else {
            console.log("Se supero el maximo de objetos")
        }
    }

    get nombre() {
        return this._nombre
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }

    get apellido() {
        return this._apellido
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }

    nombreCompleto() {
        return this.idPersona + " " + this.nombre + " " + this.apellido
    }
    toString() {
        return this.nombreCompleto();
    }

    static saludar() {
        console.log("saludo desde el metodo static")
    }
    static saludar2(persona) {
        console.log("HOLA " + persona.nombre + " " + persona.apellido);
    }
}

class Empleado extends Persona {
    constructor(nombre,apellido,edad,departamento) {
        super(nombre,apellido,edad);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }

    nombreCompleto() {
        return super.nombreCompleto() + ", " + this._departamento
    }
}

let persona1 = new Persona("Roberto", "Gomez", 24);
let persona2 = new Persona("Maria", "Lopez", 40);

persona1.apellido = "Martinez"
console.log(persona1.apellido);

let empleado1 = new Empleado("Juan Manuel","Fangio", 35,"Piloto de Carreras");
console.log(empleado1.nombreCompleto())

console.log(persona1.toString())
console.log(persona2.toString())
console.log(empleado1.toString())

Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);

let persona3 = new Persona("Roberto", "Gomez", 24);
let persona4 = new Persona("Maria", "Lopez", 40);