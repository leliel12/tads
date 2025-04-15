package genetics;

public class Calculadora {
    public int sumar(int a, int b) {
        return a + b;
    }

    public int restar(int a, int b) {
        return a - b;
    }

    public int multiplicar(int a, int b) {
        return a * b;
    }

    public int dividir(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("No es posible dividir por cero.");
        }
        return a / b;
    }

    public double raizCuadrada(int a) {
        if (a < 0) {
            throw new IllegalArgumentException("No es posible calcular la raíz cuadrada de un número negativo.");
        }
        return Math.sqrt(a);
    }

    public double potencia(int a, int b){
        if(b == 0){
            return 1;
        }
        int resultado = 1;
        for (int i = 0; i < b; i++) {
            resultado *= a;
        }
        return resultado;
    }

    public double porcentaje(int a, int b){
        if (b < 0) {
            throw new IllegalArgumentException("No es posible calcular un porcentaje negativo.");
        }
        return (a * b) / 100.0;
    }

    public static int factorial(int n) {
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    public static boolean esPrimo(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}