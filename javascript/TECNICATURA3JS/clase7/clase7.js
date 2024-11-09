class Person {
  constructor(nombre, apellido) {
    this._nombre = nombre; 
    this._apellido = apellido;
  }

  get nombre() {
    return this._nombre;
  }

  set nombre(nombre) {
    this._nombre = nombre;
  }

  get apellido() {
    return this._apellido; 
  }

  set apellido(apellido) {
    this._apellido = apellido; 
  }

  nombreCompleto() {
  
    return this._nombre + " " + this._apellido; 
  }

  
  toString() {
   
    return this.nombreCompleto();
  }
}

      let personOne = new Person("Carlos", "Rodriguez");
      console.log(personOne.nombre);
      personOne.nombre = "Miguel";
      console.log(personOne.nombre);
      
      let personTwo = new Person("Ana", "García");
      console.log(personTwo.nombre);
      personTwo.nombre = "Laura";
      console.log(personTwo.nombre);


      personOne.apellido = "Fernández"; 
      console.log(personOne.apellido);

      personTwo.apellido = "Martinez"; 
      console.log(personTwo.apellido);

      class Empleado extends Person {
        constructor(nombre, apellido, departamento) {
          super(nombre, apellido);
          this.departamento = departamento;
        }

        get departamento() {
          return this._departamento;
        }

        set departamento(departamento) {
          this._departamento = departamento;
        }

        nombreCompleto() {
          return super.nombreCompleto() + " " + this._departamento;
        }
      }

let empleado1 = new Empleado("Juan Manuel", "Fangio", "Piloto de Carreras");
console.log(empleado1); 
console.log(empleado1.nombre); 
console.log(empleado1.nombreCompleto());

console.log(empleado1.toString());
console.log(personOne.toString());
