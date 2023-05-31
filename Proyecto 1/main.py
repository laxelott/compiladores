from syntax import *
import sys

def readFile(fileName):
    lines = []
    with open(fileName) as archivo:
        lines = archivo.readlines()
    return lines

fileName = sys.argv[1] if len(sys.argv) > 1 else ""

if fileName != "":
    print(f"Procesando archivo {fileName}...")
    lines = readFile(fileName)
    i = 1
    print(lines)
    for line in lines:
        print(f"--- Linea {i}")
        i += 1
        tokens: list[Token] = Scanner.escanear(line)
        
        for token in tokens:
            print(token.__str__())
else:
    while(True):
        line = input("> ")
        tokens: list[Token] = Scanner.escanear(line)
        
        for token in tokens:
            print(token.__str__())