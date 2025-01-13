package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverVariable extends Solver {
    public SolverVariable(Nodo nodo) {
        super(nodo);
    }

    @Override
    protected Object resolver(Nodo n) throws SolverException {
        if (Global.DEBUG)
            System.out.println("solVA");
        if (n.getHijos() == null) {
            throw new SolverException("Identificador faltante", n.getValue().linea);
        } else if (n.getHijos().size() > 2) {
            throw new SolverException("Valores de más", n.getValue().linea);
        }

        Boolean isFunction = n.getHijos().get(0).getValue().tipo == TipoToken.FUNCTION;

        if (n.getValue().esTipoDeDato()) {
            // Intentar inicializar variable
            invalidateVariable(n, 0);
            // Agregar hijo 1 como identificador
            if (isFunction) {
                TablaSimbolos.asignarFuncion(n.getHijos().get(0).getValue().lexema, n.getValue().tipo);
            } else {
                TablaSimbolos.asignarVariable(n.getHijos().get(0).getValue().lexema, n.getValue().tipo);
            }
        } else if (n.getValue().tipo == TipoToken.SET) {
            // Checar que variable exista
            validateVariable(n, 1);
        }

        if (isFunction) {
            
        } else if (n.getHijos().size() == 2) {
            // Agregar solución de hijo 2 como valor de identificador
            Solver solver = new SolverAritmetico(n.getHijos().get(0));
            @SuppressWarnings("unchecked")
            Tuple<TipoToken, Object>res = (Tuple<TipoToken, Object>) solver.resolver();

            TablaSimbolos.asignarVariable(n.getHijos().get(1).getValue().lexema, res.x, res.y);

            // Checar compatibilidad de tipo de dato
            if (!Token.sonCompatibles(res.x, (TipoToken) TablaSimbolos.obtenerTipoVariable(n.getHijos().get(1).getValue().lexema))) {
                throw new SolverException("Tipos incompatibles en (" + n.getHijos().get(1).getValue().lexema + ")", n.getValue().linea);
            }
            return res;
        }
        return null;
    }

    public static Boolean checkVariable(Nodo n) {
        return TablaSimbolos.existeIdentificadorVariable(n.getValue().lexema);
    }

    public static Boolean checkVariable(Nodo n, int childNumber) {
        return TablaSimbolos.existeIdentificadorVariable(n.getHijos().get(childNumber).getValue().lexema);
    }

    public static Boolean validateVariable(Nodo n) throws SolverException {
        if (!checkVariable(n)) {
            throw new SolverException("Variable " + n.getValue().lexema + " no inicializada", n.getValue().linea);
        } else {
            return true;
        }
    }

    public static Boolean validateVariable(Nodo n, int childNumber) throws SolverException {
        if (!checkVariable(n, childNumber)) {
            throw new SolverException(
                    "Variable " + n.getHijos().get(childNumber).getValue().lexema + " no inicializada",
                    n.getValue().linea);
        } else {
            return true;
        }
    }

    public static Boolean invalidateVariable(Nodo n) throws SolverException {
        if (checkVariable(n)) {
            throw new SolverException("Variable " + n.getValue().lexema + " ya inicializada", n.getValue().linea);
        } else {
            return true;
        }
    }

    public static Boolean invalidateVariable(Nodo n, int childNumber) throws SolverException {
        if (checkVariable(n, childNumber)) {
            throw new SolverException(
                    "Variable " + n.getHijos().get(childNumber).getValue().lexema + " ya inicializada",
                    n.getValue().linea);
        } else {
            return true;
        }
    }

}