public class OperadoresdeAsignacion {
    public static void main(String[] args) {
        int varnum1 = 1, varnum2 = 4;
        int varnum3 = varnum1 + 6 - varnum2;
        System.out.println("Varnum3 es igual: " + varnum3);
        varnum1 += 1;
        System.out.println("Varnum1 es igual: " + varnum1);
        varnum2 -= 2;
        System.out.println("Varnum2 es igual: " + varnum2);
        varnum1 *= 5;
        System.out.println("Varnum1 es igual: " + varnum1);
        varnum3 /= 4;
        System.out.println("Varnum3 es igual: " + varnum3);
        varnum1 %= 6;
        System.out.println("Varnum1 es igual: " + varnum1);
    }

}
