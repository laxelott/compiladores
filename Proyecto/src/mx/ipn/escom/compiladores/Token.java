package mx.ipn.escom.compiladores;

public class Token {

    public final TipoToken tipo;
    public final String lexema;
    public final Object literal;
    public final int linea;

    public Token(TipoToken tipo, String lexema, int linea) {
        this.tipo = tipo;
        this.lexema = lexema;
        this.literal = null;
        this.linea = linea;
    }
    
    public Token(TipoToken tipo, String lexema, Object literal, int linea) {
        this.tipo = tipo;
        this.lexema = lexema;
        this.literal = literal;
        this.linea = linea;
    }

    @Override
    public String toString() {
        return tipo + " " + lexema + " " + (literal == null ? " " : literal.toString());
    }

    // Métodos auxiliares
    public boolean esOperando() {
        switch (this.tipo) {
            case CADENA:
            case IDENTIFICADOR:
            case NUMERO:
            case TRUE:
            case FALSE:
                return true;
            default:
                return false;
        }
    }

    public boolean esOperador() {
        switch (this.tipo) {
            case SUMA:
            case RESTA:
            case MULTIPLICACION:
            case DIVISION:
            case IGUAL:
            case IGUAL_A:
            case MAYOR:
            case MAYOR_IGUAL:
            case MENOR:
            case MENOR_IGUAL:
            case AND:
            case OR:
                return true;
            default:
                return false;
        }
    }

    public boolean esPalabraReservada() {
        switch (this.tipo) {
            case VAR:
            case SET:
            case IF:
            case PRINT:
            case TRUE:
            case FALSE:
            case ELSE:
                return true;
            default:
                return false;
        }
    }

    public boolean esEstructuraDeControl() {
        switch (this.tipo) {
            case IF:
            case ELSE:
                return true;
            default:
                return false;
        }
    }

    public boolean precedenciaMayorIgual(Token t) {
        return this.obtenerPrecedencia() >= t.obtenerPrecedencia();
    }

    private int obtenerPrecedencia() {
        switch (this.tipo) {
            case MAYOR:
            case MAYOR_IGUAL:
            case MENOR:
            case MENOR_IGUAL:
            case IGUAL_A:
                return 5;
            case MULTIPLICACION:
            case DIVISION:
            case AND:
                return 3;
            case SUMA:
            case RESTA:
            case OR:
                return 2;
            case IGUAL:
                return 1;
            default:
                return 0;
        }
    }

    public int aridad() {
        switch (this.tipo) {
            case MULTIPLICACION:
            case DIVISION:
            case SUMA:
            case RESTA:
            case IGUAL:
            case IGUAL_A:
            case MAYOR:
            case MAYOR_IGUAL:
            case MENOR:
            case MENOR_IGUAL:
            case AND:
            case OR:
                return 2;
            default:
                return 0;
        }
    }
}
