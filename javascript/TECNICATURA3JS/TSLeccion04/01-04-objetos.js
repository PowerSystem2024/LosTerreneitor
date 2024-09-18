let x = 10; // Variable de tipo primitivo
console.log(x.length);

// Objeto
let persona = {
  nombre: "Mario",
  apellido: "Meza",
  email: "mario_meza@email.com",
  edad: 38,
  idioma: "es",
  get lang() {
    return this.idioma.toUpperCase();
  },
  set lang(lang) {
    return (this.idioma = lang.toUpperCase());
  },
  nombreCompleto: function () {
    return this.nombre + " " + this.apellido;
  },
  get nombreEdad() {
    return "El nombres es: " + this.nombre + ", Edad:" + this.edad;
  },
};

console.log("Objeto con método");
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona.nombreCompleto());

console.log("Creamos un objeto");
let persona2 = new Object(); // Debe crear un objeto nuevo en memoria
persona2.nombre = "Gerardo";
persona2.apellido = "Calcagni";
persona2.direccion = "Perpetua Llorente 249";
persona2.telefono = "260415678569";

// Distintas formas de imprimir un objeto
// Número 1: La mas sencilla concatenar cada valor de cada propiedad
console.log("Distintas formas de imprimir un objeto: Forma 1");
console.log(persona2.nombre);
console.log(persona2["direccion"]); // Accedemos como si fuera un arreglo

// Número 2: A través de un ciclo for in
console.log("Distintas formas de imprimir un objeto: Forma 2");
for (propiedad in persona2) {
  console.log(propiedad);
  console.log(persona2[propiedad]);
}
// Número 3: La función Object.values()
console.log("Distintas formas de imprimir un objeto: Forma 3");
let persona3 = Object.values(persona);
console.log(persona3);

// Métdo 4: Utilizaremos el método JSON.stringify()
console.log("Distintas formas de imprimir un objeto: Forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);
persona.apellida = "Calcagni"; // Cambiamos de manera dinámica el nombre de un objeto
console.log(persona.apellida);
delete persona.apellida; // eliminamos el error
console.log(persona);

// Métodos get y set Parte 1 y 2
console.log("Comenzamos a utilizar el método get");
console.log(persona.nombreEdad);
console.log("Comenzamos con el método get para idioma");
console.log(persona.lang);
console.log("Comenzamos con el método set");
persona.lang = "en";
console.log(persona.lang);

// Constructores de objetos
function Persona3(nombre = "Luis", apellido, email) {
  this.nombre = nombre;
  this.apellido = apellido;
  this.email = email;
}

let padre = new Persona3("Daniel", "Calcagni", "tutosneotecs@gmail.com");
console.log(padre);

let madre = new Persona3("Lidia", "Meza", "lidia_meza@email.com");
console.log(madre);
