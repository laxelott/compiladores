from yaml_parser import Node

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
    def findTokens(cadena: str, nodeList: list[Node], ignoreList: list[Node]):
        if len(cadena) == 0:
            return []
        
        match: bool
        token: Token
        prev:str
        next: str
        match, token, prev, next = getToken(cadena, nodeList)
        if match:
            if type(token.node) is ignoreList:
                return [*Scanner.findTokens(prev), *Scanner.findTokens(next)]
            else:
                return [*Scanner.findTokens(prev), token, *Scanner.findTokens(next)]
        else:
            raise Exception(f'Error! token inválida -> "{cadena}"')
        
def getToken(string: str, nodeList: list[Node]) -> tuple[bool, Token, str, str]:
    token = ''
    match = False
    splits = ['', '']
    for tipo in nodeList:
        if (found := tipo.match(string)) != '':
            token = Token(tipo(found))
            match = True
            if string != "\n":
                splits = string.split(found, 1)
            break

    return match, token, splits[0], splits[1]

