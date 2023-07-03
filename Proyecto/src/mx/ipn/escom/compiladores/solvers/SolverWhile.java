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

		Nodo nodoWhile = n.clone();

		// Checar que la condición sea booleana
		Solver solver = new SolverAritmetico(n.getHijos().get(0));
		Object condicion = solver.resolver();
		if (!(condicion instanceof Boolean)) {
			throw new SolverException("Booleano inválido (" + condicion + ")", n.getValue().linea);
		}

		// Quitar condición del árbol
		nodoWhile.getHijos().remove(0);

		while ((Boolean) condicion) {
			// Correr lo de adentro del if
			Arbol arbol = new Arbol(nodoWhile);
			arbol.recorrer();
			condicion = solver.resolver();
		}

		return condicion;
	}
}