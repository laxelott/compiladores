package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverIf extends Solver {
	public SolverIf(Nodo nodo) {
		super(nodo);
	}

	@Override
	protected Object resolver(Nodo n) throws SolverException {
		if (Global.DEBUG)
			System.out.println("solIF");
		if (n.getHijos() == null) {
			throw new SolverException("Condición faltante", n.getValue().linea);
		}

		// Checar la condición
		int end;
		Nodo nodoElse = new Nodo(null);
		Boolean boolElse = false;
		Solver solver = new SolverAritmetico(n.getHijos().get(0));
		Object condicion = solver.resolver();
		// Checar que la condición sea booleana
		if (!(condicion instanceof Boolean)) {
			throw new SolverException("Booleano inválido (" + condicion + ")", n.getValue().linea);
		}

		// Checar si el ultimo nodo es un else
		n.getHijos().remove(0);
		end = n.getHijos().size() - 1;
		if (n.getHijos().get(end).getValue().tipo == TipoToken.ELSE) {
			boolElse = true;
			nodoElse = n.getHijos().get(end);
			n.getHijos().remove(end);
		}

		if ((Boolean) condicion) {
			// Correr lo de adentro del if
			Arbol arbol = new Arbol(n);
			arbol.recorrer();
		} else if (boolElse) {
			Arbol arbol = new Arbol(nodoElse);
			arbol.recorrer();
		}

		return condicion;
	}
}