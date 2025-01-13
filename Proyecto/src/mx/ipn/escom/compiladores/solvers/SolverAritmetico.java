package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverAritmetico extends Solver {
    public SolverAritmetico(Nodo nodo) {
        super(nodo);
    }

    @Override
    protected Tuple<TipoToken, Object> resolver(Nodo n) throws SolverException {
        if (Global.DEBUG) {
            System.out.println("solAR");
        }

        TipoToken tipo = null;
        Object value = null;
            
        // No tiene hijos, es un operando
        if (n.getHijos() == null) {
            tipo = n.getValue().tipo;
            if (n.getValue().tipo == TipoToken.STRING || n.getValue().tipo == TipoToken.CHAR) {
                value = n.getValue().lexema;
            } else if (n.getValue().tipo == TipoToken.INT) {
                value = Double.valueOf(n.getValue().lexema);
            } else if (n.getValue().tipo == TipoToken.TRUE || n.getValue().tipo == TipoToken.FALSE) {
                Solver solver = new SolverBooleano(n);
                value = solver.resolver();
            } else if (n.getValue().tipo == TipoToken.IDENTIFICADOR) {
                // Checar que esté en la tabla de símbolos
                SolverVariable.validateVariable(n);
                Object resVal = TablaSimbolos.obtenerVariable(n.getValue().lexema);
                tipo = (TipoToken) TablaSimbolos.obtenerTipoVariable(n.getValue().lexema);

                if (tipo == TipoToken.TRUE || tipo == TipoToken.FALSE) {
                    value = SolverBooleano.getBool(tipo);
                    tipo = TipoToken.INT;
                } else {
                    value = resVal;
                }
            } else {
                throw new SolverException("Valor inválido", n.getValue().linea);
            }

            return new Tuple<TipoToken, Object>(tipo, value);
        } else if (n.getHijos().size() != n.getValue().aridad()) {
            throw new SolverException("Operador inválido (" + n.getHijos().get(0).getValue().lexema + ")",
                    n.getValue().linea);
        }

        // Por simplicidad se asume que la lista de hijos del nodo tiene dos elementos
        Nodo izq = n.getHijos().get(0);
        Nodo der = n.getHijos().get(1);

        Tuple<TipoToken, Object> resultadoIzquierdo = resolver(izq);
        Tuple<TipoToken, Object> resultadoDerecho = resolver(der);
        
        TipoToken lTipo = resultadoIzquierdo.x;
        TipoToken rTipo = resultadoDerecho.x;
        Object lVal = resultadoIzquierdo.y;
        Object rVal = resultadoDerecho.y;

        // Checar que los resultados sean compatibles
        if (!Token.sonCompatibles(lTipo, rTipo)) {
            throw new SolverException("Operandos de diferente tipo", n.getValue().linea);
        }

        if (lTipo == TipoToken.INT || lTipo == TipoToken.FLOAT) {
            switch (n.getValue().tipo) {
                case SUMA:
                    value = ((Double) lVal + (Double) rVal);
                case RESTA:
                    value = ((Double) lVal - (Double) rVal);
                case MULTIPLICACION:
                    value = ((Double) lVal * (Double) rVal);
                case DIVISION:
                    value = ((Double) lVal / (Double) rVal);
                case MAYOR:
                    value = ((Double) lVal > (Double) rVal);
                case MAYOR_IGUAL:
                    value = ((Double) lVal >= (Double) rVal);
                case MENOR:
                    value = ((Double) lVal < (Double) rVal);
                case MENOR_IGUAL:
                    value = ((Double) lVal <= (Double) rVal);
                case IGUAL_A:
                    value = ((Double) lVal == (Double) rVal);
                default:
                    throw new SolverException("Operador inválido para tipo", n.getValue().linea);
            }
        } else if (lTipo == TipoToken.STRING || lTipo == TipoToken.CHAR) {
            switch (n.getValue().tipo) {
                case SUMA:
                    value = (String.valueOf(lVal)).concat(String.valueOf(rVal));
                case RESTA:
                    value = ((String.valueOf(lVal)).replaceAll(String.valueOf(rVal), ""));
                case IGUAL_A:
                    value = ((String.valueOf(lVal)).equals(String.valueOf(rVal)));
                default:
                    throw new SolverException("Operador inválido para tipo", n.getValue().linea);
            }
        } else if (lTipo == TipoToken.TRUE || lTipo == TipoToken.FALSE) {
            switch (n.getValue().tipo) {
                case IGUAL_A:
                    value = ((Boolean) lVal == (Boolean) rVal);
                case AND:
                    value = ((Boolean) lVal && (Boolean) rVal);
                case OR:
                    value = ((Boolean) lVal || (Boolean) rVal);
                default:
                    throw new SolverException("Operador inválido para tipo", n.getValue().linea);
            }
        }

        return new Tuple<TipoToken, Object>(tipo, value);
    }
}
