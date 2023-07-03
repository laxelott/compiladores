package mx.ipn.escom.compiladores.generadores;

import mx.ipn.escom.compiladores.*;
import java.util.List;
import java.util.Stack;

public class GeneradorAST {

    private final List<Token> postfija;
    private final Stack<Nodo> pila;

    public GeneradorAST(List<Token> postfija) {
        this.postfija = postfija;
        this.pila = new Stack<>();
    }

    public Arbol generarAST() {
        Stack<Nodo> pilaPadres = new Stack<>();
        Nodo raiz = new Nodo(null);
        pilaPadres.push(raiz);

        Nodo padre = raiz;

        for (int i=0; i< postfija.size(); ++i) {
            Token t = postfija.get(i);
            if (t.tipo == TipoToken.EOF) {
                break;
            }
            
            if (t.tipo == TipoToken.IGUAL) {
                Boolean search = false;
                // Buscar un padre var hasta un semicolon
                for (int j=i; j>=0;--j) {
                    if(postfija.get(j).tipo == TipoToken.VAR) {
                        search = true;
                        break;
                    } else if (postfija.get(j).tipo == TipoToken.SEMICOLON) {
                        break;
                    }
                }
                // Si no hay padre (var), establecerlo como set
                if (!search) {
                    Nodo n = new Nodo(new Token(TipoToken.SET, "set", t.linea));

                    padre = pilaPadres.peek();
                    padre.insertarSiguienteHijo(n);

                    pilaPadres.push(n);
                    padre = n;
                }
            }
            
            if (t.esPalabraReservada()) {
                Nodo n = new Nodo(t);

                padre = pilaPadres.peek();
                padre.insertarSiguienteHijo(n);

                pilaPadres.push(n);
                padre = n;
            } else if (t.esOperando()) {
                Nodo n = new Nodo(t);
                pila.push(n);
            } else if (t.esOperador()) {
                int aridad = t.aridad();
                Nodo n = new Nodo(t);
                for (int j = 1; j <= aridad; j++) {
                    Nodo nodoAux = pila.pop();
                    n.insertarHijo(nodoAux);
                }
                pila.push(n);
            } else if (t.tipo == TipoToken.SEMICOLON) {
                if (pila.isEmpty()) {
                    /*
                     * Si la pila esta vacía es porque t es un punto y coma
                     * que cierra una estructura de control
                     */
                    pilaPadres.pop();
                    padre = pilaPadres.peek();
                } else {
                    Nodo n = pila.pop();

                    if (padre.getValue().tipo == TipoToken.VAR || padre.getValue().tipo == TipoToken.SET) {
                        /*
                         * En el caso del VAR, es necesario eliminar el igual que
                         * pudiera aparecer en la raíz del nodo n.
                         */
                        if (n.getValue().tipo == TipoToken.IGUAL) {
                            padre.insertarHijos(n.getHijos());
                        } else {
                            padre.insertarSiguienteHijo(n);
                        }
                        pilaPadres.pop();
                        padre = pilaPadres.peek();
                    } else if (padre.getValue().tipo == TipoToken.PRINT) {
                        padre.insertarSiguienteHijo(n);
                        pilaPadres.pop();
                        padre = pilaPadres.peek();
                    } else {
                        padre.insertarSiguienteHijo(n);
                    }
                }
            }
        }

        // Suponiendo que en la pila sólamente queda un nodo
        // Nodo nodoAux = pila.pop();
        Arbol programa = new Arbol(raiz);

        return programa;
    }
}
