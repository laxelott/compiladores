package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class Solver {
    private final Nodo nodo;
    public final TablaSimbolos tabla; 
	public Solver(Nodo nodo, TablaSimbolos tabla) {
		this.nodo = nodo;
		this.tabla = tabla;
	}
	public Object resolver() throws SolverException {
        return resolver(nodo);
    }
    protected Object resolver(Nodo n) throws SolverException {
		return null;
	}
}