public class OperadoresUnarios {
    public static void main(String[] args) {
        // Operadores Unarios Cambio de signos
        var varA = 7;
        var varB = -varA;
        System.out.println("VarA es igual: " + varA);
        System.out.println("VarB es igual: " + varB);
        // Operador de negacion
        var varC = true;
        var varD = !varC;
        System.out.println("VarC es igual: " + varC);
        System.out.println("VarD es igual: " + varD);
        // Operadores Unarios de incremento: preincremento
        var varE = 1; // Se va a modificar su valor.
        var varF = ++varE;
        System.out.println("La VarE es: " + varE);
        System.out.println("La VarF es igual: " + varF);
        // Postincremento
        var varG = 3;
        var varH = varG++; // Primero el valor de la variable y luego el incremento
        System.out.println("La VarG es igual: " + varG);
        System.out.println("La VarH es igual: " + varH);
        // Operadores Unarios de Decremento: predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("VarI es igual: " + varI);
        System.out.println("VarJ es igual: " + varJ);
        // Postdecremento
        var varK = 8; // Solamente es modificado esta variable.
        var varL = varK--;
        System.out.println("VarK es igual: " + varK);
        System.out.println("VarL es igual: " + varL);
        // Operadores de igualadad y relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum es igual: " + cNum);
        var dNum = aNum != bNum;
        System.out.println("dNum es igual: " + dNum);
        // Comparador de objetos str
        var cadenaA = "Hello";
        var cadenaB = "Beaches";
        var cadenaC = cadenaA.equals(cadenaB);
        System.out.println("CadenaC es igual: " + cadenaC);
        var gvar = aNum >= bNum;
        System.out.println("Gvar es igual: " + gvar);

        if (aNum % 2 == 0) {
            System.out.println("El numero es par");
        } else {
            System.out.println("El numero es impar");
        }
        var edad = 12;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("Es mayor de edad.");
        } else {
            System.out.println("Es menor de edad.");
        }
        // Operadores condicionales
        var valorA = 7;
        var valorMin = 0;
        var valorMax = 10;
        var respuesta = valorA >= valorMin && valorA <= valorMax;
        if (respuesta == true) {
            System.out.println("Esta dentro del rango establecido!");

        } else {
            System.out.println("Esta fuera del rango establecido!");
        }
        var vaciones = false;
        var diaLibre = true;
        if (diaLibre || vaciones) {
            System.out.println("Papa puede asistir al juego de su hijo");

        } else {
            System.out.println("Papa no puede asistir al juego de su hijo");
        }
        // Operador Ternario
        var resultadoT = (5 > 6) ? "Verdadero" : "Falso";
        System.out.println("El ResultadoT es igual: " + resultadoT);

        var numT = 4;
        var resultadoD = (numT % 2 == 0) ? "Es par" : "No es par";
        System.out.println("El resultadoD es: " + resultadoD);

        // Prioridad de los operadores
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("Var x es igual: " + x);
        System.out.println("Var y es igual: " + y);
        System.out.println("Var z es igual: " + z);

        var solucionArigmetica = 4 + 5 * 6 / 3; // Expresion matematica: 4 + ((5*6)/3)= 14
        System.out.println("La respuesta es: " + solucionArigmetica);
        solucionArigmetica = (4 + 5) * 6 / 3; // 4 + 5 = 9 * 6  = 54 /3 =18
        System.out.println("La respuesta es: " + solucionArigmetica);
        
    }

}
