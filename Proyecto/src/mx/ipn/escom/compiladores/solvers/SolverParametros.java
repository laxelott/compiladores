package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverParametros extends Solver {
    public SolverParametros(Nodo nodo) {
        super(nodo);
    }

    @Override
    protected Object resolver(Nodo n) throws SolverException {
        if (Global.DEBUG)
            System.out.println("solPAR");

        for (int i=0; i<n.getHijos().size(); ++i) {
            SolverVariable varSolver = new SolverVariable(n.getHijos().get(i));
            varSolver.resolver(n.getHijos().get(i));
        }

        // Solver solver 

        // Solver solver = new SolverAritmetico(n.getHijos().get(0));
        // Tuple<TipoToken, Object> valor = solver.resolver();

        // System.out.println(valor);
        return null;
    }
}