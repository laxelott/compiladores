from enums import *

class Token:
    reservados = [item.value for item in Reservado]
    especiales = [item.value for item in Especial]
    numeros = [item.value for item in Numero]

    def __init__(self, cadena) -> None:
        if cadena in self.reservados:
            self.valor = Reservado(cadena)
        elif cadena in self.especiales:
            self.valor = Especial(cadena)
        elif cadena in self.numeros:
            self.valor = Numero(cadena)
        elif cadena[0] == '"':
            self.valor = Cadena(cadena[1:-1])
        elif cadena == '\0':
            self.valor = EOF()
        else:
            self.valor = Identificador(cadena)
    
    def tipo(self):
        if hasattr(self.valor, "nombre"):
            return self.valor.nombre
        else:
            return "quien-sabe"
    
    def __str__(self) -> str:
        return f"({self.tipo()}) {self.valor}"

class Scanner():
    def escanear(cadena: str):
        resultado = []
        tokens = cadena.split(" ")
        buscarCadena = False
        charIndex = 0
        progresoCadena = ""
        
        for token in tokens:
            charIndex += len(token)

            if buscarCadena:
                progresoCadena += " " + token
                if token[-1:] == '"':
                    buscarCadena = False
                    resultado.append(Token(progresoCadena))
                    progresoCadena = ""
            elif token[0] == '"':
                buscarCadena = True
                progresoCadena += token
            else:
                resultado += Scanner.detectarToken(token)
            
            charIndex += 1
        
        resultado.append(Token('\0'))
        
        return resultado

    def detectarToken(token: str):
        if len(token) == 0:
            return []
        elif len(token) == 1:
            return [Token(token)]
        elif any((match := substring) in token for substring in Token.especiales):
            index = token.index(match)
            t1 = token[:index]
            t2 = token[index]
            t3 = token[index+1:]
            return [*Scanner.detectarToken(t1), Token(t2), *Scanner.detectarToken(t3)]
        elif not token[-1:].isalnum():
            t1 = token
            t2 = ''
            i = len(token) - 1
            while not token[i].isalnum():
                t1 = t1[:-1]
                t2 += token[i] + t2
                i -= 1
                if i==0:
                    break
            return [*Scanner.detectarToken(t1), Token(t2)]
        elif not token[0].isalpha():
            t1 = ''
            t2 = token
            i = 0
            while not token[i].isalpha():
                t1 += token[i]
                t2 = t2[1:]
                i += 1
                if i==len(token):
                    break
            return [Token(t1), *Scanner.detectarToken(t2)]
        else:
            return [Token(token)]