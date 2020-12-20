import ts as TS
import jsonMode as Master
import interprete as Inter
from six import string_types
from errores import *
from expresiones import *
from prettytable import PrettyTable
from random import *
from expresiones import *

LisErr = TablaError([])
ts_global = TS.TablaDeSimbolos()
Lista = []
ListaTablasG = []
baseN = []
baseActual = ""
Ejecucion = ">"

listaGeneral = {}




Lista.append(Ejecucion)


class Instruccion():
    'Abstracta'

    def Ejecutar(self):
        pass


def imprir(string):
    global Ejecucion

    Ejecucion += string + "\n"
    Lista.clear();
    Lista.append(Ejecucion)

def mostrarConsulta(resultado):
    tabla = PrettyTable()
    for key, val in resultado.items():
        tabla.add_column(key, val)

    imprir(str(tabla))

#----------------------------------------------------------
#           TABLA DE SIMBOLOS
#----------------------------------------------------------
#----------------------------------------------------------
from graphviz import Digraph, nohtml
from graphviz import Graph
from graphviz import escape

def tabla_simbolos():
    print("------------SIMBOLOS---------------")
    ts=ts_global
    SymbolT =  Graph('g', filename='bsimbolos.gv', format='png',node_attr={'shape': 'plaintext', 'height': '.1'})

    #DICIONARIO DATOS
    cadena=''
    for fn in ts.Datos:
        fun=ts.obtenerDato(fn)
        cadena+='<TR><TD>'+str(fun.bd)+'</TD>'+'<TD>'+str(fun.tabla)+'</TD>'+'<TD>'+str(fun.columna)+'</TD>'+'<TD>'+str(fun.valor)+'</TD>'+'<TD>'+str(fun.fila)+'</TD></TR>'


    #DICIONARIO Tablas
    cadena2=''
    for fn in ts.Tablas:
        fun=ts.obtenerTabla(fn)
        for cuerpos in fun.cuerpo:
            if isinstance(cuerpos.tipo,valorTipo):
                cadena2+='<TR><TD>'+str(fun.id)+'</TD>'+'<TD>'+str(cuerpos.id)+'</TD>'+'<TD>'+str(cuerpos.tipo.valor)+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD></TR>'
            else:
                cadena2+='<TR><TD>'+str(fun.id)+'</TD>'+'<TD>'+str(cuerpos.id)+'</TD>'+'<TD>'+str(cuerpos.tipo)+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD></TR>'

    cadena3=''
    for fn in ts.BasesDatos:
        fun=ts.obtenerBasesDatos(fn)
        cadena3 +='<TR><TD>'+str(fun.idBase)+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD></TR>'



    SymbolT.node('table','''<<TABLE>
                            <TR>
                                <TD>BASE DATOS</TD>
                                <TD>TABLA</TD>
                                <TD>COLUMNA</TD>
                                <TD>VALOR </TD>
                                <TD>FILA</TD>
                            </TR>'''
                            +cadena+
                            ''' <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD>ID TABLA</TD>
                                <TD>ID COLUMNA</TD>
                                <TD>TIPO COLUMNA</TD>
                                <TD>  </TD>
                                <TD>  </TD>
                            </TR>'''
                             + cadena2 +
                             ''' <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD>ID BASE DE DATOS</TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>'''
                            +cadena3+
                        '''</TABLE>>''')


    #DICCIONARIO BASE DE DATOS

    SymbolT.render('g', format='png', view=True)

# Un drop table esta compuesto por el ID de la tabla que eliminara.
class DropTable(Instruccion):
    def __init__(self, id):
        self.id = id

    def Ejecutar(self):
        #validar que exista la base de datos global
        #validar que exista la tabla en la base de datos
        #eliminar

        global ts_global, baseActual
        global LisErr

        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:
            r2 = ts_global.obtenerTabla(self.id[0].val)
            if r2 is not None:
                #Eliminar Tabla
                res = Master.dropTable(baseActual,self.id[0].val)
                if res ==0:
                    #se Elimino exitosamente
                    ts_global.EliminarTabla(self.id[0].val)
                    imprir("DROP TABLE:   Exito al Eliminar ")
                elif res ==1:
                    #Error all eliminar
                    imprir("DROP TABLE:   Error Logico al eliminar")
                elif res==2:
                    #No esta la base de datos en la data
                    imprir("DROP TABLE:   Error no se encuentra la BD ")
                elif res==3:
                    #No esta la tabla en la base de datos
                    imprir("DROP TABLE:   Error no se encuentra la Tabla en la DB")
                else:
                    imprir("DROP TABLE:   Error al eliminar la Tabla!")

            else:
                imprir("DROP TABLE:   La tabla no existe!")
        else:
            imprir("DROP TABLE:   La Base de datos a eliminar no existe!")
            #colocar error semantico








class Absoluto(Instruccion) :
    def __init__(self, variable) :
        self.variable=variable

#---------------------------------------------------------------------------------------------------
class Select(Instruccion) :
    def __init__(self,  unionn, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn


    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr
        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos


        if r is not None:


           for ee in self.Nombres_Tablas:


               if(isinstance(ee,AccesoTablaSinLista)): #viene sin alias


                   #Recorremos el diccionario general para ver si existe la tabla que queremos
                   # recorremos lista General de Tablas
                   for elemento2 in ts_global.Tablas:

                       x: CreateTable = ts_global.obtenerTabla(elemento2)


                       if (str(x.id) == str(ee.NombreT)):
                          #si es la tabla validamos que tipo de campo viene



                            for ii in self.Lista_Campos:
                                if(isinstance(ii,Campo_AccedidoSinLista)): #nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                    #*  , nombrecampo,  nombrecampo alias
                                    #listaGeneral
                                    for ele in x.cuerpo: #recorremos lista de columnas
                                        y:CampoTabla = ele
                                        if (str(y.id) == str(ii.Columna)):


                                            print("LA columan "+str(ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                            #Bamos a sacar todos los datos coincidentes
                                            #recorremos datos

                                            #Vallidamos que la no venga sin datos
                                            print(ii.NombreT)
                                            if(ii.NombreT !=""):
                                                #hacemos una doble condicion para agarrar la columna que es

                                                if(str(x.id)==ii.NombreT):
                                                    print("Estoy entrando <<<<<<<<<<<<<<<<<<<<< ")
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))
                                                    listaGeneral[ii.Columna] = lista
                                                else:
                                                    print("")

                                            else:

                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))
                                                listaGeneral[ii.Columna] = lista


                                        elif(str(ii.Columna) == "*"):
                                            print("Vienen todo los datos de la tabla")

                                            #Vallidamos que la no venga sin datos
                                            if(ii.NombreT!=""):
                                                #hacemos una doble condicion para agarrar la columna que es
                                                if(str(x.id)==ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[pp.id] = Lista2

                                            #viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[pp.id] = Lista2


                                        else:
                                            print("")

                                elif(isinstance(ii,Campo_Accedido)): # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                    #listaGeneral
                                    for ele in x.cuerpo:
                                        y: CampoTabla = ele

                                        if (y.id == ii.Columna):
                                            print("LA columan "+str(ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")

                                            #verificamos el alias

                                            ListaAlias = ii.Lista_Alias
                                            #Tenemos el alias
                                            nuevoNave = ListaAlias.Alias
                                            print("ahora la columna se llama"+str(nuevoNave))

                                            # Bamos a sacar todos los datos coincidentes
                                            #Vallidamos que la no venga sin datos
                                            if(ii.NombreT !=""):
                                                #hacemos una doble condicion para agarrar la columna que es
                                                if(str(x.id)==ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = lista


                                        elif(y.id == '*'):
                                            #Recorrer todos los datos de la columna
                                            print("Vienen todo los datos  los datos de esa columna")

                                            ListaAlias = ii.Lista_Alias
                                            #Tenemos el alias
                                            nuevoNave = ListaAlias.Alias

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[str(nuevoNave)] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = Lista2
                                        else:
                                            print("")
                                else:
                                    print("Otros posibles tipos ")
                       else:
                           print("")
#============================================================================   Acceso a las tablas con alias
               elif(isinstance(ee,AccesoTabla)): #viene con un alias

                   # verificamos el alias
                   AliasTabla = ee.Lista_Alias
                   # Tenemos el alias
                   AliasT = AliasTabla.Alias
                   # Recorremos el diccionario general para ver si existe la tabla que queremos
                   # recorremos lista General de Tablas
                   for elemento2 in ts_global.Tablas:
                       x: CreateTable = ts_global.obtenerTabla(elemento2)
                       if (str(x.id) == str(ee.NombreT)):
                           # si es la tabla validamos que tipo de campo viene
                           for ii in self.Lista_Campos:
                               if (isinstance(ii,Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                   # *  , nombrecampo,  nombrecampo alias
                                   # listaGeneral
                                   for ele in x.cuerpo:  # recorremos lista de columnas
                                       y: CampoTabla = ele
                                       if (str(y.id) == str(ii.Columna)):
                                           print("LA columan " + str(
                                               ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                           # Bamos a sacar todos los datos coincidentes
                                           # recorremos datos
                                           # Vallidamos que la no venga sin datos
                                           if (ii.NombreT != ""):
                                               if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                   i = ts_global.Datos
                                                   lista = []
                                                   for gg in ts_global.Datos:
                                                       t: DatoInsert = ts_global.obtenerDato(gg)
                                                       if (str(t.columna) == str(ii.Columna)):
                                                           print(str(t.valor))
                                                           lista.append(str(t.valor))

                                                   listaGeneral[ii.Columna] = lista
                                               else:
                                                   print("")
                                           else:
                                               i = ts_global.Datos
                                               lista = []
                                               for gg in ts_global.Datos:
                                                   t: DatoInsert = ts_global.obtenerDato(gg)
                                                   if (str(t.columna) == str(ii.Columna)):
                                                       print(str(t.valor))
                                                       lista.append(str(t.valor))
                                               listaGeneral[ii.Columna] = lista
                                       elif (str(ii.Columna) == "*"):
                                           print("Vienen todo los datos de la tabla")
                                           # Vallidamos que la no venga sin datos
                                           if (ii.NombreT != ""):
                                               # hacemos una doble condicion para agarrar la columna que es
                                               if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                   # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                   for columnas in x.cuerpo:
                                                       pp: CampoTabla = columnas
                                                       Lista2 = []
                                                       i = ts_global.Datos
                                                       for gg in i:
                                                           t: DatoInsert = ts_global.obtenerDato(gg)
                                                           if (pp.id == t.columna):
                                                               print(str(t.valor))
                                                               Lista2.append(str(t.valor))
                                                       listaGeneral[pp.id] = Lista2
                                           # viene sin referencia a tabla
                                           else:
                                               # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                               for columnas in x.cuerpo:
                                                   pp: CampoTabla = columnas
                                                   Lista2 = []
                                                   i = ts_global.Datos
                                                   for gg in i:
                                                       t: DatoInsert = ts_global.obtenerDato(gg)
                                                       if (pp.id == t.columna):
                                                           print(str(t.valor))
                                                           Lista2.append(str(t.valor))
                                                   listaGeneral[pp.id] = Lista2
                                       else:
                                           print("")
                               elif (isinstance(ii, Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss
                                   # listaGeneral
                                   for ele in x.cuerpo:
                                       y: CampoTabla = ele
                                       if (y.id == ii.Columna):
                                           print("LA columan " + str(ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                           # verificamos el alias
                                           ListaAlias = ii.Lista_Alias
                                           # Tenemos el alias
                                           nuevoNave = ListaAlias.Alias
                                           print("ahora la columna se llama" + str(nuevoNave))
                                           # Bamos a sacar todos los datos coincidentes
                                           # Vallidamos que la no venga sin datos
                                           if (ii.NombreT != ""):
                                               # hacemos una doble condicion para agarrar la columna que es
                                               if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                   i = ts_global.Datos
                                                   lista = []
                                                   for gg in ts_global.Datos:
                                                       t: DatoInsert = ts_global.obtenerDato(gg)
                                                       if (str(t.columna) == str(ii.Columna)):
                                                           print(str(t.valor))
                                                           lista.append(str(t.valor))
                                                   listaGeneral[str(nuevoNave)] = lista
                                               else:
                                                   print("")
                                           else:
                                               i = ts_global.Datos
                                               lista = []
                                               for gg in ts_global.Datos:
                                                   t: DatoInsert = ts_global.obtenerDato(gg)
                                                   if (str(t.columna) == str(ii.Columna)):
                                                       print(str(t.valor))
                                                       lista.append(str(t.valor))
                                               listaGeneral[str(nuevoNave)] = lista
                                       elif (y.id == '*'):
                                           # Recorrer todos los datos de la columna
                                           print("Vienen todo los datos  los datos de esa columna")
                                           ListaAlias = ii.Lista_Alias
                                           # Tenemos el alias
                                           nuevoNave = ListaAlias.Alias
                                           # Vallidamos que la no venga sin datos
                                           if (ii.NombreT != ""):
                                               # hacemos una doble condicion para agarrar la columna que es
                                               if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                   # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                   for columnas in x.cuerpo:
                                                       pp: CampoTabla = columnas
                                                       Lista2 = []
                                                       i = ts_global.Datos
                                                       for gg in i:
                                                           t: DatoInsert = ts_global.obtenerDato(gg)
                                                           if (pp.id == t.columna):
                                                               print(str(t.valor))
                                                               Lista2.append(str(t.valor))
                                                       listaGeneral[str(nuevoNave)] = Lista2
                                           # viene sin referencia a tabla
                                           else:
                                               # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                               for columnas in x.cuerpo:
                                                   pp: CampoTabla = columnas
                                                   Lista2 = []
                                                   i = ts_global.Datos
                                                   for gg in i:
                                                       t: DatoInsert = ts_global.obtenerDato(gg)
                                                       if (pp.id == t.columna):
                                                           print(str(t.valor))
                                                           Lista2.append(str(t.valor))
                                                   listaGeneral[str(nuevoNave)] = Lista2
                                       else:
                                           print("")
                               else:
                                   print("Otros posibles tipos ")
                       else:
                           print("")
               else:
                    imprir("Viene otro tipo de accion ")
        else:
            imprir("SELECT : No existe la base de datos acual")
        print(listaGeneral)
        mostrarConsulta(listaGeneral)
        listaGeneral.clear()






#---------------------------------------------------------------------------------------------------
class Select2(Instruccion) :
    def __init__(self,  unionn,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn
        self.Cuerpo = Cuerpo

    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr
        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos

        if r is not None:

            for ee in self.Nombres_Tablas:

                if (isinstance(ee, AccesoTablaSinLista)):  # viene sin alias

                    # Recorremos el diccionario general para ver si existe la tabla que queremos
                    # recorremos lista General de Tablas
                    for elemento2 in ts_global.Tablas:

                        x: CreateTable = ts_global.obtenerTabla(elemento2)

                        if (str(x.id) == str(ee.NombreT)):
                            # si es la tabla validamos que tipo de campo viene

                            for ii in self.Lista_Campos:
                                if (isinstance(ii,
                                               Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                    # *  , nombrecampo,  nombrecampo alias
                                    # listaGeneral
                                    for ele in x.cuerpo:  # recorremos lista de columnas
                                        y: CampoTabla = ele
                                        if (str(y.id) == str(ii.Columna)):

                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                            # Bamos a sacar todos los datos coincidentes
                                            # recorremos datos

                                            # Vallidamos que la no venga sin datos
                                            print(ii.NombreT)
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT):
                                                    print("Estoy entrando <<<<<<<<<<<<<<<<<<<<< ")
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))
                                                    listaGeneral[ii.Columna] = lista
                                                else:
                                                    print("")

                                            else:

                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))
                                                listaGeneral[ii.Columna] = lista


                                        elif (str(ii.Columna) == "*"):
                                            print("Vienen todo los datos de la tabla")

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[pp.id] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[pp.id] = Lista2


                                        else:
                                            print("")

                                elif (isinstance(ii,
                                                 Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                    # listaGeneral
                                    for ele in x.cuerpo:
                                        y: CampoTabla = ele

                                        if (y.id == ii.Columna):
                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")

                                            # verificamos el alias

                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias
                                            print("ahora la columna se llama" + str(nuevoNave))

                                            # Bamos a sacar todos los datos coincidentes
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = lista


                                        elif (y.id == '*'):
                                            # Recorrer todos los datos de la columna
                                            print("Vienen todo los datos  los datos de esa columna")

                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[str(nuevoNave)] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = Lista2
                                        else:
                                            print("")
                                else:
                                    print("Otros posibles tipos ")
                        else:
                            print("")


                # ============================================================================   Acceso a las tablas con alias
                elif (isinstance(ee, AccesoTabla)):  # viene con un alias

                    # verificamos el alias
                    AliasTabla = ee.Lista_Alias
                    # Tenemos el alias
                    AliasT = AliasTabla.Alias
                    # Recorremos el diccionario general para ver si existe la tabla que queremos
                    # recorremos lista General de Tablas
                    for elemento2 in ts_global.Tablas:
                        x: CreateTable = ts_global.obtenerTabla(elemento2)
                        if (str(x.id) == str(ee.NombreT)):
                            # si es la tabla validamos que tipo de campo viene
                            for ii in self.Lista_Campos:
                                if (isinstance(ii,
                                               Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                    # *  , nombrecampo,  nombrecampo alias
                                    # listaGeneral
                                    for ele in x.cuerpo:  # recorremos lista de columnas
                                        y: CampoTabla = ele
                                        if (str(y.id) == str(ii.Columna)):
                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                            # Bamos a sacar todos los datos coincidentes
                                            # recorremos datos
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))
                                                            lista.append(str(t.valor))
                                                    listaGeneral[ii.Columna] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))
                                                listaGeneral[ii.Columna] = lista
                                        elif (str(ii.Columna) == "*"):
                                            print("Vienen todo los datos de la tabla")
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[pp.id] = Lista2
                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[pp.id] = Lista2
                                        else:
                                            print("")
                                elif (isinstance(ii,
                                                 Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss
                                    # listaGeneral
                                    for ele in x.cuerpo:
                                        y: CampoTabla = ele
                                        if (y.id == ii.Columna):
                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                            # verificamos el alias
                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias
                                            print("ahora la columna se llama" + str(nuevoNave))
                                            # Bamos a sacar todos los datos coincidentes
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))
                                                            lista.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = lista
                                        elif (y.id == '*'):
                                            # Recorrer todos los datos de la columna
                                            print("Vienen todo los datos  los datos de esa columna")
                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[str(nuevoNave)] = Lista2
                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = Lista2
                                        else:
                                            print("")
                                else:
                                    print("Otros posibles tipos ")
                        else:
                            print("")
                else:
                    imprir("Viene otro tipo de accion ")
        else:
            imprir("SELECT : No existe la base de datos acual")
        print(listaGeneral)
        #listaGeneral.clear()



        #====================================================================   Proceso del cuerpo para editar valores en la tabla
       #procesando el cuerpo General de las tablas al insertar correctamente
        for tiposCuerpo in self.Cuerpo:
            if (isinstance(tiposCuerpo, Cuerpo_TipoWhere)):
                print("Vamos a ver condiciones y luego a mostrar datos de las condiciones")
                resultado = Inter.procesar_expresion_select(tiposCuerpo.Cuerpo, ts_global)
                if resultado is None:
                    imprir("SELECT: No existen registros.")
                else:
                    for r in resultado:
                        print(">>"+str(r.valor))

            elif (isinstance(tiposCuerpo, GroupBy)):
                print("Vamos a ver los tipos de grupos a realizar ")
                # Recorremos diccionario
                # for item in listaGeneral:
                #    print("dfdsf")
            elif (isinstance(tiposCuerpo, OrderBy)):
                print("Vamos a ordenar  segun lo que venga ")





            elif (isinstance(tiposCuerpo, AccesoLimit)):
                print("Bamos a elegir el limite ")
                if (str(tiposCuerpo.Reservada).lower() == "offset"):
                    # codigo de offset
                    # Recorremos la lista General
                    print("Estoy entrando al Offset")
                    for nn in listaGeneral:
                        l = listaGeneral.get(nn)
                        # Recorro la lista dentro del diccionario
                        indice = 0
                        for dato in l:
                            if (indice < int(tiposCuerpo.Expresion_Numerica)):
                                print(">>>" + l.pop(0))
                                indice += 1
                elif (str(tiposCuerpo.Reservada).lower() == "limit"):
                    # Codigo de limit
                    if (str(tiposCuerpo.Expresion_Numerica).lower() == "all"):
                        print("Voy a retornar todo sin limite")
                    else:
                        # Recorremos la lista General
                        for nn in listaGeneral:
                            l = listaGeneral.get(nn)

                            # Recorro la lista dentro del diccionario
                            indice = 0
                            for dato in l:
                                if (indice < int(tiposCuerpo.Expresion_Numerica)):
                                    print(">>>"+l.pop())
                                    indice += 1

            elif (isinstance(tiposCuerpo, AccesoSubConsultas)):
                print("Bamos a ver el cuerpo de cada subconsulta")

        print(listaGeneral)

        mostrarConsulta(listaGeneral)
        listaGeneral.clear


# Con Distinct
# ---------------------------------------------------------------------------------------------------
class Select3(Instruccion):
    def __init__(self, distinct, unionn, Lista_Campos=[], Nombres_Tablas=[]):
        self.distinct = distinct
        self.Lista_Campos = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn = unionn

    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos

        if r is not None:

            for ee in self.Nombres_Tablas:

                if (isinstance(ee, AccesoTablaSinLista)):  # viene sin alias

                    ####Recorremos el diccionario general para ver si existe la tabla que queremos
                    # recorremos lista General de Tablas
                    for elemento2 in ts_global.Tablas:

                        x: CreateTable = ts_global.obtenerTabla(elemento2)
                        if (str(x.id) == str(ee.NombreT)):
                            # si es la tabla validamos que tipo de campo viene

                            for ii in self.Lista_Campos:
                                if (isinstance(ii,
                                               Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                    # *  , nombrecampo,  nombrecampo alias
                                    # listaGeneral
                                    for ele in x.cuerpo:  # recorremos lista de columnas
                                        y: CampoTabla = ele
                                        if (str(y.id) == str(ii.Columna)):

                                            ##Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            # comparamos si ya existe en la lista
                                                            miniB = False
                                                            for item in lista:
                                                                if str(item.valor) == str(t.valor):
                                                                    print(
                                                                        "------- METER EL OBJETOO COMPLETO DE DATOINSERT 1")
                                                                    miniB = True

                                                            if miniB == False:
                                                                lista.append(t)
                                                            else:
                                                                pass
                                                            # fin comparacion insert

                                                    listaGeneral[ii.Columna] = lista
                                                else:
                                                    print("")
                                            else:  # SI EL NOMBRE O ALIAS ESTA VACIO
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    # Recorremos lista de Campos

                                                    if (str(t.columna) == str(
                                                            ii.Columna)):  # COMPARAR CADA ATRIBUTO Y SI ES LA MISMA COLUMNA ALMACENAR
                                                        print(str(t.valor))

                                                        # comparamos si ya existe en la lista
                                                        miniB = False
                                                        for item in lista:
                                                            miI: DatoInsert = item
                                                            if str(miI.valor) == str(t.valor):
                                                                miniB = True

                                                        if miniB == False:
                                                            print(" SI ALMACENA: > " + str(t.valor))
                                                            lista.append(t)
                                                        else:
                                                            pass
                                                        # fin comparacion insert

                                                listaGeneral[ii.Columna] = lista
                                        elif (str(ii.Columna) == "*"):
                                            print("Vienen todo los datos de la tabla")

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                # comparamos si ya existe en la lista
                                                                miniB = False
                                                                for item in Lista2:
                                                                    if str(item.valor) == str(t.valor):
                                                                        print("--------YA ESTOY 2")
                                                                        miniB = True

                                                                if miniB == False:
                                                                    Lista2.append(t)
                                                                else:
                                                                    pass
                                                                # fin comparacion insert
                                                        listaGeneral[pp.id] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            # comparamos si ya existe en la lista
                                                            miniB = False
                                                            for item in Lista2:
                                                                if str(item.valor) == str(t.valor):
                                                                    print("--------YA ESTOY 3")
                                                                    miniB = True

                                                            if miniB == False:
                                                                Lista2.append(t)
                                                            else:
                                                                pass
                                                            # fin comparacion insert
                                                    listaGeneral[pp.id] = Lista2


                                        else:
                                            print("")

                                elif (isinstance(ii, Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                    # listaGeneral
                                    for ele in x.cuerpo:
                                        y: CampoTabla = ele

                                        if (y.id == ii.Columna):
                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores 4")

                                            # verificamos el alias

                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias

                                            print("ahora la columna se llama" + str(nuevoNave))

                                            # Bamos a sacar todos los datos coincidentes
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))
                                                            # comparamos si ya existe en la lista
                                                            miniB = False
                                                            for item in lista:
                                                                if str(item.valor) == str(t.valor):
                                                                    print("--------YA ESTOY 4")
                                                                    miniB = True

                                                            if miniB == False:
                                                                lista.append(t)
                                                            else:
                                                                pass
                                                            # fin comparacion insert
                                                    listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        # comparamos si ya existe en la lista
                                                        miniB = False
                                                        for item in lista:
                                                            if str(item.valor) == str(t.valor):
                                                                print("--------YA ESTOY 5")
                                                                miniB = True

                                                        if miniB == False:
                                                            lista.append(t)
                                                        else:
                                                            pass
                                                        # fin comparacion insert
                                                listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = lista


                                        elif (y.id == '*'):
                                            # Recorrer todos los datos de la columna
                                            print("Vienen todo los datos  los datos de esa columna")

                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                # comparamos si ya existe en la lista
                                                                miniB = False
                                                                for item in Lista2:
                                                                    if str(item.valor) == str(t.valor):
                                                                        print("--------YA ESTOY 6")
                                                                        miniB = True

                                                                if miniB == False:
                                                                    Lista2.append(t)
                                                                else:
                                                                    pass
                                                                # fin comparacion insert
                                                        listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            # comparamos si ya existe en la lista
                                                            miniB = False
                                                            for item in Lista2:
                                                                if str(item.valor) == str(t.valor):
                                                                    print("--------YA ESTOY 7")
                                                                    miniB = True

                                                            if miniB == False:
                                                                Lista2.append(t)
                                                            else:
                                                                pass
                                                            # fin comparacion insert
                                                    listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = Lista2
                                        else:
                                            print("")
                                else:
                                    print("Otros posibles tipos ")
                        else:
                            print(" LAS TABLAS NO SON CORRECTAS")

                # VIENE CON UN ALIAS
                elif (isinstance(ee, AccesoTabla)):  # viene con un alias

                    # verificamos el alias

                    AliasTabla = ee.Lista_Alias

                    # Tenemos el alias

                    AliasT = AliasTabla.Alias

                    # Recorremos el diccionario general para ver si existe la tabla que queremos

                    # recorremos lista General de Tablas

                    for elemento2 in ts_global.Tablas:

                        x: CreateTable = ts_global.obtenerTabla(elemento2)

                        if (str(x.id) == str(ee.NombreT)):

                            # si es la tabla validamos que tipo de campo viene

                            for ii in self.Lista_Campos:

                                if (isinstance(ii,Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias

                                    # *  , nombrecampo,  nombrecampo alias

                                    # listaGeneral

                                    for ele in x.cuerpo:  # recorremos lista de columnas

                                        y: CampoTabla = ele

                                        if (str(y.id) == str(ii.Columna)):

                                            print("LA columan " + str(

                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")

                                            # Bamos a sacar todos los datos coincidentes

                                            # recorremos datos

                                            # Vallidamos que la no venga sin datos

                                            if (ii.NombreT != ""):

                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):

                                                    i = ts_global.Datos

                                                    lista = []

                                                    for gg in ts_global.Datos:

                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))

                                                    listaGeneral[ii.Columna] = lista

                                                else:

                                                    print("")

                                            else:

                                                i = ts_global.Datos

                                                lista = []

                                                for gg in ts_global.Datos:

                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))

                                                listaGeneral[ii.Columna] = lista

                                        elif (str(ii.Columna) == "*"):

                                            print("Vienen todo los datos de la tabla")

                                            # Vallidamos que la no venga sin datos

                                            if (ii.NombreT != ""):

                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente

                                                    for columnas in x.cuerpo:

                                                        pp: CampoTabla = columnas

                                                        Lista2 = []

                                                        i = ts_global.Datos

                                                        for gg in i:

                                                            t: DatoInsert = ts_global.obtenerDato(gg)

                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))

                                                                Lista2.append(str(t.valor))

                                                        listaGeneral[pp.id] = Lista2

                                            # viene sin referencia a tabla

                                            else:

                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente

                                                for columnas in x.cuerpo:

                                                    pp: CampoTabla = columnas

                                                    Lista2 = []

                                                    i = ts_global.Datos

                                                    for gg in i:

                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))

                                                            Lista2.append(str(t.valor))

                                                    listaGeneral[pp.id] = Lista2

                                        else:

                                            print("")

                                elif (isinstance(ii,Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                    # listaGeneral

                                    for ele in x.cuerpo:

                                        y: CampoTabla = ele

                                        if (y.id == ii.Columna):

                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")

                                            # verificamos el alias

                                            ListaAlias = ii.Lista_Alias

                                            # Tenemos el alias

                                            nuevoNave = ListaAlias.Alias

                                            print("ahora la columna se llama" + str(nuevoNave))

                                            # Bamos a sacar todos los datos coincidentes

                                            # Vallidamos que la no venga sin datos

                                            if (ii.NombreT != ""):

                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):

                                                    i = ts_global.Datos

                                                    lista = []

                                                    for gg in ts_global.Datos:

                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))

                                                    listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = lista

                                                else:

                                                    print("")

                                            else:

                                                i = ts_global.Datos

                                                lista = []

                                                for gg in ts_global.Datos:

                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))

                                                listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = lista

                                        elif (y.id == '*'):

                                            # Recorrer todos los datos de la columna

                                            print("Vienen todo los datos  los datos de esa columna")

                                            ListaAlias = ii.Lista_Alias

                                            # Tenemos el alias

                                            nuevoNave = ListaAlias.Alias

                                            # Vallidamos que la no venga sin datos

                                            if (ii.NombreT != ""):

                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente

                                                    for columnas in x.cuerpo:

                                                        pp: CampoTabla = columnas

                                                        Lista2 = []

                                                        i = ts_global.Datos

                                                        for gg in i:

                                                            t: DatoInsert = ts_global.obtenerDato(gg)

                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))

                                                                Lista2.append(str(t.valor))

                                                        listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = Lista2

                                            # viene sin referencia a tabla

                                            else:

                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente

                                                for columnas in x.cuerpo:

                                                    pp: CampoTabla = columnas

                                                    Lista2 = []

                                                    i = ts_global.Datos

                                                    for gg in i:

                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))

                                                            Lista2.append(str(t.valor))

                                                    listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = Lista2
                                        else:
                                            print("")
                                else:
                                    print("Otros posibles tipos ")
                        else:
                            print("")
                else:

                    imprir("Viene otro tipo de accion ")
        else:
            imprir("SELECT : No existe la base de datos acual")

        # primero obtener la primera lista
        miCuenta = 0
        titulo = []
        alias = []
        primera = []
        for lista in listaGeneral:
            if miCuenta != 1:
                primera = listaGeneral.get(lista)
                miCuenta += 1
            break

        # obtener los titulos del punto a la izquierda esto_No.ESTO_SI
        for lista in listaGeneral:
            derecha = self.quitarIzq(lista)
            sinP = derecha.replace(".", "")
            titulo.append(str(sinP))

        # obtener los alias con punto
        for lista in listaGeneral:
            alias.append(str(lista))

        nuevoDic = {}
        resdistinct = []
        for reg in primera:  # [a, b, c]
            p: DatoInsert = reg
            for t in titulo:  # [carne, apellido]
                for dat in ts_global.Datos:  # Datos
                    de: DatoInsert = ts_global.obtenerDato(dat)
                    for titu in titulo:  # [carne, apellido]
                        if de.columna == titu:
                            if p.columna == t and p.fila == de.fila:
                                resdistinct.append(de)

        # ingreso lista final FALTA
        for t in titulo:
            lis = []
            for u in resdistinct:
                v = self.quitarIzq("asdddd")
                if u.columna == t:
                    lis.append(u.valor)
            nuevoDic[t] = lis

        print(nuevoDic)
        #mostrarConsulta(nuevoDic)

        mostrarConsulta(nuevoDic)
        nuevoDic.clear()
        listaGeneral.clear()

    def quitarIzq(self,Cadena):
        resultado = ""
        punto = False
        for letra in Cadena:
            if letra == '.':
                punto= True

            if punto == True:
                resultado += letra

        if punto == False:
            return Cadena
        else:
            return resultado

    def quitarDer(self,Cadena):
        resultado = ""
        punto = True
        for letra in Cadena:
            if letra == '.':
                punto= False

            if punto == True:
                resultado += letra

        return resultado




#---------------------------------------------------------------------------------------------------
class Select4(Instruccion) :
    def __init__(self,distinct,  unionn,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.distinct = distinct
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn
        self.Cuerpo = Cuerpo

    def Ejecutar(self):
        print("Ejecutando  Select ")





#subSelect sin cuerpo
#---------------------------------------------------------------------------------------------------

class SubSelect(Instruccion) :
    def __init__(self, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas

#subSelect con cuerpo
#---------------------------------------------------------------------------------------------------
class SubSelect2(Instruccion) :
    def __init__(self,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.Cuerpo = Cuerpo

#subSelect sin cuerpo con distict
#---------------------------------------------------------------------------------------------------

class SubSelect3(Instruccion) :
    def __init__(self,Distict, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Distict       = Distict
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas

#subSelect con cuerpo con distict
#---------------------------------------------------------------------------------------------------
class SubSelect4(Instruccion) :
    def __init__(self,Distict,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Distict       = Distict
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.Cuerpo = Cuerpo







# Campos Accedidos
#---------------------------------------------------------------------------------------------------

#Campos Accedidos por Lista
class Campo_Accedido(Instruccion): #Nombre.columna  Lista_Posible

    def __init__(self, NombreT, Columna, Lista_Alias=[]):
        self.NombreT       = NombreT
        self.Columna       = Columna
        self.Lista_Alias   = Lista_Alias

    def Ejecutar(self):
        print("")

#Campos Accedidos por Lista
class Campo_AccedidoSinLista(Instruccion): #Nombre.columna  Lista_Posible

    def __init__(self, NombreT, Columna):
        self.NombreT       = NombreT
        self.Columna       = Columna

#---------------------------------------------------------------------------------------------------
#Nombre Tabla Accedidos
#---------------------------------------------------------------------------------------------------

class AccesoTabla(Instruccion): #Tabla Lista

    def __init__(self, NombreT,Lista_Alias=[]):
        self.NombreT     = NombreT
        self.Lista_Alias = Lista_Alias

#Accediendo sin lista
class AccesoTablaSinLista(Instruccion): #Tabla

    def __init__(self, NombreT):
        self.NombreT     = NombreT

#---------------------------------------------------------------------------------------------------

#Campos Accedidos desde Group By
#---------------------------------------------------------------------------------------------------

class AccesoGroupBy(Instruccion): #Tabla Lista

    def __init__(self, NombreT,Columna,Estado,Lista_Alias=[]):
        self.NombreT      = NombreT
        self.Columna      = Columna
        self.Lista_Alias  = Lista_Alias
        self.Estado = Estado



#---------------------------------------------------------------------------------------------------



# Campos Limit
#---------------------------------------------------------------------------------------------------

class AccesoLimit(Instruccion):

    def __init__(self,Reservada,Expresion_Numerica):
        self.Reservada = Reservada
        self.Expresion_Numerica  =  Expresion_Numerica


#Campos Accedidos desde Las Subconsultas
#---------------------------------------------------------------------------------------------------

class AccesoSubConsultas(Instruccion):

    def __init__(self, AnteQuery=[],Query=[],Lista_Alias=[]):
        self.AnteQuery      = AnteQuery
        self.Query          = Query
        self.Lista_Alias  = Lista_Alias


#---------------------------------------------------------------------------------------------------

#Campos de los unions
#---------------------------------------------------------------------------------------------------

class CamposUnions(Instruccion):
    def __init__(self,Reservada,Comportamiento,Consulta=[]):
        self.Reservada      = Reservada
        self.Comportamiento = Comportamiento
        self.Consulta       = Consulta


# Alias
#---------------------------------------------------------------------------------------------------
#Alias Campos
#---------------------------------------------------------------------------------------------------

#Alias Campos sin lista
class Alias_Campos_ListaCamposSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias
#Alias Tablas
#---------------------------------------------------------------------------------------------------
#Alias campos Sin Lista
class Alias_Table_ListaTablasSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias
#Alias Group By
#---------------------------------------------------------------------------------------------------
#Alias campos Sin Lista
class Alias_Tablas_GroupSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias

#Alias SUB QUERYS
#---------------------------------------------------------------------------------------------------
class Alias_SubQuerysSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias

# FIN ALIAS
#---------------------------------------------------------------------------------------------------


#Cuerpo Consulta
#---------------------------------------------------------------------------------------------------
#where Condiciones

class Cuerpo_Condiciones(Instruccion):
    def __init__(self,Cuerpo=[]):
        self.Cuerpo = Cuerpo

#Cuerpo Tipo Where condiciones
#---------------------------------------------------------------------------------------------------
class Cuerpo_TipoWhere(Instruccion):
    def __init__(self,Cuerpo=[]):
        self.Cuerpo = Cuerpo
#TIPOS DE GROUP BY
#---------------------------------------------------------------------------------------------------
#Group By  Con Having y condiciones
class GroupBy(Instruccion):
    def __init__(self,Lista_Campos=[],Condiciones=[]):
        self.Lista_Campos = Lista_Campos
        self.Condiciones  = Condiciones


#Group By  Con Having y condiciones
class OrderBy(Instruccion):
    def __init__(self,Lista_Campos=[],Condiciones=[]):
        self.Lista_Campos = Lista_Campos
        self.Condiciones  = Condiciones


#TIPOS DE CASES
#---------------------------------------------------------------------------------------------------
class CaseCuerpo(Instruccion):
    def __init__(self,Cuerpo,Lista_When=[]):
        self.Lista_When = Lista_When
        self.Cuerpo     = Cuerpo
class ExpresionesCase(Instruccion):
    def __init__(self,Reservada,ListaExpresiones=[]):
        self.Reservada            = Reservada
        self.ListaExpresiones     = ListaExpresiones

class TiposWhen(Instruccion):
    def __init__(self,Reservada,Reservada2,Reservada3,ListaExpresiones1=[],ListaExpresiones2=[],ListaExpresiones3=[]):
        self.Reservada    = Reservada
        self.Reservada2   = Reservada2
        self.Reservada3   = Reservada3
        self.ListaExpresiones1 = ListaExpresiones1
        self.ListaExpresiones2 = ListaExpresiones2
        self.ListaExpresiones3 = ListaExpresiones3


#---------------------------------------------------------------------------------------------------

#INSERTAR DATOS CESAR
class DatoInsert(Instruccion):
    def __init__(self, bd, tabla, columna, valor, fila):
        self.bd = bd
        self.tabla = tabla
        self.columna = columna
        self.valor = valor
        self.fila = fila




class Insert_Datos(Instruccion):
    def __init__(self, id_table, valores):
        self.id_table = id_table
        self.valores = valores

    def Ejecutar(self):
        FilaG = randint(1,500)
        print("Ejecucion")
        global ts_global, baseActual
        global LisErr
        r = ts_global.obtenerBasesDatos(baseActual)

        if r is None:
            imprir("INSERT BD:  No existe la BD para insertar.")
        else:
            imprir("INSERT BD:  Si existe la BD para insertar. " + str(self.id_table[0].val))

            r2:CreateTable = ts_global.obtenerTabla(self.id_table[0].val)
            if r2 is None:
                imprir("INSERT BD:  No existe la Tabla para insertar.")
            else:

                imprir("INSERT BD:  Si existe la Tabla para insertar. ")

                # Obtener tabla actual
                rT:CreateTable = ts_global.obtenerTabla(self.id_table[0].val)
                #print(">>>>>>>"+str(rT.id))

                temporal:CampoTabla = rT.cuerpo

                cC = 0
                for c in rT.cuerpo:
                    cC += 1

                cV = 0
                for v in self.valores:
                    cV += 1

                if cC == cV:
                    #print(" >> Parametros exactos.")
                    index = 0
                    banderaInsert = False

                    for cc in self.valores:

                        if isinstance(temporal[index].tipo, valorTipo):

                            resultado = Inter.procesar_expresion(cc, None)
                            print(" Mi proceso: "+str(resultado))
                            if isinstance(resultado, string_types) and (str(temporal[index].tipo.valor).upper() == 'VARCHAR' or str(temporal[index].tipo.valor).upper() == 'CHARACTER' or str(temporal[index].tipo.valor).upper() == 'CHAR'):
                                print(" >>> Parametros correctos, insertar, Validar la exprecion.")
                                banderaInsert = True
                            else:
                                imprir("INSERT BD: Parametros incorrectos. ")
                                banderaInsert = False
                        else:
                            resultado = Inter.procesar_expresion(cc, None)
                            print(" Mi proceso: "+str(resultado))
                            #print(" Valor: >>>" + str(cc.val))
                            if isinstance(resultado, string_types) and  str(temporal[index].tipo).upper() == 'TEXT' or str(temporal[index].tipo).upper() == 'DATE':
                                print(" >>> Parametros correctos, insertar")
                                banderaInsert = True
                            elif str(temporal[index].tipo) == 'BOOLEAN'and (str(cc.val).upper() == "TRUE" or str(cc.val).upper() == "FALSE"):
                                imprir("INSERT BD: Parametros correctos, insertar")
                                banderaInsert = True
                            elif int(resultado) > 0 and (str(temporal[index].tipo).upper() == 'SMALLINT' or str(temporal[index].tipo).upper() == 'INTEGER' or str(temporal[index].tipo).upper() == 'INT' or str(temporal[index].tipo).upper() == 'BIGINT' or str(temporal[index].tipo).upper() == 'DECIMAL' or str(temporal[index].tipo).upper() == 'REAL' or str(temporal[index].tipo).upper() == 'FLOAT' or str(temporal[index].tipo).upper() == 'MONEY'):
                                print(" >>> Parametros correctos, insertar")
                                banderaInsert = True
                            else:
                                imprir("INSERT BD: Parametros incorrectos. ")
                                banderaInsert = False

                        index += 1

                    # INSERTANDO DATOS
                    ix = 0
                    if banderaInsert is True:
                        listaTemp = []

                        for ccc in self.valores:
                            resultado = Inter.procesar_expresion(ccc, None)
                            d = DatoInsert(baseActual, r2.id, str(temporal[ix].id), resultado, FilaG)
                            ts_global.agregarDato(d)
                            listaTemp.append(resultado)
                            ix += 1

                        sr = Master.insert(baseActual, str(self.id_table[0].val), listaTemp)
                        print(baseActual + str(self.id_table[0].val) + str(len(listaTemp)))
                        if sr is 0:
                            imprir("INSERT BD:  Insert realizado con exito.")
                        else:
                            imprir("INSERT BD:  No se realizo el insert.")
                else:
                    imprir("INSERT BD:  Parametros insuficientes.")

# ***************************** CREATE TABLE Y INHERITS ****************************************
class Inherits(Instruccion):
    def __init__(self, id):
        self.id = id


class CreateTable(Instruccion):
    def __init__(self, id, cuerpo, inhe):
        self.id = id
        self.cuerpo = cuerpo
        self.inhe = inhe

    def Ejecutar(self):
        global ts_global, baseActual
        global LisErr

        # SI la tabla ya existe en el diccionario.
        r = ts_global.obtenerTabla(self.id)

        if r is None:
            imprir("INSERT BD: Creando tabla. ")

            # se cuenta el numero de columnas
            columnas = 0

            for campos in self.cuerpo:
                columnas += 1
            print("---------------")
            print(baseActual)
            print(columnas)

            rM = Master.createTable(baseActual, self.id, columnas)

            if rM == 0:
                ts_global.agregarTabla(self)
                print(" > Se creo la tabla en la base de datos.")

            elif rM == 1:
                print("> 1")
                er =  ErrorRep('Semantico', 'No se encontro el archivo data.',0)
                LisErr.agregar(er)

            elif rM == 2:
                print("> 2")
                er =  ErrorRep('Semantico', 'No existe la base de datos actual.',0)
                LisErr.agregar(er)

            elif rM == 3:
                print( "> 3")
                er =  ErrorRep('Semantico', 'La tabla ya existe en la base de datos.',0)
                LisErr.agregar(er)
        else:
            imprir("INSERT BD: La tabla ya esta en la TS. ")
            er = ErrorRep('Semantico', 'La tabla ya existe en la base de datos.', 0)
            LisErr.agregar(er)

# --------------------------------------------------------
class CampoTabla(Instruccion):
    def __init__(self, id, tipo, validaciones):
        self.id = id
        self.tipo = tipo
        self.validaciones = validaciones

#---------------------------------------------------------
class CampoValidacion(Instruccion):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor

#---------------------------------------------------------------------------------------------------
class Delete_Datos(Instruccion):
    def __init__(self, id_table, valore_where):
        self.id_table = id_table
        self.valore_where = valore_where

    def Ejecutar(self):
        global ts_global, baseActual, ListaTablasG
        global LisErr

        ListaTablasG.append(self.id_table[0].val)
        rb = ts_global.obtenerBasesDatos(baseActual)
        if rb is None:
            imprir("DELETE: No existe la base de datos. ")
            er = ErrorRep('Semantico', 'No existe la base de datos indicada.', 0)
            LisErr.agregar(er)
        else:
            rt = ts_global.obtenerTabla(self.id_table[0].val)
            if rt is None:
                imprir("DELETE: No existe la tabla de datos. ")
                er = ErrorRep('Semantico', 'No existe la tabla indicada.', 0)
                LisErr.agregar(er)
            else:
                resultado = Inter.procesar_expresion(self.valore_where, ts_global)
                listaEliminar = []
                # recorrer lista de valores a eliminar.
                if len(resultado) is 0:
                    imprir("DELETE: No existen registros.")
                    er = ErrorRep('Semantico', 'No existen registros que cumplan la condicion para eliminar.', 0)
                    LisErr.agregar(er)
                else:
                    for i in resultado:
                        ii:DatoInsert = i

                        #recorrer tabla de simbolos.
                        for item in ts_global.Datos:
                            v: DatoInsert = ts_global.obtenerDato(item)
                            bandera = False
                            if str(ii.fila) == str(v.fila):

                                for p in listaEliminar:
                                    if item == p:
                                        bandera = True
                                    else:
                                        bandera = False

                                if bandera is False:
                                    listaEliminar.append(item)

                    for d in listaEliminar:
                        r = ts_global.EliminarDato(d)
                        if r is None:
                            pass
                        else:
                            pass
                    imprir(" DELETE: Se eliminaron los registros.")
# --------------------------------------------------------------------------------------------------
class constraintTabla(Instruccion):
    def __init__(self, valor, id, condiciones, listas_id, referencia, idRef):
        self.valor = valor
        self.id = id
        self.condiciones = condiciones
        self.listas_id = listas_id
        self.referencia = referencia
        self.idRef = idRef





class CreateDataBase(Instruccion):
    def __init__(self, replace, exists, idBase, idOwner, Modo ):
        self.replace = replace
        self.exists = exists
        self.idBase = idBase
        self.idOwner = idOwner
        self.Modo = Modo


    def Ejecutar(self):
        global ts_global, baseActual
        global LisErr,Ejecucion

        if self.replace == "":
            r = ts_global.obtenerBasesDatos(self.idBase)
            if r is None:
                rM = Master.createDatabase(str(self.idBase))
                imprir("CREATE DB:  Base de datos creada con exito!")
                if rM == 0:
                    ts_global.agregarBasesDatos(self)
                    print(" > Base de datos creada con exito!")
                elif rM == 1 or rM == 2:
                    print("> Base de datos ya existe.")
                    er = ErrorRep('Semantico', 'La Base de datos ya existe', 0)
                    LisErr.agregar(er)
            else:
                print("Si encontre la BD. ")
                imprir("CREATE DB:  La Base de Datos No se Creo ya que existe!")
                er = ErrorRep('Semantico', 'La Base de datos ya existe', 0)
                LisErr.agregar(er)
        else:
            r = ts_global.obtenerBasesDatos(self.idBase)
            if r is None:

                rM = Master.createDatabase(str(self.idBase))
                imprir("CREATE DB:    Base de datos creada con exito!")
                baseActual = str(self.idBase)
                baseN.append(self.idBase)
                if rM == 0:
                    ts_global.agregarBasesDatos(self)
                    print(" > Base de datos creada con exito!")
                elif rM == 1 or rM == 2:
                    print("> Base de datos ya existe Se va a Reemplazar ")
            else:
                imprir("CREATE DB:  Se encontro la BD Bamos a Reemplazar!")
                Lista.clear();
                Lista.append(Ejecucion)
                print("Si encontre la BD. Bamos a Reemplazar la Misma! ")



class ShowDatabases(Instruccion):
    def __init__(self, cadenaLike):
        self.cadenaLike = cadenaLike

    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion
        #idDB = self.cadenaLike.replace("\"","")

        r  = Master.showDatabases()
        if r  is not None:  #si lo encuentra
            for element in r:
                print(str(element))
                imprir("SHOW DB:>"+ str(element))
        else:
            imprir("SHOW DB: No se encontro la BD")
            er = ErrorRep('Semantico', 'No Encontre la Base de Datos', 0)
            LisErr.agregar(er)





class AlterDataBase(Instruccion):
    def __init__(self, idDB, opcion):
        self.idDB = idDB
        self.opcion = opcion

    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion


        c1 = False
        c2 = False
        error=""

        opcion  = self.opcion.replace("\"", "")
        opcionf = self.opcion.replace("\'", "")

        r =  ts_global.obtenerBasesDatos(self.idDB)
        r2 = ts_global.obtenerBasesDatos(opcionf)

        if r is not None:  #si lo encuentra
            c1 = True
        else:
            error += "No se Encontro la Base De datos "
        if r2 is  None:  #No Esta el Nombre para definirlo en la bd
            c2 = True
        else:
            error += "  Se encontro el Valor a Setear"

        if (c1 and c2):
            print("Excelente se puede editar")
            #Editamos nuestro diccionario
            ts_global.actualizarCreateDataBase(str(self.idDB),str(self.opcion))
            imprir("ALTER DB: Edicion base de Datos Exitosa!")
            #Editamos en base de datos fisica
            rM = Master.alterDatabase(str(self.idDB),str(self.opcion))
            if rM==2:
                print("No se encuentra la BD")
            elif rM==3:
                print("Ya se encuentra la BD con el nombre a tratar")
            elif rM==1:
                print("Verificar Ocurrio Error Al editar")
            elif rM==0:
                print("Se Edito la Base de Datos con exito")
            else:
                print( "No llega nunca pero por si las moscas ")
        else:
            print("No encontre la BD.")
            imprir("ALTER DB:  No se encontro la base de datos! :( ")
            er = ErrorRep('Semantico', error, 0)
            LisErr.agregar(er)





class DropDataBase(Instruccion):

    def __init__(self, id, existe):
        self.id = id
        self.existe = existe



    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion

        r = ts_global.obtenerBasesDatos(self.id)

        if r == None:  #si lo encuentra
            imprir("DROP DB:  No se encontro la base de datos! :( ")
            er = ErrorRep('Semantico', 'No Encontre la Base de Datos', 0)
            LisErr.agregar(er)
        else:
            ts_global.EliminarBD(str(self.id))
            imprir("DROP DB:  Se elimino correctamente la base de Datos! :) ")
            rM = Master.dropDatabase(str(self.id))
            if rM==0:
                print("Exito")
            elif rM==1:
                print("Fracaso al escribir en bd")
            elif rM==2:
                print("No existe el elemento en la BD")
            else:
                print("No llega nunca pero por si las moscas")

# Crear funciones de ejecucion ----------------------------------
class SelectExtract(Instruccion):
    def __init__(self, tipoTiempo, cadenaFecha):
        self.tipoTiempo = tipoTiempo
        self.cadenaFecha = cadenaFecha

    def Ejecutar(self):
        pass


class SelectDatePart(Instruccion):
    def __init__(self, cadena, cadenaIntervalo):
        self.cadena = cadena
        self.cadenaIntervalo = cadenaIntervalo

class SelectTipoCurrent(Instruccion):
    def __init__(self, tipoCurrent):
        self.tipoCurrent = tipoCurrent

class SelectStamp(Instruccion):
    def __init__(self, cadena):
        self.cadena = cadena

class Selectnow(Instruccion):
    def __init__(self, constru):
        self.constru = constru

class CreacionEnum(Instruccion):
    def __init__(self, listaCadenas):
        self.listaCadenas = listaCadenas
# Crear funciones de ejecucion ----------------------------------

#Prueba clase errores
class ErrorSintactico():
    def __init__(self, valor, error, linea):
        self.valor = valor
        self.error = error
        self.linea = linea

    def imprimirError(self):
        return " Error " + str(self.error) + ", no se esperaba el token: " + str(self.valor) + ", Linea: " + str(self.linea)

#---------------------------------------------------------------------------------------------------
class Update_Datos(Instruccion):
    def __init__(self, id_table, valores_set, valor_where):
        self.id_table = id_table
        self.valores_set = valores_set
        self.valor_where = valor_where


    def Ejecutar(self):
        global ts_global, baseActual, ListaTablasG
        global LisErr

        ListaTablasG.append(self.id_table[0].val)
        rb = ts_global.obtenerBasesDatos(baseActual)
        if rb is None:
            imprir("UPDATE: No existe la base de datos.")
            er = ErrorRep('Semantico', 'No existe la base de datos.', 0)
            LisErr.agregar(er)
        else:
            rt = ts_global.obtenerTabla(self.id_table[0].val)
            if rt is None:
                imprir("UPDATE: No existe la tabla indicada.")
                er = ErrorRep('Semantico', 'No existe la tabla indicada.', 0)
                LisErr.agregar(er)
            else:
                resultado = Inter.procesar_expresion(self.valor_where, ts_global)
                listaUpdate = []
                if len(resultado) is 0:
                    imprir("UPDATE: No existen registros.")
                    er = ErrorRep('Semantico', 'No existen registros que cumplan la condicion para actualizar.', 0)
                    LisErr.agregar(er)
                else:
                    listaSet = []
                    # Valores SET
                    for i in self.valores_set:
                        p: ExpresionAritmetica = i
                        listaSet.append(p)

                    # recorrer lista de valores a actualizar.
                    for i in resultado:
                        ii:DatoInsert = i

                        #recorrer tabla de simbolos.
                        for item in ts_global.Datos:
                            v: DatoInsert = ts_global.obtenerDato(item)
                            bandera = False
                            if str(ii.fila) == str(v.fila):
                                for p in listaUpdate:
                                    if item == p:
                                        bandera = True
                                    else:
                                        bandera = False

                                if bandera is False:
                                    listaUpdate.append(v)

                    for i in listaUpdate:
                        ii: DatoInsert = i
                        for s in listaSet:
                            ss: ExpresionAritmetica = s
                            if str(ss.exp1.id) == str(ii.columna):
                                ii.valor = str(ss.exp2.val)
                            else:
                                pass
                imprir("UPDATE: Se actualizaron los registros.")




#Clase para el Alter Table----------------------------
class Alter_Table_AddColumn(Instruccion):
    def __init__(self, id_table, id_columnas):
        self.id_table = id_table
        self.id_columnas = id_columnas

        """ def Ejecutar(self):
        #Verificar que existe la base de datos
        #Verificar que existe la tabla
        #Verificar que existe la columna en la tabla
        global ts_global, baseActual
        global LisErr
        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)
            print(self.id_table)



            if r2 is not None:

                for elemento in self.id_columnas:


                    if isinstance(elemento,ExpresionValor2):

                        rc =  Master.alterAddColumn(baseActual,self.id_table,elemento.val)

                        if rc == 0:

                            #Se ingreso correctamente el valor
                            temporal2 = CampoValidacion(None, None)
                            temporal  = CampoTabla(elemento.val, elemento.tipo, temporal2)
                            r2.cuerpo.append(temporal)


                            for elemento in ts_global.Tablas:
                                x:CreateTable = ts_global.obtenerTabla(elemento)
                                for ele in x.cuerpo:
                                    y:CampoTabla  = ele
                                    print(y.id+"<<<<<<<<<<<<<<<<<<<<<<")
                            imprir("ALTER TABLE: Se Agrego correctamente la Columna")
                        elif rc==1:
                            #Error al escribir en la base de datos
                            imprir("ALTER TABLE: Error al Escribir en la Base de Datos")
                        elif rc==2:
                            #No esta la base de datos  en las listas
                            imprir("ALTER TABLE: No existe la BD")
                        elif rc==3:
                            #no esta la tabla en la base de datos
                            imprir("ALTER TABLE: La tabla no existe en la BD")
                        else:
                            #Error logico
                            imprir("ALTER TABLE: Error logico en la operacion")
                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            #colocar error semantico
            """

    def Ejecutar(self):
        # Verificar que existe la base de datos
        # Verificar que existe la tabla
        # Verificar que existe la columna en la tabla
        global ts_global, baseActual
        global LisErr
        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2: CreateTable = ts_global.obtenerTabla(self.id_table)
            print(self.id_table)

            if r2 is not None:

                for elemento in self.id_columnas:

                    if isinstance(elemento, ExpresionValor2):

                        bandera = False
                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if(x.id == self.id_table):

                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    if (y.id != elemento.val):
                                        bandera = True
                            else:
                                print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")


                        if bandera == True:

                            rc = Master.alterAddColumn(baseActual, self.id_table, elemento.val)

                            if rc == 0:
                                # Se ingreso correctamente el valor
                                temporal2 = CampoValidacion(None, None)
                                temporal = CampoTabla(elemento.val, elemento.tipo, temporal2)
                                r2.cuerpo.append(temporal)

                                # Recorrido de elementos
                                for elemento in ts_global.Tablas:
                                    x: CreateTable = ts_global.obtenerTabla(elemento)
                                    for ele in x.cuerpo:
                                        y: CampoTabla = ele
                                        print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")

                                imprir("ALTER TABLE: Se Agrego correctamente la Columna")
                            elif rc == 1:
                                # Error al escribir en la base de datos
                                imprir("ALTER TABLE: Error al Escribir en la Base de Datos")
                            elif rc == 2:
                                # No esta la base de datos  en las listas
                                imprir("ALTER TABLE: No existe la BD")
                            elif rc == 3:
                                # no esta la tabla en la base de datos
                                imprir("ALTER TABLE: La tabla no existe en la BD")
                            else:
                                # Error logico
                                imprir("ALTER TABLE: Error logico en la operacion")

                        else:
                            imprir("ALTER TABLE: La columna a insertar ya existe ")

                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")


class Alter_COLUMN(Instruccion):
    def __init__(self, idtabla,columnas):
        self.idtabla = idtabla
        self.columnas = columnas

    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2: CreateTable = ts_global.obtenerTabla(self.idtabla)

            if r2 is not None:


                for tt in self.columnas:

                    if isinstance(tt, ExpresionValor2):


                        #recorremos lista General de Tablas
                        for elemento2 in ts_global.Tablas:

                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if (x.id == self.idtabla):
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele

                                    print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")
                                    if (y.id == tt.val):

                                        y.tipo = tt.tipo
                                        imprir("ALTER TABLE: Se Actualizo correctamente El Tipo de Dato")
                                    else:
                                        print("")
                            else:
                                print("")

                        # imprimir valores actualizados
                        # for elemento2 in ts_global.Tablas:
                        #    x: CreateTable = ts_global.obtenerTabla(elemento2)
                        #    for ele in x.cuerpo:
                        #        y: CampoTabla = ele
                        #       print(y.id + "<<<<<<<<<<<<<<<<<<<<<< EEEEEEEEEEEE")

                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
                else:
                    imprir("ALTER TABLE:   La tabla no existe!   ")
            else:
                imprir("ALTER TABLE:   La Base de datos no existe")
                # colocar error semantico








class Alter_Table_Drop_Column(Instruccion):
    def __init__(self, id_table, columnas):
        self.id_table = id_table
        self.columnas = columnas


    def Ejecutar(self):

        #Verificar que existe la base de datos
        #Verificar que existe la tabla
        #Verificar que existe la columna en la tabla

        global ts_global, baseActual
        global LisErr
        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)

            if r2 is not None:

                for elemento in self.columnas:

                    if isinstance(elemento,ExpresionValor):
                        #Agarramos el valor de la lista de elementos
                        #Recorremos para buscar la columna en la lista
                          contador=0
                          for elemento2 in ts_global.Tablas:
                             x:CreateTable = ts_global.obtenerTabla(elemento2)

                             if(x.id == self.id_table):

                                 for ele in x.cuerpo:
                                   y:CampoTabla  = ele
                                   print(y.id+"<<<<<<<<<<<<<<<<<<<<<<")

                                   if (y.id==elemento.val):
                                       contador += 1

                                       #mandamos a eliminar y verificamos la respuesta
                                       print(str(baseActual)+str(self.id_table)+str(contador))
                                       rc = Master.alterDropColumn(str(baseActual), str(self.id_table), int(contador))
                                       if rc == 0:
                                           # Se elimino correctamente el elemento
                                           #Eliminamos de nuestro diccionario
                                           r2.cuerpo.remove(y.id)
                                           imprir("ALTER TABLE: Se Elimino correctamente la Columna")
                                       elif rc == 1:
                                           # Error al escribir en la base de datos
                                           imprir("ALTER TABLE: Error al Eliminar en la Base de Datos")
                                       elif rc == 2:
                                           # No esta la base de datos  en las listas
                                           imprir("ALTER TABLE: No existe la BD")
                                       elif rc == 3:
                                           # no esta la tabla en la base de datos
                                           imprir("ALTER TABLE: La tabla no existe en la BD")
                                       elif rc == 4:
                                           # no esta la tabla en la base de datos
                                           imprir("ALTER TABLE: La Columna no esta ")

                                       elif rc == 5:
                                           # no esta la tabla en la base de datos
                                           imprir("ALTER TABLE: Excedio los Limites ")

                                       else:
                                           # Error logico
                                           imprir("ALTER TABLE: Error logico en la operacion")
                                   else:
                                       contador+=1

                             else:
                                 print("Next!")

                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            #colocar error semantico


class Alter_Table_Rename_Column(Instruccion):
    def __init__(self, id_table, old_column, new_column):
        self.id_table = id_table
        self.old_column = old_column
        self.new_column = new_column

    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)

            if r2 is not None:

                elementoo  = self.old_column
                elementoo2 = self.new_column

                if isinstance(elementoo, ExpresionValor) and isinstance(elementoo2, ExpresionValor):

                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if(x.id == self.id_table):
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")
                                    if (y.id == elementoo.val):
                                        y.id = elementoo2.val
                                        imprir("ALTER TABLE: Se Actualizo correctamente la Columna")
                                    else:
                                        print("")
                            else:
                                print("")
                        #imprimir valores actualizados
                        #for elemento2 in ts_global.Tablas:
                        #    x: CreateTable = ts_global.obtenerTabla(elemento2)
                        #    for ele in x.cuerpo:
                        #        y: CampoTabla = ele
                        #       print(y.id + "<<<<<<<<<<<<<<<<<<<<<< EEEEEEEEEEEE")

                else:
                    imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            # colocar error semantico


class Alter_Table_Drop_Constraint(Instruccion):
    def __init__(self, id_table, id_constraint):
        self.id_tabla = id_table
        self.id_constraint = id_constraint


    def Ejecutar(self):
        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)

            if r2 is not None:

                elementoo  = self.id_constraint

                if isinstance(elementoo, ExpresionValor):

                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if(x.id == self.id_tabla):
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")
                                    if (y.id == elementoo.val):

                                        for validacion in y.validaciones:
                                            validacion:CampoValidacion
                                            if validacion.valor=="CONSTRAINT_UNIQUE":
                                                validacion.valor = " "
                                                imprir("ALTER TABLE: CONSTRAINT ELIMINADO CORRECTAMENTE")
                                    else:
                                        print("")
                            else:
                                print("")


                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if(x.id == self.id_tabla):
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    if (y.id == elementoo.val):

                                        for validacion in y.validaciones:
                                            validacion: CampoValidacion
                                            print("VALIDACIONES CAMPO >>>>"+str(validacion.id)+"<->"+str(validacion.valor))
                                    else:
                                        print("")
                            else:
                                print("")

                elif isinstance(elementoo,constraintTabla):




                    for elemento2 in ts_global.Tablas:

                        x: CreateTable = ts_global.obtenerTabla(elemento2)
                        if (x.id == self.id_tabla):

                            for ele in x.cuerpo:

                                y: CampoTabla = ele

                                if (y.id == elementoo.val):

                                    for validacion in y.validaciones:
                                        validacion:constraintTabla

                                        validacion.valor      = None
                                        validacion.id         = None
                                        validacion.condiciones= None
                                        validacion.listas_id  = None
                                        validacion.referencia = None
                                        validacion.idRef      = None


                                        imprir("ALTER TABLE: CONSTRAINT ELIMINADO CORRECTAMENTE")
                                else:
                                    print("")
                        else:
                            print("")


                    for elemento2 in ts_global.Tablas:
                        x: CreateTable = ts_global.obtenerTabla(elemento2)

                        if (x.id == self.id_tabla):
                            for ele in x.cuerpo:
                                y: CampoTabla = ele

                                if (y.id == elementoo.val):
                                    for validacion in y.validaciones:
                                        validacion:constraintTabla
                                        var="VALIDACIONES CAMPO >>>>"+str(validacion.valor)+str(validacion.id)+str(validacion.condiciones )+str(validacion.listas_id  )+str(validacion.referencia  )+str(validacion.idRef)
                                        print(var)
                                else:
                                    print("")
                        else:
                            print("")
                else:
                    imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            # colocar error semantico


class Alter_table_Alter_Column_Set(Instruccion):
    def __init__(self, id_table, id_column):
        self.id_tabla = id_table
        self.id_column = id_column
    def Ejecutar(self):
        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)

            if r2 is not None:

                elementoo  = self.id_constraint

                if isinstance(elementoo, ExpresionValor):

                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if x.id == self.id_tabla:
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")
                                    if (y.id == elementoo.val):

                                        bandera = False
                                        for validacion in y.validaciones:
                                            validacion:CampoValidacion

                                            if validacion.id == "NOT" and validacion.valor=="NULL":
                                                imprir("ALTER TABLE: YA TIENE LA VALIDACION NOT NULL")
                                                bandera= True

                                        if(bandera==False):
                                            # Se ingreso correctamente el valor
                                            temporal2 = CampoValidacion("NOT", "NULL")
                                            y.validaciones.append(temporal2)
                                            imprir("ALTER TABLE: SE SETEO NOT NULL CORRECTAMENTE")
                                    else:
                                        print("")

                            else:
                                print("")


                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if x.id == self.id_tabla:

                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    if (y.id == elementoo.val):

                                        for validacion in y.validaciones:
                                            validacion: CampoValidacion
                                            print("VALIDACIONES CAMPO >>>>"+str(validacion.id)+"<->"+str(validacion.valor))
                                    else:
                                        print("")
                            else:
                                print("")
                else:
                    imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            # colocar error semantico


class Alter_table_Add_Foreign_Key(Instruccion):
    def __init__(self, id_table, id_column, id_column_references):
        self.id_table = id_table
        self.id_column = id_column
        self.id_column_references = id_column_references


    def Ejecutar(self):
        #Verificar que existe la base de datos
        #Verificar que existe la tabla
        #Verificar que existe la columna en la tabla
        global ts_global, baseActual
        global LisErr
        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)
            print(self.id_table)



            if r2 is not None:

                    elemento       = self.id_column
                    elemento2      = self.id_column_references
                    tipoReferencia = "";


                    if isinstance(elemento,ExpresionValor) and isinstance(elemento,ExpresionValor):


                        bandera = False
                        bandera2 = False

                        for elemento22 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento22)

                            if x.id == self.id_table:
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele

                                    if y.id != elemento2.val:
                                        bandera=True
                                    if y.id == elemento.val:
                                        bandera2=True
                                        tipoReferencia=y.tipo


                                if (bandera==True) and (bandera2 ==True):
                                        # Se ingreso correctamente el valor
                                        #validar que exista ese esa columna en alguna tabla
                                        temporal2 = constraintTabla("FOREIGN KEY",elemento.val,None,None, None,elemento2.val)
                                        temporal = CampoTabla(elemento2.val,tipoReferencia, temporal2)
                                        r2.cuerpo.append(temporal)
                                        imprir("ALTER TABLE: En Hora Buena Se Ingreso la Llave Foranea Correctamente")
                                else:
                                    imprir("ALTER TABLE: No se Ejecuto la Accion ")
                            else:
                                print("")
                        else:
                            imprir("ALTER TABLE: La columna a insertar ya existe ")

                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            #colocar error semantico


class Alter_Table_Add_Constraint(Instruccion):
    def __init__(self, id_table, id_constraint, id_column):
        self.id_table = id_table
        self.id_constraint = id_constraint
        self.id_column = id_column

    def Ejecutar(self):
        global ts_global, baseActual
        global LisErr
        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)
            print(self.id_table)



            if r2 is not None:

                    elemento       = self.id_constraint
                    elemento2      = self.id_column

                    tipoReferencia = "";


                    if isinstance(elemento,ExpresionValor) and isinstance(elemento,ExpresionValor):


                        bandera = False
                        bandera2 = False

                        for elemento22 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento22)

                            if x.id == self.id_table:

                                for ele in x.cuerpo:
                                    y: CampoTabla = ele

                                    if y.id == elemento2.val:
                                        bandera=True
                                        tipoReferencia = y.tipo

                                    if y.id != elemento.val:
                                        bandera2=True

                                if (bandera==True) and (bandera2 ==True):
                                        # Se ingreso correctamente el valor
                                        #validar que exista ese esa columna en alguna tabla
                                        temporal2 = constraintTabla("UNIQUE",elemento2.val,None,None, None,elemento.val)
                                        temporal = CampoTabla(elemento.val,tipoReferencia, temporal2)
                                        r2.cuerpo.append(temporal)
                                        imprir("ALTER TABLE: En Hora Buena Se Ingreso El Constraint UNIQUE")


                                else:
                                    imprir("ALTER TABLE: No se Ejecuto la Accion ")
                            else:
                                print("")
                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            #colocar error semantico

class useClase(Instruccion):
    def __init__(self,id):
        self.id = id