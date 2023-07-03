package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class Solver {
    private final Nodo nodo;
	public Solver(Nodo nodo) {
		this.nodo = nodo;
	}
	public Object resolver() throws SolverException {
        return resolver(nodo);
    }
    protected Object resolver(Nodo n) throws SolverException {
		return null;
	}
}