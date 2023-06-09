from enum import Enum
import re 

class Node:
    name = ''
    def __init__(self, value) -> None:
        self.value = value
    def match(str) -> str:
        return ''
    def __str__(self) -> str:
        return repr(self.value)

class Reservado(Node):
    name = 'reservado'
    def __init__(self, value) -> None:
        super().__init__(value)
    def match(str) -> str:
        list = [item.value for item in Reservado.elementos]
        for item in list:
            if item in str:
                return item
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

class SQLReserved(Node):
    name = "sql"
    def __init__(self, value) -> None:
        super().__init__(value)
    def match(str) -> str:
        list = [item.value for item in SQLReserved.elementos]
        for item in list:
            if item in str:
                return item
        return ''
    
    # Usar declaración funcional porque "from" es reservado
    elementos = Enum('elementos',
        [
            ('select', 'select'),
            ('from', 'from'),
            ('distinct', 'distinct')
        ]
    )

class Especial(Node):
    name = 'especial'
    def __init__(self, value) -> None:
        super().__init__(value)
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
        punto = '.'
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
    name = 'numero'
    def __init__(self, value) -> None:
        super().__init__(value)
    def match(str) -> str:
        if match := re.search('(?<!\w)\d+\.?\d*(?!\w)', str):
            match = match.group(0)
            if (match[-1] == '.'):
                raise Exception("Falta un decimal!")
            return match
        else:
            return ''

class Cadena(Node):
    name = 'value'
    def __init__(self, value) -> None:
        super().__init__(value)
    def match(str) -> str:
        if match := re.search('".*?"', str):
            match = match.group(0)
            return match
        else:
            return ''
    
class Identificador(Node):
    name = 'identificador'
    def __init__(self, value) -> None:
        super().__init__(value)
    def match(str) -> str:
        if match := re.search('[^0-9\n\0 ]+\d*', str):
            match = match.group(0)
            return match
        else:
            return ''

class Comentario(Node):
    name = 'comentario'
    def __init__(self, value) -> None:
        super().__init__(value)
    def match(str) -> str:
        if match := re.search('(\/\*.*?\*\/)|(--.*?(?=\n))', str, re.DOTALL):
            match = match.group(0)
            return match
        else:
            return ''
    
class Newline(Node):
    name = 'newline'
    def __init__(self, value) -> None:
        super().__init__(value)
    def match(str) -> str:
        if (str == '\n'):
            return 'Newline'
        else:
            return ''

class EOF(Node):
    name = 'end-of-file'
    def __init__(self, value) -> None:
        super().__init__(value)
    def match(str) -> str:
        if (str == '\0'):
            return 'EOF'
        else:
            return ''
        
class Espacio(Node):
    name = 'espacio'
    def __init__(self, value) -> None:
        super().__init__(value)
    def match(str) -> str:
        if (str == ' '):
            return ' '
        else:
            return ''
