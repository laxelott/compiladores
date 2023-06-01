from syntax import *
import sys
import re

def readFile(fileName):
    lines = []
    with open(fileName) as archivo:
        lines = archivo.read()
    return lines

fileName = sys.argv[1] if len(sys.argv) > 1 else ""

if fileName != "":
    print(f"Procesando archivo {fileName}...")
    lines = re.sub(r'\n+', '\n', readFile(fileName))
    tokens: list[Token] = Scanner.escanear(lines)
    
    for token in tokens:
        print(token.__str__())
else:
    while(True):
        line = input("> ")
        tokens: list[Token] = Scanner.escanear(line)
        
        for token in tokens:
            print(token.__str__())