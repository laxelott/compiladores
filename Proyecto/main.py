import sys
from syntax import *
from parse import *
from patterns import *

def readFile(filename):
    lines = []
    with open(filename) as archivo:
        lines = archivo.read()
    return lines


fileName = sys.argv[1] if len(sys.argv) > 1 else ""
patterns = Patterns()

if fileName != "":
    print(f"Procesando archivo {fileName}...")
    lines = re.sub(r'\n+', '\n', readFile(fileName))
    tokens: list[Token] = Scanner.escanear(lines) 
    
    for token in tokens:
        print(token.__str__())
    
    # Quitar los comentarios de las tokens
    tokens = list(filter(lambda token: not (type(token.node) is Comentario), tokens))
        
    try:
        finder = PatternFinder(tokens)
        parse = finder.findRegularDefinition(patterns.PROGRAM())

        if len(finder.tokens) > 0:
            print(finder.printTokens())
            raise ParserError(f"Error: {finder.tokens[0].node.value} inválido!")
    except ParserError as error:
        print(error)
    else:
        print("Sentencia válida")
else:
    while (True):
        line = input("> ")
        tokens: list[Token] = Scanner.escanear(line)

        # for token in tokens:
        #     print(token.__str__())

        try:
            finder = PatternFinder(tokens)
            parse = finder.findRegularDefinition(patterns.PROGRAM())

            if len(finder.tokens) > 0:
                raise ParserError(
                    f"Error: {finder.tokens[0].node.value} inválido!")
        except ParserError as error:
            print(error)
        else:
            print("Sentencia válida")
