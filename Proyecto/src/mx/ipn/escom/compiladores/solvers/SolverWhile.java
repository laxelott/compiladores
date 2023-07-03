package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverWhile extends Solver {
	public SolverWhile(Nodo nodo) {
		super(nodo);
	}

	@Override
	protected Object resolver(Nodo n) throws SolverException {
		if (Global.DEBUG)
			System.out.println("solWH");
		if (n.getHijos() == null) {
			throw new SolverException("Condición faltante", n.getValue().linea);
		}

		// Checar que la condición sea booleana
		Nodo nodoCondicion = n.getHijos().get(0);
		Solver solver = new SolverAritmetico(nodoCondicion);
		Object condicion = solver.resolver();
		if (!(condicion instanceof Boolean)) {
			throw new SolverException("Booleano inválido (" + condicion + ")", n.getValue().linea);
		}

		n.getHijos().remove(0);

		while ((Boolean) condicion) {
			// Correr lo de adentro del if
			Arbol arbol = new Arbol(n);
			arbol.recorrer();
			condicion = solver.resolver();
		}

		return condicion;
	}
}