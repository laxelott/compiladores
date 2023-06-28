package mx.ipn.escom.compiladores;

public enum TipoToken {
    IDENTIFICADOR, NUMERO, CADENA,

    // Palabras reservadas
    IF, VAR, PRINT, ELSE,
    AND, OR,
    TRUE, FALSE,
    SET,

    // Caracteres
    SUMA, RESTA, MULTIPLICACION, DIVISION,
    IGUAL, MAYOR, MAYOR_IGUAL, MENOR, MENOR_IGUAL,
    IGUAL_A,
    LPAREN, RPAREN, LBRACE, RBRACE, SEMICOLON,

    // Final de cadena
    EOF
}
