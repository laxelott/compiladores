from enums import *

class Token:
    def __init__(self, node: Node) -> None:
        self.node = node
    
    def tipo(self):
        if hasattr(self.node, "name"):
            return self.node.name
        else:
            return "quien-sabe"
    
    def __str__(self) -> str:
        return f"({self.tipo()}) {self.node}"

class Scanner():
    def escanear(cadena: str):
        resultado = Scanner.findTokens(cadena)

        return resultado

    def findTokens(cadena: str):
        if len(cadena) == 0:
            return []
        
        match: bool
        token: Token
        prev:str
        next: str
        match, token, prev, next = getToken(cadena)
        if match:
            if type(token.node) is Basura:
                return [*Scanner.findTokens(prev), *Scanner.findTokens(next)]
            else:
                return [*Scanner.findTokens(prev), token, *Scanner.findTokens(next)]
        else:
            raise Exception(f'Error! token inválida -> "{cadena}"')
        
def getToken(string: str) -> tuple[bool, Token, str, str]:
    # Lista de detección con prioridad
    tipos: list[Node] = [
        Comentario,
        Cadena,
        Basura,
        Numero,
        Especial,
        Reservado,
        Identificador,
        EOF
    ]
    
    token = ''
    match = False
    splits = ['', '']
    for tipo in tipos:
        if (found := tipo.match(string)) != '':
            token = Token(tipo(found))
            match = True
            if string != "\n":
                splits = string.split(found, 1)
            break

    return match, token, splits[0], splits[1]

