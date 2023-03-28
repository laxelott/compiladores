from enum import Enum

class Reservado(Enum):
    @property
    def nombre(self):
        return 'reservado'
    y = 'y'					# and
    clase = 'clase'			# class
    ademas = 'ademas'		# else
    falso = 'falso'			# false
    para = 'para'			# for
    funcion = 'funcion'		# def
    si = 'si'				# if
    nulo = 'nulo'			# null
    o = '||'				# or
    imprimir = 'imprimir'	# print
    retornar = 'retornar'	# return
    super = 'super'			# super
    este = 'este'			# this
    verdadero = 'verdadero'	# rue
    var = 'var'				# var
    mientras = 'mientras'	# while
class Especial(Enum):
    @property
    def nombre(self):
        return 'especial'
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
    noigual = '!='
    igual = '='
    iguala = '=='
    menor = '<'
    menorigual = '<='
    mayor = '>'
    mayorigual = '>='
    coment = '//'
    comentInicio = '/*'
    comentFin = '*/'
class Numero(Enum):
    @property
    def nombre(self):
        return 'numero'
    cero = '0'
    uno = '1'
    dos = '2'
    tres = '3'
    cuatro = '4'
    cinco = '5'
    seis = '6'
    siete = '7'
    ocho = '8'
    nueve = '9'

class Cadena:
    nombre = 'cadena'
    def __init__(self, cadena) -> None:
        self.cadena = cadena
    def __str__(self) -> str:
        return self.cadena
class Identificador:
    nombre = 'identificador'
    def __init__(self, cadena) -> None:
        self.identificador = cadena
    def __str__(self) -> str:
        return self.identificador
class EOF:
    nombre = 'end-of-file'
    def __init__(self) -> None:
        self.valor = '\0'
    def __str__(self) -> str:
        return 'EOF'