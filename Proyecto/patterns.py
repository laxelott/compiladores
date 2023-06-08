Valor = [
    {
        'match': Identificador,
        'required': True,
        'error': 'Identificador faltante'
    }, {
        'match': '.',
        'required': False,
        'next': [
            {
                'match': Identificador,
                'required': True,
                'error': 'Identificador incompleto (sobra un punto)'
            }
        ]
    }
]

Tabla = [
    {
        'match': Identificador,
        'required': True,
        'error': 'Identificador faltante'
    }, {
        'match': Identificador,
        'required': False
    }
]

Parametros = [
    {
        'match': '*',
        'required': False,
        'final': True
    }, {
        'match': 'distinct',
        'required': False,
    }, {
        'match': Valor,
        'required': True,
        'error': 'Valor faltante'
    }, {
        'match': ',',
        'required': False,
        'looping': True,
        'next': [
            {
                'match': Valor,
                'required': True,
                'error': 'Valor faltante (sobra una coma)'
            }
        ]
    }
]

Tablas = [
    {
        'match': Tabla,
        'required': True,
        'error': 'Tabla faltante'
    }, {
        'match': ',',
        'required': False,
        'looping': True,
        'next': [
            {
                'match': Tabla,
                'required': True,
                'error': 'Tabla faltante (sobra una coma)'
            }
        ]
    }
]

Query = [
    {
        'match': 'select',
        'required': True,
        'error': 'Select faltante'
    }, {
        'match': Parametros,
        'required': True,
        'error': 'Parametros faltantes'
    }, {
        'match': 'from',
        'required': True,
        'error': 'From faltante'
    }, {
        'match': Tablas,
        'required': True,
        'error': 'Tablas faltantes'
    }
]


While_stmt = [
	{
        'match': 'while',
        'required': True,
        'error': 'Select faltante'
    }, {
        'match': '(',
        'required': True,
        'error': 'Select faltante'
    }, {
        'match': Expression,
        'required': True,
        'error': 'Select faltante'
    }, {
        'match': ')',
        'required': True,
        'error': 'Select faltante'
    }, {
        'match': Statement,
        'required': True,
        'error': 'Select faltante'
    }
]