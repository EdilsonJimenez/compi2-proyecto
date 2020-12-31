from Instruccion_pl import *
from Temporales import *
from expresiones import *
from sentencias import *
import os
import Temporales as T
t_global = T.Temporales()
cadena = ""
ambitoFuncion = ""


class Codigo3d:

    def __init__(self):
        global cadena
        self.i = 0
        cadena += "from goto import with_goto\n"
        cadena += "import FuncionesIntermedias as F3D\n"
        cadena += "heap = F3D.heap\n"
        cadena += "stack = []\n\n"
        cadena += "@with_goto \n"
        cadena += "def main(): \n"
        cadena += "\tglobal heap\n"
        cadena += "\tglobal stack\n"

    def retorno(self):
        global cadena
        cadena += "\nlabel .R\n"
        cadena += "u = stack[-1]"

        cantidad = t_global.varFuncionAnterior()
        i = 1
        cadena += "\n"
        while i < cantidad:
            cadena += "if u == \"F"+str(i)+"\": \n"
            cadena += "\tgoto .F"+str(i)+"\n"
            i += 1

    def imprimir(self):
        global cadena
        self.retorno()
        cadena += "\n\nmain() \n"
        print(cadena)
        self.generar()

        print("----------------------------------SE LIMPIO ----------------------------------------------")
        t_global.limpiar()
        cadena = ""

    def Traducir(self, instrucciones):
        global ts_global
        for i in instrucciones:
            if isinstance(i, If_inst):
                self.t_If(i)
            elif isinstance(i, Funciones_):
                self.t_Funciones_(i)
            elif isinstance(i, Asignacion):
                self.t_asignacion(i)
            elif isinstance(i, EjecucionFuncion):
                self.t_llamadaFuncion(i)
            elif isinstance(i,ForInstruccion):
                self.t_TraduccionFor(i)
            else:
                print("NO TRADUCE....")

    def t_If(self, instancia):
        global t_global, cadena
        cadena += "--------- IF --------------- \n"
        condicion = self.procesar_expresion(instancia.condicion, t_global)
        verdadero = str(t_global.etiquetaT())
        falso = str(t_global.etiquetaT())
        salto = str(t_global.etiquetaT())


        cadena += "if " + str(condicion) + ": \n"
        cadena += "\tgoto ."+verdadero+"\n"
        cadena += "else : \n"
        cadena += "\tgoto ."+falso+"\n"

        cadena += "label . " + verdadero + "\n"
        cadena += "     ~verdadero~"+"\n"
        # Si el if trae instruciones en IF
        if instancia.instIf != 0:
            self.Traducir(instancia.instIf)
        cadena += "goto ."+salto+"\n"+"\n"
        cadena += "label ." + falso + "\n"
        # Si el if trae instruciones en ELSE
        if instancia.instElse != None:
            if instancia.instElse != 0:
                cadena += "     ~falso~" + "\n"
                self.Traducir(instancia.instElse)
        cadena += "label ."+salto+"\n"


    def t_Funciones_(self, instancia):
        global t_global, cadena, ambitoFuncion
        # temporal, nombre, tipo, tam, pos, rol ,ambito
        fun = t_global.varFuncion()
        metodo = tipoSimbolo(str(fun),instancia.Nombre, 'Integer', 0, 0, 'Metodo','')
        t_global.agregarSimbolo(metodo)
        cadena += "label ."+fun+"\n"
        ambitoFuncion = str(instancia.Nombre)

        cadena+="\n# Parametros \n"
        for param in instancia.Parametros:
            print(str(param.Nombre)+"---"+str(param.Tipo))
            tempoP = t_global.varParametro()
            cadena += str(tempoP)+ "\n"

            p = tipoSimbolo(str(tempoP), param.Nombre, param.Tipo, 1, 1, 'parametro', instancia.Nombre)
            t_global.agregarSimbolo(p)

        # Temporal de retorno
        cadena+="\n# Retorno \n"
        tempoP = t_global.varParametro()
        cadena += str(tempoP) + "\n"

        p = tipoSimbolo(str(tempoP), "return", "return", 1, 1, 'local', instancia.Nombre)
        t_global.agregarSimbolo(p)

        cadena += "\n# declaraciones \n"
        for decla in instancia.Declaraciones:
            if decla != None:
                r = self.procesar_expresion(decla.expresion, t_global)
                tempo = t_global.varTemporal()
                cadena += str(tempo) + "=" + str(r) + "\n"
                v = tipoSimbolo(str(tempo), decla.id, decla.tipo, 1, 1, 'local', instancia.Nombre)
                t_global.agregarSimbolo(v)

        #instrucciones
        codigo: Code_Funciones = instancia.Codigo
        self.Traducir(codigo.Codigo)

        anterior = "R"
        cadena += "\ngoto ."+anterior
        cadena += "\n\n"

    def t_asignacion(self, asignacion):
        global t_global, cadena
        # id, expresion
        etiR = ""
        for sim in t_global.tablaSimbolos:
            s: tipoSimbolo = t_global.obtenerSimbolo(sim)
            if s.nombre == asignacion.id and s.ambito == ambitoFuncion:
                etiR = s.temporal

        exp = self.procesar_expresion(asignacion.expresion, t_global)
        cadena += "\n" + str(etiR) + "=" + str(exp) + "\n"

    def t_llamadaFuncion(self, llamada):
        # Id, Lista-Parametros
        global t_global, cadena, ambitoFuncion, stack
        ambitoFuncion = llamada.Id
        listaParametros = []
        if llamada.Parametros != None:
            for param in llamada.Parametros:
                exp = self.procesar_expresion(param, t_global)
                listaParametros.append(str(exp))
        print("lista")
        print(listaParametros)


        cont = 0
        for sim in t_global.tablaSimbolos:
            s: tipoSimbolo = t_global.obtenerSimbolo(sim)
            if s.ambito == ambitoFuncion and str(s.rol) == "parametro":
                print(str(cont))
                cadena += "\n"+str(s.temporal) +"="+ str(listaParametros[cont])
                cont += 1

        salto = t_global.varFuncion()
        cadena += "\nstack.append(\""+salto+"\")\n"
        # llamada goto a la funcion
        for met in t_global.tablaSimbolos:
            m: tipoSimbolo = t_global.obtenerSimbolo(met)
            if m.nombre == llamada.Id and m.rol == "Metodo":
                cadena += "\ngoto ."+str(m.temporal)
        cadena += "\nlabel ."+salto



#--------------------------------  TRADUCCION FOR
    def t_TraduccionSwitch(self,Objeto):
        #Objetos globales para la traduccion
        global t_global, cadena
        cadena += "--------- For --------------- \n"





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
            c = str(expresiones.val)
            if c.isdigit():
                return expresiones.val
            else:
                q = "\""+expresiones.val+"\""
                return q
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
        print("valores"+str(val)+str(val2))
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

    def procesar_variable(self, tV, ts):
        global t_global, ambitoFuncion
        print("procesar variable")
        r = ""
        print(t_global.tablaSimbolos)
        for item in t_global.tablaSimbolos:
            v: tipoSimbolo = t_global.obtenerSimbolo(item)
            print(str(v.nombre)+"<>"+str(tV.id)+"-"+str(v.ambito)+"<>"+ambitoFuncion)
            if v.nombre == tV.id and v.ambito == ambitoFuncion:
                print(str(v.temporal))
                r = str(v.temporal)
                return r
        return r


    def generar(self):
        global cadena
        f = open('./intermedio.py', 'w')
        f.write(cadena)
        f.close()
