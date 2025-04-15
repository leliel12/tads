package genetics;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class Calculadora_Test {
    private Calculadora calculadora;
    private static final double DELTA = 0.0001;

    @Before
    public void inicializar(){
        calculadora = new Calculadora();
    }

    @Test
    public void probarSuma() {
        assertEquals(8, calculadora.sumar(5, 3), DELTA);
        assertEquals(-2, calculadora.sumar(-5, 3), DELTA);
        assertEquals(0, calculadora.sumar(0, 0), DELTA);
    }

    @Test
    public void probarResta() {
        assertEquals(2, calculadora.restar(5, 3), DELTA);
        assertEquals(-8, calculadora.restar(-5, 3), DELTA);
        assertEquals(0, calculadora.restar(0, 0), DELTA);
    }

    @Test
    public void probarMultiplicacion() {
        assertEquals(15, calculadora.multiplicar(5, 3), DELTA);
        assertEquals(-15, calculadora.multiplicar(-5, 3), DELTA);
        assertEquals(0, calculadora.multiplicar(0, 5), DELTA);
    }
    
    @Test(expected = ArithmeticException.class)
    public void probarDivisionPorCero() {
        calculadora.dividir(6, 0);
    }

    @Test
    public void probarDivision() {
        assertEquals(2, calculadora.dividir(6, 3), DELTA);
        assertEquals(-2, calculadora.dividir(-6, 3), DELTA);
    }

    @Test
    public void probarRaizCuadrada() {
        assertEquals(2, calculadora.raizCuadrada(4), DELTA);
        assertEquals(0, calculadora.raizCuadrada(0), DELTA);
    }

    @Test(expected = IllegalArgumentException.class)
    public void probarRaizCuadradaNegativa() {
        calculadora.raizCuadrada(-4);
    }

    @Test
    public void probarPotencia() {
        assertEquals(8, calculadora.potencia(2,3), DELTA);
    }

    @Test
    public void probarPotenciaCero() {
        assertEquals(1, calculadora.potencia(2,0), DELTA);
    }

    @Test
    public void testFactorial() {
        assertEquals(1, calculadora.factorial(1), DELTA);
        assertEquals(6, calculadora.factorial(3), DELTA);
        assertEquals(120, calculadora.factorial(5), DELTA);
    }

    @Test
    public void testesPrimo() {
        assertTrue(calculadora.esPrimo(2));
        assertTrue(calculadora.esPrimo(3));
        assertTrue(calculadora.esPrimo(5));
        assertFalse(calculadora.esPrimo(1));
        assertFalse(calculadora.esPrimo(0));
        assertFalse(calculadora.esPrimo(-1));
    }
}