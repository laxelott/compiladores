package mx.ipn.escom.compiladores;

import mx.ipn.escom.compiladores.solvers.*;

public class Arbol {
    private Nodo raiz;

    public Arbol() {}

    public Arbol(Nodo raiz) {
        this.raiz = raiz;
    }

    public void ejecutarNodo(Nodo n) throws SolverException {
        Solver solver;
        Token t = n.getValue();
        solver = new Solver(n);
        
        switch (t.tipo) {
            // Operadores aritméticos
            case SUMA:
            case RESTA:
            case MULTIPLICACION:
            case DIVISION:
                solver = new SolverAritmetico(n);
                break;
            case VAR:
            case SET:
                solver = new SolverVariable(n);
                break;
            case IF:
                solver = new SolverIf(n);
                break;
            case WHILE:
                solver = new SolverWhile(n);
                break;
            case FOR:
                solver = new SolverFor(n);
                break;
            case PRINT:
                solver = new SolverPrint(n);
                break;
            default:
                throw new SolverException("Posición inválida (" + t.lexema + ")", n.getValue().linea);
        }
        // Corriendo el solver adecuado
        solver.resolver();
    }

    public void recorrer() throws SolverException {
        for (Nodo n : raiz.getHijos()) {
            this.ejecutarNodo(n);
        }
    }

    @Override
    public String toString() {
        String res = "";
        for (Nodo n : raiz.getHijos()) {
            res += n.toString();
        }
        return res;
    }

}
