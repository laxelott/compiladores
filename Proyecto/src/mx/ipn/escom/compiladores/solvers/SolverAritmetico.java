package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverAritmetico extends Solver {
    public SolverAritmetico(Nodo nodo, TablaSimbolos tabla) {
        super(nodo, tabla);
    }

    @Override
    protected Object resolver(Nodo n) throws SolverException {
        // No tiene hijos, es un operando
        if (n.getHijos() == null) {
            if (n.getValue().tipo == TipoToken.CADENA) {
                return n.getValue().lexema;
            } else if (n.getValue().tipo == TipoToken.NUMERO) {
                return Double.valueOf(n.getValue().lexema);
            } else if (n.getValue().tipo == TipoToken.TRUE || n.getValue().tipo == TipoToken.FALSE) {
                Solver solver = new SolverBooleano(n, this.tabla);
                return solver.resolver();
            } else if (n.getValue().tipo == TipoToken.IDENTIFICADOR) {
                // Checar que esté en la tabla de símbolos
                SolverVariable.validateVariable(n, tabla);
                Tuple<TipoToken, Object> res = this.tabla.obtener((String) n.getValue().lexema);

                if (res.x == TipoToken.NUMERO) {
                    return res.y;
                } else if (res.x == TipoToken.CADENA) {
                    return String.valueOf(res.y);
                } else if (res.x == TipoToken.TRUE || res.x == TipoToken.FALSE) {
                    return SolverBooleano.getBool(res.x);
                } else {
                    throw new SolverException("Valor inválido de identificador (" + res.y + ")", n.getValue().linea);
                }
            } else {
                throw new SolverException("Valor inválido", n.getValue().linea);
            }
        } else if (n.getHijos().size() > 2) {
            throw new SolverException("Operador inválido", n.getValue().linea);
        }

        // Por simplicidad se asume que la lista de hijos del nodo tiene dos elementos
        Nodo izq = n.getHijos().get(0);
        Nodo der = n.getHijos().get(1);

        Object resultadoIzquierdo = resolver(izq);
        Object resultadoDerecho = resolver(der);

		// System.out.println("SolverAR");
        // System.out.println(izq + " -> " + resultadoIzquierdo);
        // System.out.println(n.getValue());
        // System.out.println(der + " -> " + resultadoDerecho);
        // System.out.println("--------------");

        // Checar que los resultados sean de la misma instancia
        if (!resultadoIzquierdo.getClass().equals(resultadoDerecho.getClass())) {
            throw new SolverException("Operandos de diferente tipo", n.getValue().linea);
        }

        if (resultadoIzquierdo instanceof Double) {
            switch (n.getValue().tipo) {
                case SUMA:
                    return ((Double) resultadoIzquierdo + (Double) resultadoDerecho);
                case RESTA:
                    return ((Double) resultadoIzquierdo - (Double) resultadoDerecho);
                case MULTIPLICACION:
                    System.out.println("multiplicacion");
                    return ((Double) resultadoIzquierdo * (Double) resultadoDerecho);
                case DIVISION:
                    return ((Double) resultadoIzquierdo / (Double) resultadoDerecho);
                case MAYOR:
                    return ((Double) resultadoIzquierdo > (Double) resultadoDerecho);
                case MAYOR_IGUAL:
                    return ((Double) resultadoIzquierdo >= (Double) resultadoDerecho);
                case MENOR:
                    return ((Double) resultadoIzquierdo < (Double) resultadoDerecho);
                case MENOR_IGUAL:
                    return ((Double) resultadoIzquierdo <= (Double) resultadoDerecho);
                case IGUAL_A:
                    return ((Double) resultadoIzquierdo == (Double) resultadoDerecho);
                default:
                    throw new SolverException("Operador inválido para tipo", n.getValue().linea);
            }
        } else if (resultadoIzquierdo instanceof String) {
            switch (n.getValue().tipo) {
                case SUMA:
                    return ((String) resultadoIzquierdo).concat((String) resultadoDerecho);
                case RESTA:
                    return (((String) resultadoIzquierdo).replaceAll((String) resultadoDerecho, ""));
                case IGUAL_A:
                    return (((String) resultadoIzquierdo).equals((String) resultadoDerecho));
                default:
                    throw new SolverException("Operador inválido para tipo", n.getValue().linea);
            }
        } else if (resultadoIzquierdo instanceof Boolean) {
            switch (n.getValue().tipo) {
                case IGUAL_A:
                    return ((Boolean) resultadoIzquierdo == (Boolean) resultadoDerecho);
                case AND:
                    return ((Boolean) resultadoIzquierdo && (Boolean) resultadoDerecho);
                case OR:
                default:
                    throw new SolverException("Operador inválido para tipo", n.getValue().linea);
            }
        }

        return null;
    }
}
