from enum import Enum

class OPERACION_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    MULTI = 3
    DIVIDIDO = 4
    RESIDUO = 5

class OPERACION_LOGICA(Enum) :
    AND = 1
    OR = 2
    XOR = 3

class OPERACION_RELACIONAL(Enum) :
    IGUALQUE = 1
    DISTINTO = 2
    MAYORIGUAL = 3
    MENORIGUAL = 4
    MAYORQUE = 5
    MENORQUE = 6

class OPERACION_BIT_A_BIT(Enum) :
    AND = 1
    OR = 2
    XOR = 3
    SHIFT_IZQ = 4
    SHIFT_DER = 5
    
class TIPO_VARIABLE(Enum) :
    TEMPORAL = 1 
    PARAMETRO = 2
    VALOR_DEV_FUN = 3
    RA = 4
    STACK = 5
    SP = 6

class TIPO_DATO(Enum) :
    ENTERO = 1
    FLOTANTE = 2
    CADENA = 3
    ARREGLO = 4
    CHAR = 5

class FUNCION_NATIVA(Enum):
    ABS = 1
    CBRT = 2
    CEIL = 3
    CEILING = 4
    DEGREES = 5
    DIV = 6
    EXP = 7
    FACTORIAL = 8
    FLOOR = 9

#------------------------------------------------------------------------

class Casteo() :
    def __init__(self,tipo_dato,variable) :
        self.tipo_dato = tipo_dato
        self.variable = variable

#------------------------------------------------------------------------

class UnitariaNegAritmetica() :
    def __init__(self, exp) :
        self.exp = exp

class UnitariaLogicaNOT() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnitariaNotBB() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnariaReferencia() :
    def __init__(self,tipoVar):
        self.tipoVar=tipoVar

#------------------------------------------------------------------------

class Expresion:
    '''Clase abstracta'''

class Parametro(Expresion) :
    def __init__(self, expresion) :
        self.expresion=expresion

class Variable(Expresion) :
    
    def __init__(self, id, tipoVar) :
        self.id=id
        self.tipoVar=tipoVar

class ExpresionValor(Expresion) :
    def __init__(self, val = 0) :
        self.val = val

class AccesoArray(Expresion) :
    def __init__(self,tipoVar,params=[]) :
        self.tipoVar=tipoVar
        self.params=params
#------------------------------------------------------

class ExpresionAritmetica(Expresion) :
   
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

#------------------------------------------------------

class ExpresionLogica(Expresion) :
    
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

#------------------------------------------------------
class ExpresionRelacional(Expresion) :

    def __init__(self,exp1,exp2,operador) :
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

#------------------------------------------------------
class ExpresionBitABit(Expresion) :

    def __init__(self,exp1,exp2,operador) :
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

# ------------------------------------------------------
class valorTipo(Expresion):
    def __init__(self, valor, expresion):
        self.valor = valor
        self.expresion = expresion


# --------------------------------------------------------
class CampoTabla(Expresion):
    def __init__(self, id, tipo, validaciones):
        self.id = id
        self.tipo = tipo

        self.validaciones = validaciones

#---------------------------------------------------------
class CampoValidacion(Expresion):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor


#-----------------------------------------------------------
class ExpresionFuncion(Expresion):
    def __init__(self, funcion, exp1, exp2, exp3, exp4):
        self.funcion = funcion
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4