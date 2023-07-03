package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverFor extends Solver {
	public SolverFor(Nodo nodo) {
		super(nodo);
	}

	@Override
	protected Object resolver(Nodo n) throws SolverException {
		if (Global.DEBUG)
			System.out.println("solFO");
		if (n.getHijos() == null) {
			throw new SolverException("For vacío", n.getValue().linea);
		}
		if (n.getHijos().size() < 3) {
			throw new SolverException("For incompleto!", n.getValue().linea);
		}

		Arbol arbol;
		Nodo nodoFor = n.clone();

		nodoFor.getHijos().remove(0);
		nodoFor.getHijos().remove(0);
		nodoFor.getHijos().remove(0);

		// Ejecutar el primer nodo
		arbol = new Arbol();
		arbol.ejecutarNodo(n.getHijos().get(0));

		// Checar que el nodo condición sea booleano
		Nodo nodoCondicion = n.getHijos().get(1);
		Solver solver = new SolverAritmetico(nodoCondicion);
		Object condicion = solver.resolver();
		if (!(condicion instanceof Boolean)) {
			throw new SolverException("Booleano inválido (" + condicion + ")", n.getValue().linea);
		}

		// Mover el nodo paso hasta el final
		nodoFor.getHijos().add(n.getHijos().get(2));

		while ((Boolean) condicion) {
			arbol = new Arbol(nodoFor);
			arbol.recorrer();
			solver = new SolverAritmetico(nodoCondicion);
			condicion = solver.resolver();
		}

		return condicion;
	}
}