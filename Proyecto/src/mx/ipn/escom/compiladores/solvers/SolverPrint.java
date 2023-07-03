package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverPrint extends Solver {
    public SolverPrint(Nodo nodo) {
        super(nodo);
    }

    @Override
    protected Object resolver(Nodo n) throws SolverException {
        if (Global.DEBUG)
            System.out.println("solPR");
        if (n.getHijos() == null) {
            throw new SolverException("Faltan argumentos", n.getValue().linea);
        }
        if (n.getHijos().size() > 1) {
            throw new SolverException("Valores de print de más (" + n.getHijos().size() + ")", n.getValue().linea);
        }

        Solver solver = new SolverAritmetico(n.getHijos().get(0));
        Object valor = solver.resolver();

        System.out.println(valor);
        return null;
    }
}