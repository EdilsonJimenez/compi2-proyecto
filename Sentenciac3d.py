from Instruccion_pl import *
from Temporales import *
from expresiones import *
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
                self.transIf(i)
            else:
                print("NO TRADUCE....")

    def transIf(self, instancia):
        print("Se traduce el if")
        global t_global, cadena

        condicion = self.procesar_expresion(instancia.condicion, t_global)
        verdadero = str(t_global.etiquetaT())
        falso = str(t_global.etiquetaT())
        salto = str(t_global.etiquetaT())

        cadena += "if" + str(condicion) + ": \n"
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

        print(cadena)

    # EXPRESIONES
    def procesar_expresion(self, expresiones, ts):
        if isinstance(expresiones, ExpresionAritmetica):
            self.procesar_aritmetica(expresiones, ts)
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

    def procesar_aritmetica(self,expresion, ts):
        global LisErr
        val = procesar_expresion(expresion.exp1, ts)
        val2 = procesar_expresion(expresion.exp2, ts)

        if expresion.operador == OPERACION_ARITMETICA.MAS:
            if ((isinstance(val, int) or isinstance(val, float))
                    and ((isinstance(val2, int) or isinstance(val2, float)))):
                v = t_global.varTemporal();
                cadena += v + "="+str(val)+"+"+val2
                return val + val2
            else:
                agregarErrorDatosOperacion(val, val2, "+", "numerico", 0, 0)
                return None
        elif expresion.operador == OPERACION_ARITMETICA.MENOS:
            if ((isinstance(val, int) or isinstance(val, float))
                    and ((isinstance(val2, int) or isinstance(val2, float)))):
                return val - val2
            else:
                agregarErrorDatosOperacion(val, val2, "-", "numerico", 0, 0)
                return None
        elif expresion.operador == OPERACION_ARITMETICA.MULTI:
            if ((isinstance(val, int) or isinstance(val, float))
                    and ((isinstance(val2, int) or isinstance(val2, float)))):
                return val * val2
            else:
                agregarErrorDatosOperacion(val, val2, "*", "numerico", 0, 0)
                return None
        elif expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
            if val2 == 0:
                agregarErrorDatosOperacion(val, val2, "/", "numerico diferente de 0 en el segundo parametro", 0, 0)
                return None
            if ((isinstance(val, int) or isinstance(val, float))
                    and ((isinstance(val2, int) or isinstance(val2, float)))):
                return val / val2
            else:
                agregarErrorDatosOperacion(val, val2, "/", "numerico", 0, 0)
                return None
        elif expresion.operador == OPERACION_ARITMETICA.RESIDUO:
            if ((isinstance(val, int) or isinstance(val, float))
                    and ((isinstance(val2, int) or isinstance(val2, float)))):
                return val % val2
            else:
                agregarErrorDatosOperacion(val, val2, "/", "numerico", 0, 0)
                return None
        elif expresion.operador == OPERACION_ARITMETICA.POTENCIA:
            if ((isinstance(val, int) or isinstance(val, float))
                    and ((isinstance(val2, int) or isinstance(val2, float)))):
                return pow(val, val2)
            else:
                agregarErrorDatosOperacion(val, val2, "%", "numerico", 0, 0)
                return None
        elif expresion.operador == OPERACION_BIT_A_BIT.AND:
            if isinstance(val, int) and isinstance(val2, int):
                return val & val2
            else:
                agregarErrorDatosOperacion(val, val2, "&", "entero", 0, 0)
                return None
        elif expresion.operador == OPERACION_BIT_A_BIT.OR:
            if isinstance(val, int) and isinstance(val2, int):
                return val | val2
            else:
                agregarErrorDatosOperacion(val, val2, "|", "entero", 0, 0)
                return None
        elif expresion.operador == OPERACION_BIT_A_BIT.XOR:
            if isinstance(val, int) and isinstance(val2, int):
                return val ^ val2
            else:
                agregarErrorDatosOperacion(val, val2, "#", "entero", 0, 0)
                return None
        elif expresion.operador == OPERACION_BIT_A_BIT.SHIFT_DER:
            if isinstance(val, int) and isinstance(val2, int):
                return val >> val2
            else:
                agregarErrorDatosOperacion(val, val2, ">>", "entero", 0, 0)
                return None
        elif expresion.operador == OPERACION_BIT_A_BIT.SHIFT_IZQ:
            if isinstance(val, int) and isinstance(val2, int):
                return val << val2
            else:
                agregarErrorDatosOperacion(val, val2, "<<", "entero", 0, 0)
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
        elif (isinstance(val[0], DatoInsert) and isinstance(val2, int)
              or isinstance(val[0], DatoInsert) and isinstance(val2, int)
              or isinstance(val[0], DatoInsert) and isinstance(val2, float)
              or isinstance(val[0], DatoInsert) and isinstance(val2, int)):

            if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if int(Vd.valor) == val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if int(Vd.valor) != val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if int(Vd.valor) >= val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if int(Vd.valor) <= val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if int(Vd.valor) > val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if int(Vd.valor) < val2:
                        listaV.append(Vd)
                return listaV
        elif isinstance(val[0], DatoInsert) and isinstance(val2, string_types):
            if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if str(Vd.valor) == val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if str(Vd.valor) != val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if str(Vd.valor) >= val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if str(Vd.valor) <= val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if str(Vd.valor) > val2:
                        listaV.append(Vd)
                return listaV
            elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
                listaV = []
                for v in val:
                    Vd: DatoInsert = v
                    if str(Vd.valor) < val2:
                        listaV.append(Vd)
                return listaV
        else:
            print('Error: Expresion relacional con tipos incompatibls')
            # consola.insert('end','>>Error: Expresion relacional con tipos incompatibles'+str(expresion.operador)+'\n>>')
            # newErr=ErrorRep('Semantico','Expresion relacional con tipos incompatibles '+str(expresion.operador),indice)
            # LisErr.agregar(newErr)
            return None

    def procesar_logica(expresion, ts):
        print("Logica en LOGICA")
        val = procesar_expresion(expresion.exp1, ts)
        val2 = procesar_expresion(expresion.exp2, ts)

        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            if expresion.operador == OPERACION_LOGICA.AND:
                return 1 if (val and val2) else 0
            elif expresion.operador == OPERACION_LOGICA.OR:
                return 1 if (val or val2) else 0
            elif expresion.operador == OPERACION_LOGICA.IS_DISTINCT:
                return 1 if (val != val2) else 0
            elif expresion.operador == OPERACION_LOGICA.IS_NOT_DISTINCT:
                return 1 if (val == val2) else 0
        elif (isinstance(val[0], DatoInsert) and isinstance(val2[0], DatoInsert)):
            if expresion.operador == OPERACION_LOGICA.OR:
                print("Logica en OR")
                listaP = []
                for v in val:
                    vv: DatoInsert = v
                    listaP.append(vv)
                for v2 in val2:
                    vv2: DatoInsert = v2
                    listaP.append(vv2)
                return listaP

            elif expresion.operador == OPERACION_LOGICA.AND:
                listaP = []
                for v in val:
                    vv: DatoInsert = v
                    for v2 in val2:
                        vv2: DatoInsert = v2
                        if vv2.fila == vv.fila:
                            listaP.append(vv2)

                return listaP

            elif expresion.operador == OPERACION_LOGICA.IS_DISTINCT:
                listaP = []
                for v in val:
                    vv: DatoInsert = v
                    for v2 in val2:
                        vv2: DatoInsert = v2
                        if vv2.fila != vv.fila:
                            listaP.append(vv2)

                return listaP

            elif expresion.operador == OPERACION_LOGICA.IS_NOT_DISTINCT:
                listaP = []
                for v in val:
                    vv: DatoInsert = v
                    for v2 in val2:
                        vv2: DatoInsert = v2
                        if vv2.fila == vv.fila:
                            listaP.append(vv2)

                return listaP
        elif ((val == None) and isinstance(val2[0], DatoInsert)):
            if expresion.operador == OPERACION_LOGICA.OR:
                print("Logica en OR")
                listaP = []
                for v2 in val2:
                    vv2: DatoInsert = v2
                    listaP.append(vv2)

                return listaP

            elif expresion.operador == OPERACION_LOGICA.AND:
                listaP = []
                for v2 in val2:
                    vv2: DatoInsert = v2
                    listaP.append(vv2)

                return listaP

            elif expresion.operador == OPERACION_LOGICA.IS_DISTINCT:
                listaP = []
                for v2 in val2:
                    vv2: DatoInsert = v2
                    listaP.append(vv2)

                return listaP

            elif expresion.operador == OPERACION_LOGICA.IS_NOT_DISTINCT:
                listaP = []
                for v2 in val2:
                    vv2: DatoInsert = v2
                    listaP.append(vv2)

                return listaP

        elif (isinstance(val[0], DatoInsert) and val2 == None):
            if expresion.operador == OPERACION_LOGICA.OR:
                print("Logica en OR")
                listaP = []
                for v in val:
                    vv: DatoInsert = v
                    listaP.append(vv)

                return listaP

            elif expresion.operador == OPERACION_LOGICA.AND:
                listaP = []
                for v in val:
                    vv: DatoInsert = v
                    listaP.append(vv)

                return listaP

            elif expresion.operador == OPERACION_LOGICA.IS_DISTINCT:
                listaP = []
                for v in val:
                    listaP.append(v)

                return listaP

            elif expresion.operador == OPERACION_LOGICA.IS_NOT_DISTINCT:
                listaP = []
                for v in val:
                    listaP.append(v)

                return listaP
        else:
            print('Error: No se puede realizar la op. logica')
            # consola.insert('end','>>Error: Expresion logica con tipos incompatibles'+str(expresion.operador)+'\n>>')
            # newErr=ErrorRep('Semantico','Expresion logica con tipos incompatibles '+str(expresion.operador),indice)
            # LisErr.agregar(newErr)

