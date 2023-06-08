from syntax import *
from parseDescendiente import *
# from parseAscendiente import *

while(True):
    line = input("> ")
    tokens: list[Token] = Scanner.escanear(line)
    
    # for token in tokens:
    #     print(token.__str__())
        
    try:
        finder = PatternFinder(tokens)
        parse = finder.findRegularDefinition(Query)
        
        if len(finder.tokens) > 0:
            raise ParserError(f"Error: {finder.tokens[0].node.value} inválido!")
    except ParserError as error:
        print(error)
    else:
        print("Sentencia válida")