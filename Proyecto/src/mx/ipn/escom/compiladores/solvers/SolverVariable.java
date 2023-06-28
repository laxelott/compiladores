package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverVariable extends Solver {
    public SolverVariable(Nodo nodo, TablaSimbolos tabla) {
        super(nodo, tabla);
    }

    public static Boolean checkVariable(Nodo n, TablaSimbolos tabla) {
        return tabla.existeIdentificador(n.getValue().lexema);
    }

    public static Boolean checkVariable(Nodo n, int childNumber, TablaSimbolos tabla) {
        return tabla.existeIdentificador(n.getHijos().get(childNumber).getValue().lexema);
    }

    public static Boolean validateVariable(Nodo n, TablaSimbolos tabla) throws SolverException {
        if(!checkVariable(n, tabla)) {
            throw new SolverException("Variable " + n.getValue().lexema + " no inicializada", n.getValue().linea);
        } else {
            return true;
        }
    }

    public static Boolean validateVariable(Nodo n, int childNumber, TablaSimbolos tabla) throws SolverException {
        if(!checkVariable(n, childNumber, tabla)) {
            throw new SolverException("Variable " + n.getHijos().get(childNumber).getValue().lexema + " no inicializada", n.getValue().linea);
        } else {
            return true;
        }
    }

    public static Boolean invalidateVariable(Nodo n, TablaSimbolos tabla) throws SolverException {
        if(checkVariable(n, 0, tabla)) {
            throw new SolverException("Variable " + n.getValue().lexema + " ya inicializada", n.getValue().linea);
        } else {
            return true;
        }
    }

    public static Boolean invalidateVariable(Nodo n, int childNumber, TablaSimbolos tabla) throws SolverException {
        if(checkVariable(n, childNumber, tabla)) {
            throw new SolverException("Variable " + n.getHijos().get(childNumber).getValue().lexema + " ya inicializada", n.getValue().linea);
        } else {
            return true;
        }
    }
    

    @Override
    protected Object resolver(Nodo n) throws SolverException {
		// System.out.println("SolverVAR");
        if (n.getHijos() == null) {
            throw new SolverException("Identificador faltante", n.getValue().linea);
        } else if (n.getHijos().size() > 2) {
            throw new SolverException("Valores de más", n.getValue().linea);
        }

        if (n.getValue().tipo == TipoToken.VAR) {
            // Intentar inicializar variable
            invalidateVariable(n, 0, tabla);
            // Agregar hijo 1 como identificador
            this.tabla.asignar(n.getHijos().get(0).getValue().lexema);
            return null;
        } else if (n.getValue().tipo == TipoToken.SET)  {
            // Checar que variable exista
            validateVariable(n, 0, tabla);
        }

        if (n.getHijos().size() == 2) {
            // Agregar solución de hijo 2 como valor de identificador
            Solver solver = new SolverAritmetico(n.getHijos().get(1), this.tabla);
            Object res = solver.resolver();
            TipoToken tipo = null;

            if (res instanceof Double) {
                tipo = TipoToken.NUMERO;
            } else if (res instanceof String) {
                tipo = TipoToken.CADENA;
            } else if (res instanceof Boolean) {
                tipo = (Boolean) res ? TipoToken.TRUE : TipoToken.FALSE;
            } else {
                throw new SolverException("Valor de asignación inválido (" + res +")", n.getValue().linea);
            }

            this.tabla.asignar(n.getHijos().get(0).getValue().lexema, tipo, res);
            return res;
        }
        return null;
    }
}