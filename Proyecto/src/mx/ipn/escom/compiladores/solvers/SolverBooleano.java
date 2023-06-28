package mx.ipn.escom.compiladores.solvers;

import mx.ipn.escom.compiladores.*;

public class SolverBooleano extends Solver {
    public SolverBooleano(Nodo nodo, TablaSimbolos tabla) {
        super(nodo, tabla);
    }

	public static Boolean getBool(TipoToken valor) {
		return valor.equals(TipoToken.TRUE);
	}

    @Override
    protected Boolean resolver(Nodo n) throws SolverException {
		System.out.println("SolverBOOL");
		if (n.getHijos() != null) {
            throw new SolverException("Valor inválido boo", n.getValue().linea);
        }
		
		switch (n.getValue().tipo) {
			case TRUE:
				return true;
			case FALSE:
				return false;
			case IDENTIFICADOR:
				SolverVariable.validateVariable(n, tabla);
				
				Object valor = this.tabla.obtener((String) n.getValue().lexema);
				if (valor.getClass() != Boolean.class) {
					throw new SolverException("Booleano inválido", n.getValue().linea);
				} else {
					return (Boolean) valor;
				}
			default:
				throw new SolverException("Booleano inválido", n.getValue().linea);
		}
    }
}