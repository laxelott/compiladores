from __future__ import annotations

class Patterns:
    # PROGRAMA
    def PROGRAM(self):
        print("PROGRAM")
        return [
            {
                'match': self.DECLARATION,
                'required': True,
                'looping': True,
                'error': 'PROGRAM: DECLARATION faltante'
            }
        ]

    # DECLARACIONES
    def DECLARATION(self):
        print("DECLARATION")
        return [
            {
                'match': self.CLASS_DECL,
                'required': False
            },
            {
                'match': self.FUN_DECL,
                'required': False
            },
            {
                'match': self.VAR_DECL,
                'required': False
            },
            {
                'match': self.STATEMENT,
                'required': False
            }
        ]


    def CLASS_DECL(self):
        print("CLASS_DECL")
        return [
            {
                'match': 'class',
                'required': False,
                'error': 'CLASS_DECL: class faltante',
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'CLASS_DECL: id faltante'
                    },
                    {
                        'match': self.CLASS_INHER,
                        'required': False,
                        'error': 'CLASS_DECL: CLASS_INHER faltante'
                    },
                    {
                        'match': '{',
                        'required': True,
                        'error': 'CLASS_DECL: { faltante'
                    },
                    {
                        'match': self.FUNCTIONS,
                        'required': False,
                        'error': 'CLASS_DECL: FUNCTIONS faltante'
                    },
                    {
                        'match': '}',
                        'required': True,
                        'error': 'CLASS_DECL: } faltante'
                    }
                ]
            }
        ]

    def CLASS_INHER(self):
        print("CLASS_INHER")
        return [
            {
                'match': '<',
                'required': False,
                'error': 'CLASS_INHER: < faltante',
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'CLASS_INHER: id faltante'
                    }
                ]
            },
        ]

    def FUN_DECL(self):
        print("FUN_DECL")
        return [
            {
                'match': 'fun',
                'required': False,
                'error': 'FUN_DECL: fun faltante',
                'next': [
                    {
                        'match': self.FUNCTION,
                        'required': True,
                        'error': 'FUN_DECL: FUNCTION faltante'
                    }    
                ]
            }
        ]

    def VAR_DECL(self):
        print("VAR_DECL")
        return [
            {
                'match': 'var',
                'required': False,
                'error': 'VAR_DECL: var faltante',
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'VAR_DECL: Identificador faltante'
                    },
                    {
                        'match': self.VAR_INIT,
                        'required': False,
                        'error': 'VAR_DECL: VAR_INIT faltante'
                    },
                    {
                        'match': ';',
                        'required': True,
                        'error': 'VAR_DECL: ; faltante'
                    }       
                ]
            }
        ]

    def VAR_INIT(self):
        print("VAR_INIT")
        return [
            {
                'match': '=',
                'required': False,
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'VAR_INIT: EXPRESSION faltante'
                    }
                ]
            },
        ]

    # SENTENCIAS
    def STATEMENT(self):
        print("STATEMENT")
        return [
            {
                'match': self.EXPR_STMT,
                'required': False,
                'error': 'STATEMENT: EXPR_STMT faltante'
            },
            {
                'match': self.FOR_STMT,
                'required': False,
                'error': 'STATEMENT: FOR_STMT faltante'
            },
            {
                'match': self.IF_STMT,
                'required': False,
                'error': 'STATEMENT: IF_STMT faltante'
            },
            {
                'match': self.PRINT_STMT,
                'required': False,
                'error': 'STATEMENT: PRINT_STMT faltante'
            },
            {
                'match': self.RETURN_STMT,
                'required': False,
                'error': 'STATEMENT: RETURN_STMT faltante'
            },
            {
                'match': self.WHILE_STMT,
                'required': False,
                'error': 'STATEMENT: WHILE_STMT faltante'
            },
            {
                'match': self.BLOCK,
                'required': False,
                'error': 'STATEMENT: BLOCK faltante'
            },
        ]

    def EXPR_STMT(self):
        print("EXPR_STMT")
        return [
            {
                'match': self.EXPRESSION,
                'required': False,
                'error': 'EXPR_STMT: EXPRESSION faltante',
            }, {
                'match': ';',
                'required': False,
                'error': 'EXPR_STMT: ; faltante'
            }
        ]

    def FOR_STMT(self):
        print("FOR_STMT")
        return [
            {
                'match': 'for',
                'required': False,
                'error': 'FOR_STMT: for faltante',
                'next': [
                    {
                        'match': '(',
                        'required': True,
                        'error': 'FOR_STMT: ( faltante'
                    },
                    {
                        'match': self.FOR_STMT_1,
                        'required': True,
                        'error': 'FOR_STMT: FOR_STMT_1 faltante'
                    },
                    {
                        'match': self.FOR_STMT_2,
                        'required': True,
                        'error': 'FOR_STMT: FOR_STMT_2 faltante'
                    },
                    {
                        'match': self.FOR_STMT_3,
                        'required': False,
                        'error': 'FOR_STMT: FOR_STMT_3 faltante'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': 'FOR_STMT: ) faltante'
                    },
                    {
                        'match': self.STATEMENT,
                        'required': True,
                        'error': 'FOR_STMT: STATEMENT faltante'
                    },
                ]
            },
        ]

    def FOR_STMT_1(self):
        print("FOR_STMT_1")
        return [
            {
                'match': self.VAR_DECL,
                'required': False,
                'error': 'FOR_STMT_1: VAR_DECL faltante'
            },
            {
                'match': self.EXPRESSION,
                'required': False,
                'error': 'FOR_STMT_1: EXPRESSION faltante'
            },
    ]

    def FOR_STMT_2(self): 
        print("FOR_STMT_2")
        return [
            {
                'match': self.EXPRESSION,
                'required': False,
                'error': 'FOR_STMT_2: EXPRESSION faltante'
            },
            {
                'match': ';',
                'required': True,
                'error': 'FOR_STMT_2: ; faltante'
            },
        ]

    def FOR_STMT_3(self):
        print("FOR_STMT_3")
        return [
            {
                'match': self.EXPRESSION,
                'required': False,
                'error': 'FOR_STMT_3: EXPRESSION faltante'
            },
        ]

    def IF_STMT(self):
        print("IF_STMT")
        return [
            {
                'match': 'if',
                'required': False,
                'error': 'IF_STMT: if faltante',
                'next': [
                    {
                        'match': '(',
                        'required': True,
                        'error': 'IF_STMT: ( faltante'
                    },
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'IF_STMT: EXPRESSION faltante'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': 'IF_STMT: ) faltante'
                    },
                    {
                        'match': self.STATEMENT,
                        'required': True,
                        'error': 'IF_STMT: STATEMENT faltante'
                    },
                    {
                        'match': self.ELSE_STATEMENT,
                        'required': False,
                        'error': 'IF_STMT: ELSE_STATEMENT faltante'
                    },
                ]
            },  
        ]

    def ELSE_STATEMENT(self):
        print("ELSE_STATEMENT")
        return [
            {
                'match': 'else',
                'required': False,
                'next': [
                    {
                        'match': self.STATEMENT,
                        'required': True,
                        'error': 'ELSE_STATEMENT: STATEMENT faltante'
                    },
                ]
            },
        ]

    def PRINT_STMT(self):
        print("PRINT_STMT")
        return [
            {
                'match': 'print',
                'required': False,
                'error': 'PRINT_STMT: print faltante',
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'PRINT_STMT: EXPRESSION faltante'
                    },
                    {
                        'match': ';',
                        'required': True,
                        'error': 'PRINT_STMT: ; faltante'
                    },
                ]
            },
        ]

    def RETURN_STMT(self):
        print("RETURN_STMT")
        return [
            {
                'match': 'return',
                'required': False,
                'error': 'RETURN_STMT: return faltante',
                'next': [
                            {
                        'match': self.RETURN_EXP_OPC,
                        'required': False,
                        'error': 'RETURN_STMT: RETURN_EXP_OPC faltante'
                    },
                    {
                        'match': ';',
                        'required': True,
                        'error': 'RETURN_STMT: ; faltante'
                    },
                ]
            },
        ]

    def RETURN_EXP_OPC(self):
        print("RETURN_EXP_OPC")
        return [
            {
                'match': self.EXPRESSION,
                'required': False,
            },
        ]

    def WHILE_STMT(self):
        print("WHILE_STMT")
        return [
            {
                'match': 'while',
                'required': False,
                'error': 'WHILE_STMT: while faltante',
                'next': [
                    {
                        'match': '(',
                        'required': True,
                        'error': 'WHILE_STMT: ( faltante'
                    },
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'WHILE_STMT: EXPRESSION faltante'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': 'WHILE_STMT: ) faltante'
                    },
                    {
                        'match': self.STATEMENT,
                        'required': True,
                        'error': 'WHILE_STMT: STATEMENT faltante'
                    },
                ]
            },
            
        ]

    def BLOCK(self):
        print("BLOCK")
        return [
            {
                'match': '{',
                'required': False,
                'error': 'BLOCK: { faltante',
                'next': [
                    {
                        'match': self.BLOCK_DECL,
                        'required': True,
                        'error': 'BLOCK: BLOCK_DECL faltante'
                    },
                    {
                        'match': '}',
                        'required': True,
                        'error': 'BLOCK: } faltante'
                    },
                ]
            },
        ]

    def BLOCK_DECL(self):
        print("BLOCK_DECL")
        return [
            {
                'match': self.DECLARATION,
                'required': False,
                'looping': True
            },
        ]

    # EXPRESIONES
    def EXPRESSION(self):
        print("EXPRESSION")
        return [
            {
                'match': self.ASSIGNMENT,
                'required': False,
                'error': 'EXPRESSION: ASSIGNMENT faltante'
            }
        ]

    def ASSIGNMENT(self):
        print("ASSIGNMENT")
        return [
            {
                'match': self.LOGIC_OR,
                'required': False,
                'error': 'ASSIGNMENT: LOGIC_OR faltante'
            },
            {
                'match': self.ASSIGNMENT_OPC,
                'required': False,
                'error': 'ASSIGNMENT: ASSIGNMENT_OPC faltante'
            },
        ]

    def ASSIGNMENT_OPC(self):
        print("ASSIGNMENT_OPC")
        return [
            {
                'match': '=',
                'required': False,
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'ASSIGNMENT_OPC: EXPRESSION faltante'
                    },
                ]
            },
        ]

    def LOGIC_OR(self):
        print("LOGIC_OR")
        return [
            {
                'match': self.LOGIC_AND,
                'required': False,
                'error': 'LOGIC_OR: LOGIC_AND faltante'
            }, {
                'match': self.LOGIC_OR_2,
                'required': False,
                'error': 'LOGIC_OR: LOGIC_OR_2 faltante'
            } 
        ]

    def LOGIC_OR_2(self):
        print("LOGIC_OR_2")
        return [
            {
                'match': 'or',
                'required': False,
                'next': [
                    {
                        'match': self.LOGIC_AND,
                        'required': True,
                        'error': 'LOGIC_OR_2: LOGIC_AND faltante'
                    },
                    {
                        'match': self.LOGIC_OR_2,
                        'required': True,
                        'error': 'LOGIC_OR_2: LOGIC_OR_2 faltante'
                    },
                ]
            },
        ]

    def LOGIC_AND(self):
        print("LOGIC_AND")
        return [
            {
                'match': self.EQUALITY,
                'required': False,
                'error': 'LOGIC_AND: EQUALITY faltante',
            }, {
                'match': self.LOGIC_AND_2,
                'required': False,
                'error': 'LOGIC_AND: LOGIC_AND_2 faltante'
            }
        ]

    def LOGIC_AND_2(self):
        print("LOGIC_AND_2")
        return [
            {
                'match': 'and',
                'required': False,
                'next': [
                    {
                        'match': self.EQUALITY,
                        'required': True,
                        'error': 'LOGIC_AND_2: EQUALITY faltante'
                    },
                    {
                        'match': self.LOGIC_AND_2,
                        'required': True,
                        'error': 'LOGIC_AND_2: LOGIC_AND_2 faltante'
                    },
                ]
            },
        ]

    def EQUALITY(self):
        print("EQUALITY")
        return [
            {
                'match': self.COMPARISON,
                'required': False,
                'error': 'EQUALITY: COMPARISON faltante'
            },
            {
                'match': self.EQUALITY_2,
                'required': False,
                'error': 'EQUALITY: EQUALITY_2 faltante'
            },
        ]

    def EQUALITY_2(self):
        print("EQUALITY_2")
        return [
            {
                'match': '!=',
                'required': False,
                'next': [
                    {
                        'match': self.COMPARISON,
                        'required': True,
                        'error': 'EQUALITY_2: COMPARISON faltante'
                    },
                ]
            },
            {
                'match': '==',
                'required': False,
                'next': [
                    {
                        'match': self.COMPARISON,
                        'required': True,
                        'error': 'EQUALITY_2: COMPARISON faltante'
                    },
                ]
            },
        ]

    def COMPARISON(self):
        print("COMPARISON")
        return [
            {
                'match': self.TERM,
                'required': False,
                'error': 'COMPARISON: TERM faltante',
            }, {
                'match': self.COMPARISON_2,
                'required': False,
                'looping': True,
                'error': 'COMPARISON: COMPARISON_2 faltante'
            }
        ]
    def COMPARISON_2(self):
        print("COMPARISON_2")
        return [
            {
                'match': '>',
                'required': False,
                'next': [
                    {
                        'match': self.TERM,
                        'required': True,
                        'error': 'COMPARISON_2: TERM faltante'
                    },
                ]
            },
            {
                'match': '>=',
                'required': False,
                'next': [
                    {
                        'match': self.TERM,
                        'required': True,
                        'error': 'COMPARISON_2: TERM faltante'
                    },
                ]
            },
            {
                'match': '<',
                'required': False,
                'next': [
                    {
                        'match': self.TERM,
                        'required': True,
                        'error': 'COMPARISON_2: TERM faltante'
                    },
                ]
            },
            {
                'match': '<=',
                'required': False,
                'next': [
                    {
                        'match': self.TERM,
                        'required': True,
                        'error': 'COMPARISON_2: TERM faltante'
                    },
                ]
            },
        ]

    def TERM(self):
        print("TERM")
        return [
            {
                'match': self.FACTOR,
                'required': False,
                'error': 'TERM: FACTOR faltante',
            },{
                'match': self.TERM_2,
                'required': False,
                'error': 'TERM: TERM_2 faltante',
                'looping': True
            }
        ]

    def TERM_2(self):
        print("TERM_2")
        return [
            {
                'match': '-',
                'required': False,
                'next': [
                    {
                        'match': self.FACTOR,
                        'required': True,
                        'error': 'TERM_2: FACTOR faltante'
                    },
                ]
            },
            {
                'match': '+',
                'required': False,
                'next': [
                    {
                        'match': self.FACTOR,
                        'required': True,
                        'error': 'TERM_2: FACTOR faltante'
                    },
                ]
            },
        ]

    def FACTOR(self):
        print("FACTOR")
        return [
            {
                'match': self.UNARY,
                'required': False,
                'error': 'FACTOR: UNARY faltante'
            },
            {
                'match': self.FACTOR_2,
                'required': False,
                'error': 'FACTOR: FACTOR_2 faltante'
            },
        ]

    def FACTOR_2(self):
        print("FACTOR_2")
        return [
            {
                'match': '/',
                'required': False,
                'next': [
                    {
                        'match': self.UNARY,
                        'required': True,
                        'error': 'FACTOR_2: UNARY faltante'
                    },
                    {
                        'match': self.FACTOR_2,
                        'required': True,
                        'error': 'FACTOR_2: FACTOR_2 faltante'
                    },
                ]
            },
            {
                'match': '*',
                'required': False,
                'next': [
                    {
                        'match': self.UNARY,
                        'required': True,
                        'error': 'FACTOR_2: UNARY faltante'
                    },
                    {
                        'match': self.FACTOR_2,
                        'required': True,
                        'error': 'FACTOR_2: FACTOR_2 faltante'
                    },
                ]
            },
        ]

    def UNARY(self):
        print("UNARY")
        return [
            {
                'match': '!',
                'required': False,
                'next': [
                    {
                        'match': self.UNARY,
                        'required': True,
                        'error': 'UNARY: UNARY faltante'
                    }
                ]
            }, {
                'match': '-',
                'required': False,
                'next': [
                    {
                        'match': self.UNARY,
                        'required': True,
                        'error': 'UNARY: UNARY faltante'
                    }
                ]
            }, {
                'match': self.CALL,
                'required': False,
                'error': 'UNARY: CALL faltante'
            },
        ]

    def CALL(self):
        print("CALL")
        return [
            {
                'match': self.PRIMARY,
                'required': False,
                'error': 'CALL: PRIMARY faltante'
            },
            {
                'match': self.CALL_2,
                'required': False,
                'error': 'CALL: CALL_2 faltante'
            },
        ]

    def CALL_2(self):
        print("CALL_2")
        return [
            {
                'match': '(',
                'required': False,
                'next': [
                    {
                        'match': self.ARGUMENTS_OPC,
                        'required': False,
                        'error': 'CALL_2: ARGUMENTS_OPC faltante'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': 'CALL_2: ) faltante'
                    },
                    {
                        'match': self.CALL_2,
                        'required': False,
                        'error': 'CALL_2: CALL_2 faltante'
                    },
                ]
            },{
                'match': '.',
                'required': False,
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'CALL_2: id faltante'
                    },{
                        'match': self.CALL_2,
                        'required': False,
                        'error': 'CALL_2: CALL_2 faltante'
                    },
                ]
            }
        ]

    def PRIMARY(self):
        print("PRIMARY")
        return [
            {
                'match': 'true',
                'required': False,
            },
            {
                'match': 'false',
                'required': False,
            },
            {
                'match': 'null',
                'required': False,
            },
            {
                'match': 'this',
                'required': False,
            },
            {
                'match': Numero,
                'required': False,
            },
            {
                'match': Cadena,
                'required': False,
            },
            {
                'match': Identificador,
                'required': False,
            },
            {
                'match': '(',
                'required': False,
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': False,
                        'error': 'PRIMARY: EXPRESSION faltante'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': 'PRIMARY: ) faltante'
                    },
                ]
            },
            {
                'match': 'super',
                'required': False,
                'next': [
                    {
                        'match': '.',
                        'required': True,
                        'error': 'PRIMARY: . faltante'
                    },
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'PRIMARY: id faltante'
                    },
                ]
            },
        ]

    # OTRAS
    def FUNCTION(self):
        print("FUNCTION")
        return [
            {
                'match': Identificador,
                'required': False,
                'error': 'FUNCTION: id faltante',
                'next': [
                    {
                        'match': '(',
                        'required': True,
                        'error': 'FUNCTION: ( faltante'
                    },
                    {
                        'match': self.PARAMETER_OPC,
                        'required': False,
                        'error': 'FUNCTION: PARAMETER_OPC faltante'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': 'FUNCTION: ) faltante'
                    },
                    {
                        'match': self.BLOCK,
                        'required': True,
                        'error': 'FUNCTION: BLOCK faltante'
                    },       
                ]
            }
        ]

    def FUNCTIONS(self):
        print("FUNCTIONS")
        return [
            {
                'match': self.FUNCTION,
                'required': False,
                'looping': True
            }
        ]

    def PARAMETER_OPC(self):
        print("PARAMETER_OPC")
        return [
            {
                'match': self.PARAMETERS,
                'required': False,
            },
        ]

    def PARAMETERS(self):
        print("PARAMETERS")
        return [
            {
                'match': Identificador,
                'required': False,
                'error': 'PARAMETERS: id faltante',
                'next': [
                    {
                        'match': self.PARAMETERS_2,
                        'required': True,
                        'error': 'PARAMETERS: PARAMETERS_2 faltante'
                    }       
                ]
            }
        ]

    def PARAMETERS_2(self):
        print("PARAMETERS_2")
        return [
            {
                'match': ',',
                'required': False,
                'looping': True,
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'PARAMETERS_2: id faltante'
                    }
                ]
            },
        ]

    def ARGUMENTS_OPC(self):
        print("ARGUMENTS_OPC")
        return [
            {
                'match': self.ARGUMENTS,
                'required': False,
            },
        ]

    def ARGUMENTS(self):
        print("ARGUMENTS")
        return [
            {
                'match': self.EXPRESSION,
                'required': False,
                'error': 'ARGUMENTS: EXPRESSION faltante',
                'next': [
                    {
                        'match': self.ARGUMENTS_2,
                        'required': False,
                        'error': 'ARGUMENTS: ARGUMENTS_2 faltante'
                    },
                ]
            },
        ]

    def ARGUMENTS_2(self):
        print("ARGUMENTS_2")
        return [
            {
                'match': ',',
                'required': False,
                'looping': True,
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'ARGUMENTS_2: EXPRESSION faltante'
                    }
                ]
            },
        ]