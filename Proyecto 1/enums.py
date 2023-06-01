from enum import Enum
import re 

class Node:
    nombre = ''
    def __init__(self, cadena) -> None:
        self.cadena = cadena
    def match(str) -> str:
        return ''
    def __str__(self) -> str:
        return repr(self.cadena)

class Reservado(Node):
    nombre = 'reservado'
    def __init__(self, cadena) -> None:
        super().__init__(cadena)
    def match(str) -> str:
        list = [item.value for item in Reservado.elementos]
        if str in list:
            return Reservado.elementos(str).value
        else:
            return ''
    
    class elementos(Enum):
        falso = 'false'		# false
        retornar = 'return'	# return
        mientras = 'while'	# while
        clase = 'class'		# class
        imprimir = 'print'	# print
        super = 'super'		# super
        este = 'this'		# this
        verdadero = 'true'	# true
        ademas = 'else'		# else
        nulo = 'null'		# null
        para = 'for'		# for
        funcion = 'def'		# def
        var = 'var'			# var
        si = 'if'			# if
        y = 'and'			# and
        o = 'or'			# or

class Especial(Node):
    nombre = 'especial'
    def __init__(self, cadena) -> None:
        super().__init__(cadena)
    def match(str) -> str:
        list = [item.value for item in Especial.elementos]
        
        for item in list:
            if item in str:
                return item
        return ''

    class elementos(Enum):
        noigual = '!='
        iguala = '=='
        menorigual = '<='
        mayorigual = '>='
        coment = '//'
        # comentInicio = '/*'
        # comentFin = '*/'
        parentIzq = '('
        parentDer = ')'
        llaveIzq = '{'
        llaveDer = '}'
        coma = ','
        #punto = '.'
        puntocoma = ';'
        menos = '-'
        mas = '+'
        por = '*'
        entre = '/'
        no = '!'
        igual = '='
        menor = '<'
        mayor = '>'

class Numero(Node):
    nombre = 'numero'
    def __init__(self, cadena) -> None:
        super().__init__(cadena)
    def match(str) -> str:
        if match := re.search('(?<!\w)\d+\.?\d*(?!\w)', str):
            match = match.group(0)
            if (match[-1] == '.'):
                raise Exception("Falta un decimal!")
            return match
        else:
            return ''

class Cadena(Node):
    nombre = 'cadena'
    def __init__(self, cadena) -> None:
        super().__init__(cadena)
    def match(str) -> str:
        if match := re.search('".*?"', str):
            match = match.group(0)
            return match
        else:
            return ''
    
class Identificador(Node):
    nombre = 'identificador'
    def __init__(self, cadena) -> None:
        super().__init__(cadena)
    def match(str) -> str:
        if match := re.search('[^0-9\n\0 ]+\d*', str):
            match = match.group(0)
            return match
        else:
            return ''

class Comentario(Node):
    nombre = 'comentario'
    def __init__(self, cadena) -> None:
        super().__init__(cadena)
    def match(str) -> str:
        if match := re.search('(\/\*.*?\*\/)|(\/\/.*?(?=\n))', str, re.DOTALL):
            match = match.group(0)
            return match
        else:
            return ''
    
class Newline(Node):
    nombre = 'newline'
    def __init__(self, cadena) -> None:
        super().__init__(cadena)
    def match(str) -> str:
        if (str == '\n'):
            return 'Newline'
        else:
            return ''

class EOF(Node):
    nombre = 'end-of-file'
    def __init__(self, cadena) -> None:
        super().__init__(cadena)
    def match(str) -> str:
        if (str == '\0'):
            return 'EOF'
        else:
            return ''
        
class Espacio(Node):
    nombre = 'espacio'
    def __init__(self, cadena) -> None:
        super().__init__(cadena)
    def match(str) -> str:
        if (str == ' '):
            return ' '
        else:
            return ''