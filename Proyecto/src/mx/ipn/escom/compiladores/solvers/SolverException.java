package mx.ipn.escom.compiladores.solvers;

public class SolverException extends Exception {
    public final int linea;
	public SolverException(String errorMessage, int linea) {
        super(errorMessage);
        this.linea = linea;
    }
}