package mx.ipn.escom.compiladores;


import mx.ipn.escom.compiladores.generadores.*;
import mx.ipn.escom.compiladores.solvers.SolverException;

import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;


public class Principal {

    static boolean existenErrores = false;
    static TablaSimbolos tabla;

    public static void main(String[] args) throws IOException {
        tabla = new TablaSimbolos();

        if (args.length > 1) {
            System.out.println("Uso correcto: interprete [script]");

            // Convención defininida en el archivo "system.h" de UNIX
            System.exit(64);
        } else if (args.length == 1) {
            ejecutarArchivo(args[0]);
        } else {
            ejecutarPrompt();
        }
    }

    private static void ejecutarArchivo(String path) throws IOException {
        byte[] bytes = Files.readAllBytes(Paths.get(path));
        ejecutar(new String(bytes, Charset.defaultCharset()));

        // Se indica que existe un error
        if (existenErrores) {
            System.exit(65);
        }
    }

    private static void ejecutarPrompt() throws IOException {
        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input);

        for (;;) {
            System.out.print(">>> ");
            String linea = reader.readLine();
            if (linea == null)
                break; // Presionar Ctrl + D
            ejecutar(linea);
            existenErrores = false;
        }
    }

    private static void ejecutar(String source) {
        Scanner scanner = new Scanner(source);
        List<Token> tokens = scanner.scanTokens();

        /*
         * for(Token token : tokens){
         * System.out. println(token);
         * }
         */

        // Para este ejemplo no vamos a utilizar un parser
        /*
         * Parser parser = new Parser(tokens);
         * parser.parse();
         */

        GeneradorPostfija gpf = new GeneradorPostfija(tokens);
        List<Token> postfija = gpf.convertir();

        // System.out.println(tokens);
        // System.out.println(postfija);

        if (postfija.size() == 0) {
            return;
        }
        /*
         * for(Token token : postfija){
         * System.out. println(token);
         * }
         */

        GeneradorAST gast = new GeneradorAST(postfija);
        Arbol programa = gast.generarAST();
        programa.tabla = tabla;
        System.out.println(programa);

        try {
            programa.recorrer();
            tabla = programa.tabla;
        } catch(SolverException exception) {
            String donde = "semántico";
            String mensaje = exception.getMessage();
            int linea = 0;

            reportar(linea, donde, mensaje);
        }
    }

    private static void reportar(int linea, String donde, String mensaje) {
        System.err.println("[linea " + linea + "] Error " + donde + ": " + mensaje);
        existenErrores = true;
    }

}