package mx.ipn.escom.compiladores;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TablaSimbolos {

    private static final ArrayList<Map<String, Tuple<TipoToken, Object>>> values = new ArrayList<>();
    private static final Map<String, Tuple<TipoToken, Nodo>> functions = new HashMap<>();
    private static final Map<String, ArrayList<Tuple<TipoToken, String>>> parameters = new HashMap<>();

    /*
     *  VALORES
     */    

    public static void printValues() {
        System.out.println("--- VARIABLE VALUES ---");
        for (Map<String, Tuple<TipoToken, Object>> table : values) {
            System.out.println(". --------- . --------- .");
            for(Map.Entry<String, Tuple<TipoToken, Object>> entry : table.entrySet()) {
                System.out.println(entry.getKey() + " -> " + entry.getValue().x + "(" + entry.getValue().y + ")");
            }
        }
        System.out.println("--- FUNCTION VALUES ---");
        for (Map.Entry<String, Tuple<TipoToken, Nodo>> entry : functions.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue().x + "(" + entry.getValue().y + ")");
        }
    }

    public static void generarNuevaTabla() {
        Map<String, Tuple<TipoToken, Object>> tabla = new HashMap<>();
        values.add(tabla);
    }
    public static void removerTabla() {
        values.remove(values.size()-1);
    }

    public static boolean existeIdentificadorVariable(String identificador) {
        for (int i=values.size()-1; i<=0; i--) {
            if (values.get(i).containsKey(identificador)) {
                return true;
            }
        }
        return false;
    }

    public static Object obtenerVariable(String identificador) {
        for (int i=values.size()-1; i<=0; i--) {
            if (values.get(i).containsKey(identificador)) {
                if (values.get(values.size()-1).get(identificador).y == null) {
                    throw new RuntimeException("Valor de variable '" + identificador + "' no establecido.");
                }
                return values.get(i).get(identificador).y;
            }
        }
        throw new RuntimeException("Variable no definida '" + identificador + "'.");
    }

    public static Object obtenerTipoVariable(String identificador) {
        for (int i=values.size()-1; i<=0; i--) {
            if (values.get(i).containsKey(identificador)) {
                return values.get(i).get(identificador).x;
            }
        }
        throw new RuntimeException("Variable no definida '" + identificador + "'.");
    }

    public static void asignarVariable(String identificador, TipoToken tipo) {
        asignarVariable(identificador, tipo, null);
    }

    public static void asignarVariable(String identificador, TipoToken tipo, Object valor) {
        values.get(values.size()-1).put(identificador, new Tuple<TipoToken, Object>(tipo, valor));
    }
    
    public static void desasignarVariable(String identificador) {
        values.get(values.size()-1).remove(identificador);
    }

    /*
     *  FUNCIONES
     */    

    public static boolean existeIdentificadorFuncion(String identificador) {
        return functions.containsKey(identificador);
    }

    public static Object obtenerFuncion(String identificador) {
        if (!functions.containsKey(identificador)) {
            throw new RuntimeException("Funcion no definida '" + identificador + "'.");
        }
        else if (functions.get(identificador).y == null) {
            throw new RuntimeException("Valor de Funcion '" + identificador + "'no establecido.");
        }
        return functions.get(identificador).y;
    }

    public static TipoToken obtenerTipoFuncion(String identificador) {
        if (!functions.containsKey(identificador)) {
            throw new RuntimeException("Funcion no definida '" + identificador + "'.");
        }
        return functions.get(identificador).x;
    }

    public static void asignarFuncion(String identificador, TipoToken tipo) {
        functions.put(identificador, new Tuple<TipoToken, Nodo>(tipo, null));
    }

    public static void asignarFuncion(String identificador, TipoToken tipo, Nodo nodo) {
        functions.put(identificador, new Tuple<TipoToken, Nodo>(tipo, nodo));
    }

    /*
     *  PARAMETROS
     */

    public static boolean existeIdentificadorParametro(String identificador) {
        return parameters.containsKey(identificador);
    }

    @SuppressWarnings("unchecked")
    public static Tuple<TipoToken, String>[] obtenerParametros(String identificador) {
        return (Tuple<TipoToken, String>[]) parameters.get(identificador).toArray();
    }

    @SuppressWarnings({ "rawtypes", "unchecked" })
    public static void asignarParametros(String identificador, Tuple<TipoToken, String>[] parametros) {
        parameters.put(identificador, new ArrayList(Arrays.asList(parametros)));
    }
}