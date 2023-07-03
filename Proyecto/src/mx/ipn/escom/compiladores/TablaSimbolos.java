package mx.ipn.escom.compiladores;

import java.util.HashMap;
import java.util.Map;

public class TablaSimbolos {

    private static final Map<String, Tuple<TipoToken, Object>> values = new HashMap<>();

    public static void printValues() {
        System.out.println("--- TABLE VALUES ---");
        for (Map.Entry<String, Tuple<TipoToken, Object>> entry : values.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue().x + "(" + entry.getValue().y + ")");
        }
    }

    public static boolean existeIdentificador(String identificador) {
        return values.containsKey(identificador);
    }

    public static Tuple<TipoToken, Object> obtener(String identificador) {
        if (values.containsKey(identificador)) {
            return values.get(identificador);
        }
        throw new RuntimeException("Variable no definida '" + identificador + "'.");
    }

    public static void asignar(String identificador) {
        values.put(identificador, null);
    }

    public static void asignar(String identificador, TipoToken tipo, Object valor) {
        values.put(identificador, new Tuple<TipoToken, Object>(tipo, valor));
    }
}