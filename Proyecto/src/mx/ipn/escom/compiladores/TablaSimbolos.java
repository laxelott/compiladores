package mx.ipn.escom.compiladores;

import java.util.HashMap;
import java.util.Map;

public class TablaSimbolos {

    private final Map<String, Tuple<TipoToken, Object>> values = new HashMap<>();

    public boolean existeIdentificador(String identificador) {
        return values.containsKey(identificador);
    }

    public Tuple<TipoToken, Object> obtener(String identificador) {
        if (values.containsKey(identificador)) {
            return values.get(identificador);
        }
        throw new RuntimeException("Variable no definida '" + identificador + "'.");
    }

    public void asignar(String identificador) {
        values.put(identificador, null);
    }

    public void asignar(String identificador, TipoToken tipo, Object valor) {
        values.put(identificador, new Tuple<TipoToken, Object>(tipo, valor));
    }

}