from Instruccion_pl import *
from Temporales import *
from expresiones import *
from sentencias import *

from SqlComandos import SqlComandos as ff

import os
import Temporales as T
import sentencias as ss



t_global = T.Temporales()
cadena = ""
cadenaFuncion = ""
cadenaExpresion = ""
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

        cadena += "\nlabel .END\n"

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
        global ts_global, cadena, cadenaFuncion
        for i in instrucciones:
            if isinstance(i, Funciones_):
                cadenaFuncion += self.t_Funciones_(i)
            elif isinstance(i, EjecucionFuncion):
                print("6666666666666666666666666666666666666 ejecucion funcion 1")
                cadena += self.t_llamadaFuncion(i)
            elif isinstance(i, SentenciasSQL):
                cadena += self.t_sentenciaSQL(i)
            else:
                Cadena = ff(i)

                if Cadena!=None:
                    print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>    INICIO DE LA CADENA GENERADA WEBON ")
                    print(Cadena)
                    print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>    FIN  DE LA CADENA GENERADA WEBON ")
                else:
                    print("ESTA ENTRANDO OTRO TIPO DE ACCION... ")

                print(i)
                print("NO TRADUCE....")
        cadena += "\n\ngoto .END\n"
        cadena += cadenaFuncion


    def Traducir2(self, instrucciones):
        global ts_global, cadenaFuncion
        cadenaT = ""
        contador = 0
        for i in instrucciones:
            if isinstance(i, If_inst):
                cadenaT += self.t_If(i)
            elif isinstance(i, ss.EjecucionFuncion):
                cadenaT += self.t_llamadaFuncion(i)
            elif isinstance(i, Asignacion):
                cadenaT += self.t_asignacion(i)
            elif isinstance(i, ForInstruccion):
                cadenaT += self.t_TraduccionFor(i)
            elif isinstance(i, CaseSimple):
                cadenaT += self.t_TraduccionCaseSimple(i, "")
            elif isinstance(i, RetornoFuncion):
                cadenaT += self.t_retornoFuncion(i)
            elif isinstance(i, CaseBuscado):
                cadenaT += self.t_TraduccionCaseBuscado(i, "")
            else:
                # try:
                #     cadenaT += self.t_llamadaFuncion(i)
                # except:
                #     print("Esta mal algo ")
                print(i)
                print("NO TRADUCE2....")

            contador += 1
        return cadenaT


    def t_If(self, instancia):
        global t_global, cadena, cadenaExpresion
        cadenaIf  =""
        cadenaIf += "# --------- IF --------------- \n"
        print(instancia.condicion)
        condicion, cad = self.procesar_expresion(instancia.condicion, t_global)
        cadenaExpresion = ""
        cadenaIf += cad
        verdadero = str(t_global.etiquetaT())
        falso = str(t_global.etiquetaT())
        salto = str(t_global.etiquetaT())

        cadenaIf += "if " + str(condicion) + ": \n"
        cadenaIf += "\tgoto ."+verdadero+"\n"
        cadenaIf += "else : \n"
        cadenaIf += "\tgoto ."+falso+"\n"

        cadenaIf += "label ." + verdadero + "\n"
        cadenaIf += "# ~verdadero~"+"\n"
        # Si el if trae instruciones en IF
        if instancia.instIf != 0:
            cadenaIf += self.Traducir2(instancia.instIf)
        cadenaIf += "goto ."+salto+"\n"+"\n"
        cadenaIf += "label ." + falso + "\n"
        # Si el if trae instruciones en ELSE
        if instancia.instElse != None:
            if instancia.instElse != 0:
                cadenaIf += "# ~falso~" + "\n"
                cadenaIf += self.Traducir2(instancia.instElse)
        cadenaIf += "label ."+salto+"\n"

        return cadenaIf


    def t_Funciones_(self, instancia):
        global t_global, cadenaFuncion, ambitoFuncion, cadenaExpresion
        # temporal, nombre, tipo, tam, pos, rol ,ambito
        cadenaF = "\n"
        fun = t_global.varFuncion()
        metodo = tipoSimbolo(str(fun),instancia.Nombre, 'Integer', 0, 0, 'Metodo','')
        t_global.agregarSimbolo(metodo)
        cadenaF += "label ."+fun+"\n"
        ambitoFuncion = str(instancia.Nombre)
        cadenaF += "\n#**** Funcion *****\n"
        cadenaF +="\n# Parametros \n"
        for param in instancia.Parametros:
            print(str(param.Nombre)+"---"+str(param.Tipo))

            tempoP = t_global.varParametro()
            cadenaF += str(tempoP)+ "\n"

            p = tipoSimbolo(str(tempoP), param.Nombre, param.Tipo, 1, 1, 'parametro', instancia.Nombre)
            t_global.agregarSimbolo(p)

        # Temporal de retorno
        cadenaF +="\n# Retorno \n"
        tempoP = t_global.varParametro()
        cadenaF +="global "+str(tempoP) + "\n"
        p = tipoSimbolo(str(tempoP), "return", "return", 1, 1, 'local', instancia.Nombre)
        t_global.agregarSimbolo(p)

        cadenaF += "\n# Declaraciones \n"
        for decla in instancia.Declaraciones:
            if decla != None:
                cadenaexp = ""
                r,cadenaexp = self.procesar_expresion(decla.expresion, t_global)
                cadenaExpresion = ""
                cadenaF += cadenaexp
                tempo = t_global.varTemporal()
                cadenaF +=str(tempo) + " = " + str(r) + "\n"
                v = tipoSimbolo(str(tempo), decla.id, decla.tipo, 1, 1, 'local', instancia.Nombre)
                t_global.agregarSimbolo(v)

        #instrucciones
        codigo: Code_Funciones = instancia.Codigo
        cadenaF += self.Traducir2(codigo.Codigo)

        #llamamos al Recorrido del cuerpo
        #cadenaF += self.RecorrerCuerpoCodigo(codigo.Codigo,instancia.Nombre)
        self.Traducir(instancia.Instrucciones)


        anterior = "R"
        cadenaF += "\ngoto ."+anterior
        cadenaF += "\n\n"

        return cadenaF

    def t_asignacion(self, asignacion):
        # id, expresion, llamarFuncion
        global t_global, cadena, cadenaFuncion, ambitoFuncion
        cadenaAsi = ""
        if isinstance(asignacion.expresion,EjecucionFuncion):
            ambitoFuncion = asignacion.expresion.Id

            for fun in t_global.tablaSimbolos:
                f: tipoSimbolo = t_global.obtenerSimbolo(fun)
                if f.ambito == asignacion.expresion.Id and f.rol == "local" and f.nombre == "return":
                    etiR = f.temporal

            # buscamos temporal de la variable.
            for var in t_global.tablaSimbolos:
                t: tipoSimbolo = t_global.obtenerSimbolo(var)
                if t.nombre == asignacion.id and t.ambito == ambitoFuncion:
                    temp = t.temporal

            cadenaAsi += "\n" + str(temp) + "=" + str(etiR) + "\n"
            return cadenaAsi
        else:
            etiR = ""
            for sim in t_global.tablaSimbolos:
                s: tipoSimbolo = t_global.obtenerSimbolo(sim)
                if s.nombre == asignacion.id and s.ambito == ambitoFuncion:
                    etiR = s.temporal

            cadenaexp = ""
            exp,cadenaexp = self.procesar_expresion(asignacion.expresion, t_global)
            cadenaExpresion = ""
            cadenaAsi += cadenaexp
            cadenaAsi += "\n" + str(etiR) + "=" + str(exp) + "\n"

            return cadenaAsi

    def t_llamadaFuncion(self, llamada):
        # Id, Lista-Parametros
        global t_global, cadena, ambitoFuncion, stack, cadenaExpresion
        cadenallamada  = ""

        ambitoFuncion = llamada.Id
        listaParametros = []
        if llamada.Parametros != None:
            for param in llamada.Parametros:
                c = ""
                exp,c = self.procesar_expresion(param, t_global)
                cadenaExpresion = ""
                listaParametros.append(str(exp))
        print("lista")
        print(listaParametros)


        cont = 0
        for sim in t_global.tablaSimbolos:
            s: tipoSimbolo = t_global.obtenerSimbolo(sim)
            if s.ambito == ambitoFuncion and str(s.rol) == "parametro":
                print(str(cont))
                cadenallamada += "\n"+str(s.temporal) +"="+ str(listaParametros[cont])
                cont += 1

        salto = t_global.varFuncion()
        cadenallamada += "\nstack.append(\""+salto+"\")\n"
        # llamada goto a la funcion
        for met in t_global.tablaSimbolos:
            m: tipoSimbolo = t_global.obtenerSimbolo(met)
            if m.nombre == llamada.Id and m.rol == "Metodo":
                cadenallamada += "\ngoto ."+str(m.temporal)
        cadenallamada += "\nlabel ."+salto

        return cadenallamada

    def t_retornoFuncion(self, instancia):
        global ambitoFuncion, t_global, cadenaExpresion
        cadenaRetorno = " # return \n"
        for item in t_global.tablaSimbolos:
            v: tipoSimbolo = t_global.obtenerSimbolo(item)
            if v.nombre == "return" and v.ambito == ambitoFuncion:
                r = str(v.temporal)

        exp, c = self.procesar_expresion(instancia.Expresion, t_global)
        cadenaExpresion = ""
        cadenaRetorno += c
        cadenaRetorno += "\n"+str(r)+" = "+str(exp)+"\n"

        anterior = "R"
        cadenaRetorno += "\ngoto ."+anterior
        cadenaRetorno += "\n\n"

        return cadenaRetorno



#--------------------------------  TRADUCCION CUERPO DE LA FUNCION
    def RecorrerCuerpoCodigo(self,Instrucciones,Ambito):
        #Objetos para diferenciar
        if(isinstance(Instrucciones,list)):
            print("Viene una lista de codigo..")
            #Recorremos la lista
            #Miramos las instancias que trae
            for elemento in Instrucciones:
                if(isinstance(elemento,CaseSimple)):
                    #Nos bamos a la Generacion del codigo del case
                    print("Encontre el Case Simple")
                    self.t_TraduccionCaseSimple(elemento,Ambito)
                elif(isinstance(elemento,CaseBuscado)):
                    print("Encontre el Case Buscado")
        else:
            print("Viene epsilon en la produccion")


#--------------------------------   TRADUCCION CASE SIMPLE
    def t_TraduccionCaseSimple(self,Objeto:CaseSimple, Ambito):
        #Objetos globales para la traduccion
        global t_global
        cadena = "#--------- CASE SIMPLE --------------- \n"
#-------#Viene Expresion_Busqueda  => ExpresionValor(ID)
        #Creamor un temporal con el valor que va a tener
        Variable:ExpresionValor = Objeto.busqueda
# -------#viene CElse(CodigoEpsilon) =>
        #Objetemos el else
        vari1: CElse = Objeto.caseelse
        #busqueda, listawhen, caseelse
#-------#viene Lista_When =>Lista => CSWhen(Cs_Expresion, CodigoCuerpoEpsilon) => Cs_Expresion=> Lista => Lista de expresines
        cadena += self.RecorrerListaWhensCS(Objeto.listawhen,Ambito,Variable,vari1)
        return cadena

    # Recorremos la lista de Whens Case Simple
    def RecorrerListaWhensCS(self, lista,Ambito,Variable,Else):
        cadena = ""
        contador = len(lista)
        ifaux = None
        while contador > 0:
            element = lista[contador - 1]
            ele: CSWhen = element
            print(ele)
            if contador == len(lista):
                explogica = self.Recorrido_InstruccionesCS(ele.expresiones, Ambito, Variable)
                elseaux = None
                if Else is not None:
                    elseaux = Else.sentencias
                ifaux = If_inst(explogica, element.sentencias, elseaux)
            else:
                explogica = self.Recorrido_InstruccionesCS(ele.expresiones, Ambito, Variable)
                ifaux = If_inst(explogica, element.sentencias, [ifaux])
            contador = contador - 1
        if ifaux is not None:
            cadena += self.t_If(ifaux)

        return cadena

    #Recorremos la lista de instrucciones
    def Recorrido_InstruccionesCS(self, listaIns, Ambito, Variable):

        contador=0
        exp1 = None
        exp2 = None
        explogica = None
        for ele in listaIns:

            #Recorremos los tipos de instruccines
            if isinstance(ele,ExpresionAritmetica) or isinstance(ele, ExpresionValor):
                print("Viene un alista de instrucciones aritmeticas.. ")
                if contador == 0:
                    exp1 = ExpresionRelacional(Variable, ele, OPERACION_RELACIONAL.IGUALQUE)
                else:
                    exp2 = ExpresionRelacional(Variable, ele, OPERACION_RELACIONAL.IGUALQUE)
                    explogica = ExpresionLogica(exp1, exp2, OPERACION_LOGICA.OR)
                    exp1 = explogica

            contador+=1

        return exp1



#--------------------------------   TRADUCCION CASE BUSCADO
    def t_TraduccionCaseBuscado(self,Objeto:CaseBuscado, Ambito):
        #Objetos globales para la traduccion
        global t_global
        cadena = "#--------- CASE BUSCADO --------------- \n"
# -------#viene CElse(CodigoEpsilon) =>
        #Obtenemos el else si este existe
        #Objetemos el else
        vari1:CElse = Objeto.caseelse
#-------#viene Lista_When =>Lista => CBWhen(expresion->una sola, sentencias->CodigoCuerpoEpsilon)
        cadena += self.RecorrerListaWhensCB(Objeto.listawhen,Ambito,vari1)

        return cadena

    #Recorremos la lista de whens CB
    def RecorrerListaWhensCB(self, lista, Ambito, Else):
        cadena = ""
        contador = len(lista)
        ifaux = None
        while contador > 0:
            element = lista[contador - 1]
            ele: CBWhen = element
            print(ele)
            if contador == len(lista):
                elseaux = None
                if Else is not None:
                    elseaux = Else.sentencias
                ifaux = If_inst(ele.expresion, element.sentencias, elseaux)
            else:
                ifaux = If_inst(ele.expresion, element.sentencias, [ifaux])
            contador = contador - 1
        if ifaux is not None:
            cadena += self.t_If(ifaux)
        return cadena



    def t_CrearIndice(self, objeto):
        global t_global, cadena

        crearindice: CrearIndice = objeto
        # Generando Sentencia SQL

        sentencia = "CREATE "

        if crearindice.unique:
            sentencia += "UNIQUE "

        sentencia += "INDEX " + str(crearindice.id_indice)

        sentencia += " ON " + str(crearindice.id_tabla) + " ("

        for c in crearindice.columnas:
            col: ColumnaIndice = c
            sentencia += str(col.id_columna)
            if col.orden is not None:
                sentencia += " " + str(col.orden)
            if col.nulls is not None:
                sentencia += " " + str(col.nulls)
            sentencia += ", "

        sentencia = sentencia[0: len(sentencia) - 2 ]
        sentencia += ");"

        # Generando codigo de tres direcciones
        v = t_global.varTemporal()
        cadena += str(v) + " = \"" + sentencia + "\"\n"
        cadena += "heap.append(" + str(v) + ")\n"
        cadena += "ejecutarSQL()\n"


    def t_sentenciaSQL(self, sentencia: SentenciasSQL):
        global t_global
        cadena = ""
        v = t_global.varTemporal()
        cadena += str(v) + " = \"" + sentencia.CadenaSQL + "\"\n"
        cadena += "heap.append(" + str(v) + ")\n"
        cadena += "F3D.ejecutarSQL()\n"

        return cadena



# --------------------------------  TRADUCCION CUERPO DE LA FUNCION
    # EXPRESIONES
    def procesar_expresion(self, expresiones, ts):
        global cadenaExpresion
        if isinstance(expresiones, ExpresionAritmetica):
            v,c = self.procesar_aritmetica(expresiones, ts)
            cadenaExpresion += c
            return v,cadenaExpresion
        elif isinstance(expresiones, ExpresionRelacional):
            v,c = self.procesar_relacional(expresiones, ts)
            cadenaExpresion += c
            return v, cadenaExpresion
        elif isinstance(expresiones, ExpresionLogica):
            v,c = self.procesar_logica(expresiones, ts)
            cadenaExpresion += c
            return v, cadenaExpresion
        elif isinstance(expresiones, UnitariaNegAritmetica):
            v,c = procesar_negAritmetica(expresiones, ts)
            cadenaExpresion += c
            return v, cadenaExpresion
        elif isinstance(expresiones, ExpresionValor):
            c = str(expresiones.val)
            if c.isdigit():
                return expresiones.val, ""
            else:
                q = "\""+expresiones.val+"\""
                return q, ""
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
        val, cad1 = self.procesar_expresion(expresion.exp1, ts)
        val2, cad2 = self.procesar_expresion(expresion.exp2, ts)

        if expresion.operador == OPERACION_ARITMETICA.MAS:
            v = t_global.varTemporal()
            cadena = v + "= "+str(val)+" + "+str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_ARITMETICA.MENOS:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " - " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_ARITMETICA.MULTI:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " * " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " / " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_ARITMETICA.RESIDUO:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " / " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_ARITMETICA.POTENCIA:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " ** " + str(val2) + "\n"
            return v, cadena

    def procesar_relacional(self, expresion, ts):
        # OPTIMIZACION - AHORRO DE 2 LINEAS........................................................
        val, cad1 = self.procesar_expresion(expresion.exp1, ts)
        val2, cad2 = self.procesar_expresion(expresion.exp2, ts)
        print("valores"+str(val)+str(val2))
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " == " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " != " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " >= " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " <= " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " > " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " < " + str(val2) + "\n"
            return v, cadena
        else:
            return 1

    def procesar_logica(self, expresion, ts):
        val, cad1 = self.procesar_expresion(expresion.exp1, ts)
        val2, cad2 = self.procesar_expresion(expresion.exp2, ts)

        if expresion.operador == OPERACION_LOGICA.AND:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " and " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_LOGICA.OR:
            v = t_global.varTemporal()
            cadena = v + "= " + str(val) + " or " + str(val2) + "\n"
            return v, cadena

    def procesar_variable(self, tV, ts):
        global t_global, ambitoFuncion
        print("procesar variable")
        r = ""
        for item in t_global.tablaSimbolos:
            v: tipoSimbolo = t_global.obtenerSimbolo(item)
            print(str(v.nombre)+"<>"+str(tV.id)+"-"+str(v.ambito)+"<>"+ambitoFuncion)
            if v.nombre == tV.id and v.ambito == ambitoFuncion:
                print(str(v.temporal))
                r = str(v.temporal)
                return r,""
        return r,""


    def generar(self):
        global cadena
        f = open('./intermedio.py', 'w')
        f.write(cadena)
        f.close()
