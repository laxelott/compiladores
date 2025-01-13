package mx.ipn.escom.compiladores;

public enum TipoToken {
    IDENTIFICADOR,
    INTTYPE, FLOATTYPE, STRINGTYPE, CHARTYPE,
    FUNCTIONTYPE,

    // Palabras reservadas
    IF, PRINT, ELSE,
    WHILE, FOR,
    AND, OR,
    TRUE, FALSE,
    RETURN, VOID,
    PARAMS,
    SET,

    // Tipo de dato
    INT, FLOAT, STRING, CHAR, FUNCTION,

    // Caracteres
    SUMA, RESTA, MULTIPLICACION, DIVISION,
    IGUAL, MAYOR, MAYOR_IGUAL, MENOR, MENOR_IGUAL,
    IGUAL_A,
    LPAREN, RPAREN, LBRACE, RBRACE, SEMICOLON,

    // Final de cadena
    EOF
}
