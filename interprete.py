from Instruccion import *
from graphviz import Graph
from graphviz import escape
from expresiones import *
from Ast2 import *
from six import string_types
import ts as TS
from errores import *
import Gramatica as g
import jsonMode as Master
##------------------------------------------
# TABLA DE SIMBOLOS GLOBAL
ts_global = TS.TablaDeSimbolos()
# TABLA DE ERRORES GLOBAL
LisErr = TablaError([])
# ===========================
instrucciones = []
editor = None
consola = None
content = ''


# INICIALIZACION DE MAIN==============================================
# ========================================================================
def limpiarValores():
    global ts_global, instrucciones, indice, tag, LisErr
    ts_global = TS.TablaDeSimbolos
    instrucciones = []
    indice = 0
    tag = ''
    LisErr = TablaError([])


def inicializarEjecucionAscendente(contenido):
    global LisErr, instrucciones, ts_global
    ts_global = TS.TablaDeSimbolos()
    instrucciones = g.parse(contenido, LisErr)
   # reporte_errores()


def inicializarTS():
    global instrucciones, ts_global, tag
    # save_main('main',ts_global,1)
    # fill_tags(instrucciones,ts_global)
    # consola.insert('end',"\n>> ********  Start  ******** \n>>")
    # tag='main'
    # if not comprobarMain(instrucciones):
    # consola.insert('end',">>Error: Verifique errores lexicos y sintacticos\n>>")


# ========================================================================
# ========================================================================

# EJECUTANDO EXPRESIONES============================
# VERIFICANDO QUE TIPO DE EXPRESION ES
def procesar_expresion(expresiones, ts):
    if isinstance(expresiones, ExpresionAritmetica):
        return procesar_aritmetica(expresiones, ts)
    elif isinstance(expresiones, ExpresionRelacional):
        return procesar_relacional(expresiones, ts)
    elif isinstance(expresiones, ExpresionLogica):
        return procesar_logica(expresiones, ts)
    elif isinstance(expresiones, UnitariaNegAritmetica):
        return procesar_negAritmetica(expresiones, ts)
    elif isinstance(expresiones, UnitariaLogicaNOT):
        return procesar_logicaNOT(expresiones, ts)
    elif isinstance(expresiones, UnitariaNotBB):
        return procesar_NotBB(expresiones, ts)
    elif isinstance(expresiones, ExpresionValor):
        return expresiones.val
    elif isinstance(expresiones, Variable):
        return procesar_variable(expresiones, ts)
    elif isinstance(expresiones, Absoluto):
        try:
            return procesar_expresion(expresiones.variable, ts)
        # return abs(procesar_expresion(expresiones.variable,ts))
        except:
            print('Error no se puede aplicar abs() por el tipo de dato')
            # consola.insert('end','>>Error: No se puede aplicar abs() al tipo de dato\n>>')
            # newErr=ErrorRep('Semantico','No se puede aplicar abs() al tipo de dato ',indice)
            # LisErr.agregar(newErr)
            return None
    else:
        print('Error:Expresion no reconocida')


def procesar_aritmetica(expresion, ts):
    val = procesar_expresion(expresion.exp1, ts)
    val2 = procesar_expresion(expresion.exp2, ts)
    if expresion.operador == OPERACION_ARITMETICA.MAS:
        if isinstance(val, string_types) and isinstance(val2, string_types):
            return val + val2
        elif ((isinstance(val, int) or isinstance(val, float))
              and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val + val2
        else:
            # consola.insert('end','>>Error: tipos no pueden sumarse \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden sumarse ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.MENOS:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val - val2
        else:
            # consola.insert('end','>>Error: tipos no pueden restarse \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden restarse ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.MULTI:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val * val2
        else:
            # consola.insert('end','>>Error: tipos no pueden multiplicarse \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden multiplicarse ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
        if val2 == 0:
            print('Error: No se puede dividir entre 0')
            # consola.insert('end','>>Error: No se puede dividir entre cero'+str(val)+' '+str(val2)+'\n>>')
            # newErr=ErrorRep('Semantico','No se puede dividir entre cero '+str(val)+' '+str(val2),indice)
            # LisErr.agregar(newErr)
            return None
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val / val2
        else:
            print('Error: Tipos no pueden dividirse')
            # consola.insert('end','>>Error: tipos no pueden dividires \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden dividirse ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.RESIDUO:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val % val2
        else:
            print('Error: Tipos no pueden operarse %')
            # consola.insert('end','>>Error: tipos no pueden operarse por residuo \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden operarse por residuo ',indice)
            # LisErr.agregar(newErr)
            return None


def procesar_relacional(expresion, ts):
    val = procesar_expresion(expresion.exp1, ts)
    val2 = procesar_expresion(expresion.exp2, ts)

    if (isinstance(val, int) and isinstance(val2, float)
            or isinstance(val, float) and isinstance(val2, int)
            or isinstance(val, float) and isinstance(val2, float)
            or isinstance(val, int) and isinstance(val2, int)):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            return 1 if (val == val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            return 1 if (val != val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            return 1 if (val >= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            return 1 if (val <= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            return 1 if (val > val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            return 1 if (val < val2) else 0
    elif isinstance(val, string_types) and isinstance(val2, string_types):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            return 1 if (val == val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            return 1 if (val != val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            return 1 if (val >= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            return 1 if (val <= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            return 1 if (val > val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            return 1 if (val < val2) else 0
    else:
        print('Error: Expresion relacional con tipos incompatibls')
        # consola.insert('end','>>Error: Expresion relacional con tipos incompatibles'+str(expresion.operador)+'\n>>')
        # newErr=ErrorRep('Semantico','Expresion relacional con tipos incompatibles '+str(expresion.operador),indice)
        # LisErr.agregar(newErr)
        return None


def procesar_logica(expresion, ts):
    val = procesar_expresion(expresion.exp1, ts)
    val2 = procesar_expresion(expresion.exp2, ts)

    if ((isinstance(val, int) or isinstance(val, float))
            and ((isinstance(val2, int) or isinstance(val2, float)))):
        if expresion.operador == OPERACION_LOGICA.AND:
            return 1 if (val and val2) else 0
        elif expresion.operador == OPERACION_LOGICA.OR:
            return 1 if (val or val2) else 0
        elif expresion.operador == OPERACION_LOGICA.XOR:
            return 1 if (val ^ val2) else 0

    else:
        print('Error: No se puede realizar la op. logica')
        # consola.insert('end','>>Error: Expresion logica con tipos incompatibles'+str(expresion.operador)+'\n>>')
        # newErr=ErrorRep('Semantico','Expresion logica con tipos incompatibles '+str(expresion.operador),indice)
        # LisErr.agregar(newErr)


def procesar_negAritmetica(expresion, ts):
    try:
        return -1 * procesar_expresion(expresion.exp, ts)
    except:
        print('Error:tipo de dato no se puede multiplicar por -1')
        # consola.insert('end','>>Error: No se pudo realizar la neg aritmetica\n>>')
        # newErr=ErrorRep('Semantico','No se pudo realizar la neg aritmetica ',indice)
        # LisErr.agregar(newErr)
        return None


def procesar_logicaNOT(instr, ts):
    try:
        val = procesar_expresion(instr.expresion, ts)
        return 0 if (val == 1) else 1
    except:
        print('Error no se puede aplicar Neg Logica')
        # consola.insert('end','>>Error: No se puede aplicar Neg Logica\n>>')
        # newErr=ErrorRep('Semantico','No se puede aplicar Neg Logica ',indice)
        # LisErr.agregar(newErr)
        return None


def procesar_NotBB(instr, ts):
    try:
        val = procesar_expresion(instr.expresion, ts)
        if isinstance(val, int):
            binario = ~int(val)
            return int(binario)
        else:
            print('Error: no compatible para aplicar neg binario')
            # consola.insert('end','>>Error: No compatible para aplicar neg binario\n>>')
            # newErr=ErrorRep('Semantico','No compatible para aplicar neg binario ',indice)
        # LisErr.agregar(newErr)
        return None
    except:
        print('Error no compatible para aplicar neg binario')
        # consola.insert('end','>>Error: No compatible para aplicar neg binario\n>>')
        # newErr=ErrorRep('Semantico','No compatible para aplicar neg binario ',indice)
        # LisErr.agregar(newErr)
        return None


def procesar_variable(tipoVar, ts):
    val = ts.obtener(tipoVar.id)
    if val is None:
        print('Error: Variable no declarada')
        # consola.insert('end','>>Error: Variable no declarada '+str(tipoVar.id)+'\n>>')
        # newErr=ErrorRep('Semantico','Variable no declarada: '+str(tipoVar.id),indice)
        # LisErr.agregar(newErr)
        return None
    if val.tipo == TS.TIPO_DATO.ARREGLO:
        # consola.insert('end','>>Error: No se pueden imprimir arreglos '+str(tipoVar.id)+'\n>>')
        # newErr=ErrorRep('Semantico','No se pueden imprimir arreglos: '+str(tipoVar.id),indice)
        # LisErr.agregar(newErr)
        print('Error: No se pueden imprimir arreglos')
        return None
    return val.valor


# -------------------------------------------------------------------------------------------------
# --------------------------------- EJECUCION -----------------------------------------------------

from Instruccion import *
from expresiones import *


class interprete2:

    def __init__(self, sentencias):
        self.i = 0
        self.sentencias = sentencias

    def inc(self):
        global i
        self.i += 1

    def ejecucion(self):
        self.recorrerInstrucciones(self.sentencias)

    def recorrerInstrucciones(self, sente):
        global ts_global
        for i in sente:
            if isinstance(i, CreateDataBase):
                i.Ejecutar()
            elif isinstance(i, ShowDatabases):
                i.Ejecutar()
            elif isinstance(i, AlterDataBase):
                i.Ejecutar()
            elif isinstance(i, DropDataBase):
                i.Ejecutar()
            elif isinstance(i, CreateTable):
                i.Ejecutar()
            elif isinstance(i, Insert_Datos):
                i.Ejecutar()
            else:
                print("NO ejecuta")

'''
    def i_CreateDataBase(self, DataBase: CreateDataBase):
        global ts_global
        r = ts_global.obtenerCreateDateBase(DataBase.idBase)
        if r == None:
            print("No encontre la base de datos.")
            rM = Master.createDatabase(str(DataBase.idBase))
            if rM == 0:
                print("> Base de datos creada con exito!")
            elif rM == 1 or rM == 2:
                print("> Base de datos con conflicto.")
        else:
            print("Si encontre la base de datos.")
            for i in ts_global.createDataBase:
                x:CreateDataBase = ts_global.obtenerCreateDateBase(i)
                print(x.Modo)'''


#REPORTE DE ERRORES..................
def reporte_errores():
    print("ejecutando errores...........")
    Rep = Graph('g', filename='berrores.gv', format='png',node_attr={'shape': 'plaintext', 'height': '.1'})
    cadena=''
    i=1
    for item in LisErr.errores:
        cadena+='<TR><TD>'+str(i)+'</TD><TD>'+str(item.tipo)+'</TD>'+'<TD>'+str(item.descripcion)+'</TD>'+'<TD>'+str(item.linea)+'</TD></TR>'
        i+=1
    Rep.node('structs','''<<TABLE> <TR> <TD>Numero</TD><TD>Tipo-Clase Error</TD><TD>Descripcion Error</TD><TD>Linea</TD></TR>'''+cadena+'</TABLE>>')
    Rep.render('g', format='png', view=True)
    print('Hecho')




