from syntax import *

print("Inserta la cadena a procesar:")
cadena = input(">> ")

tokens: list[Token] = Scanner.escanear(cadena)

for token in tokens:
    print(token.__str__())