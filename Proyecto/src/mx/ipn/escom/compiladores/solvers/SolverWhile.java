package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverWhile extends Solver {
	public SolverWhile(Nodo nodo) {
		super(nodo);
	}

	@SuppressWarnings("unchecked")
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
		Tuple<TipoToken, Object> condicion = (Tuple<TipoToken, Object>) solver.resolver();
		if (!(condicion.x == TipoToken.INT)) {
			throw new SolverException("Booleano inválido (" + condicion + ")", n.getValue().linea);
		}

		// Quitar condición del árbol
		nodoWhile.getHijos().remove(0);

		while ((condicion.y.equals(1))) {
			// Correr lo de adentro del if
			Arbol arbol = new Arbol(nodoWhile);
			arbol.recorrer();
			condicion = (Tuple<TipoToken, Object>) solver.resolver();
		}

		return condicion;
	}
}