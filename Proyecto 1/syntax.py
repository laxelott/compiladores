from enums import *

class Token:
    def getToken(cadena) -> str:
        # Lista de detección con prioridad
        tipos: list[Node] = [
            Comentario,
            Cadena,
            Espacio,
            Numero,
            Reservado,
            Especial,
            Identificador,
            Newline,
            Select,
            From,
            Distinct,
            EOF
        ]
        
        token = ''
        match = False
        splits = ['', '']
        for tipo in tipos:
            if (found := tipo.match(cadena)) != '':
                token = Token(tipo(found))
                match = True
                if cadena != "\n":
                    splits = cadena.split(found, 1)
                break

        return match, token, splits[0], splits[1]
    
    def __init__(self, valor) -> None:
        self.valor = valor
    
    def tipo(self):
        if hasattr(self.valor, "nombre"):
            return self.valor.nombre
        else:
            return "quien-sabe"
    
    def __str__(self) -> str:
        return f"({self.tipo()}) {self.valor}"

class Scanner():
    def escanear(cadena: str):
        resultado = Scanner.findTokens(cadena)

        return resultado

    def findTokens(cadena: str):
        if len(cadena) == 0:
            return []
        
        match, token, prev, next = Token.getToken(cadena)
        if match:
            if type(token.valor) is Espacio:
                return [*Scanner.findTokens(prev), *Scanner.findTokens(next)]
            else:
                return [*Scanner.findTokens(prev), token, *Scanner.findTokens(next)]
        else:
            raise Exception(f'Error! token inválida -> "{cadena}"')
        