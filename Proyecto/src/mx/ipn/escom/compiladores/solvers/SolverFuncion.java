package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverFuncion extends Solver {
    public SolverFuncion(Nodo nodo) {
        super(nodo);
    }

    @SuppressWarnings("unchecked")
    @Override
    protected Object resolver(Nodo n) throws SolverException {
        if (Global.DEBUG)
            System.out.println("solFUN");
        if (n.getHijos() == null) {
            throw new SolverException("Faltan argumentos", n.getValue().linea);
        }

        Solver solver = new SolverParametros(n.getHijos().get(n.getHijos().size()));
        Tuple<TipoToken, String>[] params = (Tuple<TipoToken, String>[]) solver.resolver();
        
        TablaSimbolos.asignarParametros(n.getValue().lexema, params);
        return null;
    }
}