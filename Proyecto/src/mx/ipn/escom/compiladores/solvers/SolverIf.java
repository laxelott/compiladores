package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverIf extends Solver {
	public SolverIf(Nodo nodo) {
		super(nodo);
	}

	@SuppressWarnings("unchecked")
    @Override
	protected Object resolver(Nodo n) throws SolverException {
		if (Global.DEBUG)
			System.out.println("solIF");
		if (n.getHijos() == null) {
			throw new SolverException("Condición faltante", n.getValue().linea);
		}

		int end;
		Nodo nodoElse = new Nodo(null);
		Nodo nodoIf = n.clone();
		Solver solver = new SolverAritmetico(n.getHijos().get(0));
		Tuple<TipoToken, Object> condicion = (Tuple<TipoToken, Object>) solver.resolver();
		
		// Checar que la condición sea booleana
		if (!(condicion.x == TipoToken.INT)) {
			throw new SolverException("Booleano inválido (" + condicion + ")", n.getValue().linea);
		}

		// Quitar condición del arbol
		nodoIf.getHijos().remove(0);

		// Checar si el ultimo nodo es un else
		end = nodoIf.getHijos().size() - 1;
		if (nodoIf.getHijos().get(end).getValue().tipo == TipoToken.ELSE) {
			nodoElse = nodoIf.getHijos().get(end);
			nodoIf.getHijos().remove(end);
		}

		if (condicion.y.equals(1)) {
			// Correr lo de adentro del if
			Arbol arbol = new Arbol(nodoIf);
			arbol.recorrer();
		} else if (nodoElse.getValue() != null) {
			Arbol arbol = new Arbol(nodoElse);
			arbol.recorrer();
		}

		return condicion;
	}
}