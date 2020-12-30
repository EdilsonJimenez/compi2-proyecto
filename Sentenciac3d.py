from Instruccion_pl import *
from Temporales import *
from expresiones import *
from sentencias import *
import Temporales as T
t_global = T.Temporales()
cadena = ""
class Codigo3d:

    def __init__(self):
        self.i = 0

    def Traducir(self, instrucciones):
        global ts_global
        for i in instrucciones:
            if isinstance(i, If_inst):
                self.t_If(i)
            elif isinstance(i, Declaracion):
                self.t_Declaracion(i)
            else:
                print("NO TRADUCE....")

        print(cadena)

    def t_If(self, instancia):
        print("Se traduce el if")
        global t_global, cadena

        condicion = self.procesar_expresion(instancia.condicion, t_global)
        verdadero = str(t_global.etiquetaT())
        falso = str(t_global.etiquetaT())
        salto = str(t_global.etiquetaT())

        cadena += "if " + str(condicion) + ": \n"
        cadena += "\tgoto ."+verdadero+"\n"
        cadena += "else : \n"
        cadena += "\tgoto ."+falso+"\n"

        cadena += "label . " + verdadero + "\n"
        cadena += "print(\"Codigo si es Verdadero\")"+"\n"
        # Si el if trae instruciones en IF
        if instancia.instIf != 0:
            cadena += "Trae Instrucciones If"
        cadena += "goto ."+salto+"\n"+"\n"

        cadena += "label ." + falso + "\n"
        cadena += "print(\"Codigo si es Falso\")"+"\n"
        # Si el if trae instruciones en ELSE
        if instancia.instElse != None:
            if instancia.instElse != 0:
                print("Trae Instrucciones Else")
        cadena += "label ."+salto+"\n"

    def t_Declaracion(self, instancia):
        global t_global, cadena


    # EXPRESIONES
    def procesar_expresion(self, expresiones, ts):
        if isinstance(expresiones, ExpresionAritmetica):
            return self.procesar_aritmetica(expresiones, ts)
        elif isinstance(expresiones, ExpresionRelacional):
            return self.procesar_relacional(expresiones, ts)
        elif isinstance(expresiones, ExpresionLogica):
            return self.procesar_logica(expresiones, ts)
        elif isinstance(expresiones, UnitariaNegAritmetica):
            return procesar_negAritmetica(expresiones, ts)
        elif isinstance(expresiones, UnitariaLogicaNOT):
            return procesar_logicaNOT(expresiones, ts)
        elif isinstance(expresiones, UnitariaNotBB):
            return procesar_NotBB(expresiones, ts)
        elif isinstance(expresiones, ExpresionValor):
            return expresiones.val
        elif isinstance(expresiones, Variable):
            return self.procesar_variable(expresiones, ts)
        elif isinstance(expresiones, UnitariaAritmetica):
            return procesar_unitaria_aritmetica(expresiones, ts)
        elif isinstance(expresiones, ExpresionFuncion):
            return procesar_funcion(expresiones, ts)
        elif isinstance(expresiones, ExpresionTiempo):
            return procesar_unidad_tiempo(expresiones, ts)
        elif isinstance(expresiones, ExpresionConstante):
            return procesar_constante(expresiones, ts)
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
            print(expresiones)
            print('Error:Expresion no reconocida')

    def procesar_aritmetica(self, expresion, ts):
        global cadena
        val = self.procesar_expresion(expresion.exp1, ts)
        val2 = self.procesar_expresion(expresion.exp2, ts)

        if expresion.operador == OPERACION_ARITMETICA.MAS:
            v = t_global.varTemporal()
            cadena += v + "= "+str(val)+" + "+str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_ARITMETICA.MENOS:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " - " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_ARITMETICA.MULTI:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " * " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " / " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_ARITMETICA.RESIDUO:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " / " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_ARITMETICA.POTENCIA:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " ** " + str(val2) + "\n"
            return v

    def procesar_relacional(self, expresion, ts):
        # OPTIMIZACION - AHORRO DE 2 LINEAS........................................................
        global cadena
        val = self.procesar_expresion(expresion.exp1, ts)
        val2 = self.procesar_expresion(expresion.exp2, ts)
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " == " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " != " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " >= " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " <= " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " > " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " < " + str(val2) + "\n"
            return v
        else:
            return 1

    def procesar_logica(self, expresion, ts):
        global cadena
        val = self.procesar_expresion(expresion.exp1, ts)
        val2 = self.procesar_expresion(expresion.exp2, ts)

        if expresion.operador == OPERACION_LOGICA.AND:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " and " + str(val2) + "\n"
            return v
        elif expresion.operador == OPERACION_LOGICA.OR:
            v = t_global.varTemporal()
            cadena += v + "= " + str(val) + " or " + str(val2) + "\n"
            return v

    def procesar_variable(tV, ts):
        global ListaTablasG, baseN
        listaRes = []
        for item in ts.Datos:
            v: DatoInsert = ts.obtenerDato(item)
            if str(v.columna) == str(tV.id) and str(v.bd) == str(baseN[0]) and str(v.tabla) == str(ListaTablasG[0]):
                print(" <> En listar: " + str(v.valor))
                listaRes.append(v)
        print(" <><>")
        if listaRes.__len__() == 0:
            print(" >>> No hay datos para esta validación.")
            return None
        else:
            return listaRes
