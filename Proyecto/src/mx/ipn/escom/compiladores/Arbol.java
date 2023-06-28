package mx.ipn.escom.compiladores;

import mx.ipn.escom.compiladores.solvers.*;

public class Arbol {
    private final Nodo raiz;
    public TablaSimbolos tabla;

    public Arbol(Nodo raiz) {
        this.raiz = raiz;
    }

    public void recorrer() throws SolverException {
            Solver solver;
            for (Nodo n : raiz.getHijos()) {
                Token t = n.getValue();
                solver = new Solver(n, this.tabla);
                
                switch (t.tipo) {
                    // Operadores aritméticos
                    case SUMA:
                    case RESTA:
                    case MULTIPLICACION:
                    case DIVISION:
                        solver = new SolverAritmetico(n, this.tabla);
                        break;
                    case VAR:
                        solver = new SolverVariable(n, this.tabla);
                        break;
                    case SET:
                        solver = new SolverVariable(n, this.tabla);
                        break;
                    case IF:
                        solver = new SolverIf(n, this.tabla);
                        break;
                    case PRINT:
                        solver = new SolverPrint(n, this.tabla);
                        break;
                    default:
                        throw new SolverException("Posición inválida", n.getValue().linea);
                }
                // Corriendo el solver adecuado
                solver.resolver();
                this.tabla = solver.tabla;
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
