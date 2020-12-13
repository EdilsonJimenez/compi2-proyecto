from Instruccion import *
from graphviz import Digraph
from graphviz import escape
from expresiones import *
class Ast2:

    def __init__(self, sentencias):
        self.i = 0
        self.sentencias = sentencias

    def inc(self):
        global i
        self.i += 1

    def crearReporte(self):
        global dot

        dot = Digraph('AST', format='png', filename='c:/source/ast.gv')
        dot.attr('node', shape='box', color='#31CEF0')
        dot.node('Node' + str(self.i), '"AST"')
        dot.edge_attr.update(arrowhead='none')
        self.recorrerInstrucciones(self.sentencias, 'Node' + str(self.i))
        dot.render('AST', format='png', view=True)
        print('Hecho')





    def recorrerInstrucciones(self, sente, padre):
        for i in sente:
            #VIENE UN DROP TABLE
            if isinstance(i, DropTable):
                print("Si es un drop table *" + i.id)
                self.grafoDropTable(i.id, padre)

            elif isinstance(i, Select):
                print("Es Una Instruccion Select")
                self.GrafoSelect(i.Lista_Campos,i.Nombres_Tablas,i.unionn,padre)

            elif isinstance(i, Insert_Datos):
                print("Si es un drop Insert *")
                self.grafoInsert_Data(i.id_table,i.valores, padre)
            #-----------------------------------
            elif isinstance(i, Campo_Accedido):
                print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.grafoCampoAccedido(i.NombreT, i.Columna)

            elif isinstance(i, CreateTable):
                self.grafoCreateTable(i.id, i.cuerpo, i.inhe, padre)

            elif isinstance(i, CreateDataBase):
                self.grafoCreateDataBase(i.replace, i.exists, i.idBase, i.idOwner ,i.Modo, padre)

            else:
                print("No es droptable")



    def grafoDropTable(self, id, padre):
        global dot
        self.inc();

        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "DROP TRABLE")
        dot.edge(padre, 'Node' + str(self.i))
        self.inc();
        dot.node('Node' + str(self.i), id)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))





    # CAMPOS ACCEDIDOS
    # ----------------------------------------------------------------------------------------------------------

    # Objeto Que Accede A este Tipo "Campo_Accedido"
    # Campos Accedidos Con Lista
    def GrafoCampo_Accedido(self, NombreT, Columna, Lista_Alias, padre):
        global dot
        # NombreT.Campo Lista
        if ((NombreT != "") and (Columna != "") and (Lista_Alias != False )):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))

        # Campo Lista
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias != False)):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # Recorrer la lista de alias
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
        else:
            print("Error Sintactico")



        #Objeto Que Accede A este Tipo "Campo_AccedidoSinLista"
        # Campos Accedidos Sin Lista
    def GrafoCampo_AccedidoSinLista(self, NombreT, Columna, padre):
        global dot
         # NombreT.Campo
        if ((NombreT != "") and (Columna != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        # Campo
        elif ((NombreT == "") and (Columna != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        else:
            print("Error Sintactico")





    # NOMBRE TABLAS ACCEDIDOS
    # ----------------------------------------------------------------------------------------------------------


    #Objeto Que accede "AccesoTabla"
    #Nombres Lista Accedidos  Con lista
    def GrafoAccesoTabla(self, NombreT, Lista_Alias, padre):
        global dot
        if ((NombreT != "") and (Lista_Alias != False)):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Nombre_Tabla")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # Verificar el Tipo que viene
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))

        else:
            print("Error sintactico")


    #Objeto Que accede "AccesoTablaSinLista"
    #Nombres Lista Accedidos  Sin lista
    def GrafoAccesoTablaSinLista(self, NombreT, padre):
        global dot
        # Nombre
        if ((NombreT != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Nombre_Tabla")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        else:
            print("Error sintactico")





    # ALIAS CAMPOS
    # ----------------------------------------------------------------------------------------------------------

    #Objeto que tiene Acceso "Alias_Campos_ListaCampos"
    #Acceso a los Campos Con lista
    def GrafoAlias_Campos_ListaCampos(self, Alias, Lista_Sentencias, padre):
        global dot

        # as Alias , Lista    and    alias, lista
        if ((Alias != "") and (Lista_Sentencias != False)):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "As")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Alias)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "Lista_Sentencias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListadeCampos(Lista_Sentencias, 'Node' + str(self.i))

        # Lista
        elif ((Alias == "") and (Lista_Sentencias != False)):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), ",")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "Lista_Sentencias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.RecorrerListadeCampos(Lista_Sentencias, 'Node' + str(self.i))
        else:
           print("Verificar Errores Sintacticos")



    #Objeto que tiene Acceso "Alias_Campos_ListaCamposSinLista"
    #Acceso a los Campos Sin lista
    def GrafoAlias_Campos_ListaCamposSinLista(self, Alias, padre):
        global dot

        # as Alias
        if ((Alias != "") ):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "As")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Alias)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        else:
           print("Verificar Errores Sintacticos")













    # ALIAS Tablas
    # ----------------------------------------------------------------------------------------------------------

    #Objeto que tiene acceso "Alias_Table_ListaTablas"
    #Acceso a Alias de las Tablas Con Lista
    def GrafoAlias_Table_ListaTablas(self, Alias, Lista_Sentencias, padre):
        global dot

        # as Alias , Lista    and    alias, lista
        if ((Alias != "") and (Lista_Sentencias != False)):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "As")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Alias)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "Tabla")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListadeNombres(Lista_Sentencias, 'Node' + str(self.i))

        # Lista
        elif ((Alias == "") and (Lista_Sentencias != False)):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), ",")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "Tabla")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListadeNombres(Lista_Sentencias, 'Node' + str(self.i))



    #Objeto que tiene acceso "Alias_Table_ListaTablasSinLista"
    #Acceso a Alias de las Tablas Sin Lista
    def GrafoAlias_Table_ListaTablasSinLista(self, Alias, padre):
        global dot

        # as Alias
        if (Alias != "" ):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "As")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Alias)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        else:
            print("Verificar Errores Sintacticos")









    # Recorrido de la lista de Campos
    # ----------------------------------------------------------------------------------------------------------

    def RecorrerListadeCampos(self, Campos, padre):
        for i in Campos:
            if isinstance(i, Campo_Accedido):
                print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.GrafoCampo_Accedido(i.NombreT, i.Columna, i.Lista_Alias, padre)

            elif isinstance(i, Campo_AccedidoSinLista):
                print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.GrafoCampo_AccedidoSinLista(i.NombreT, i.Columna, padre)

            else:
                print("No Ningun Tipo")






    # Recorrido de la lista de Nombres de Tablas
    # ----------------------------------------------------------------------------------------------------------

    def RecorrerListadeNombres(self, Nombres, padre):
        for i in Nombres:

            if isinstance(i, AccesoTabla):
                print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.GrafoAccesoTabla(i.NombreT, i.Lista_Alias, padre)

            elif isinstance(i, AccesoTablaSinLista):
                print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.GrafoAccesoTablaSinLista(i.NombreT, padre)
            else:
                print("No Ningun Tipo")

    # Recorrido de los Alias
    # ----------------------------------------------------------------------------------------------------------


    def RecorrerTiposAlias(self, Lista_Alias, padre):
        i = Lista_Alias
        # Alias de los Campos
        if isinstance(i, Alias_Campos_ListaCampos):
            print("Es un Campo Accedido Por la Tabla" + i.NombreT)
            self.GrafoAlias_Campos_ListaCampos(i.NombreT, i.Lista_Alias, padre)

        # Alias de las Nombres de las Tablas
        if isinstance(i, Alias_Table_ListaTablas):
            print("Es un Campo Accedido Por la Tabla" + i.NombreT)
            self.GrafoAlias_Table_ListaTablas(i.NombreT, i.Lista_Alias, padre)
        else:
            print("No Ningun Tipo")



    def grafoDropTable(self, id, padre):
        global dot, i

        self.inc()
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "DROP TABLE")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc()
        dot.node('Node' + str(self.i), id)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


    def RecorrerTiposAlias(self, Lista_Alias, padre):
        print("Verificando tipos de alias")
        # Alias de los Campos
        print("Verificando tipos de alias")
        i=Lista_Alias
        if isinstance(i, Alias_Campos_ListaCampos):
            print("Es un Campo Accedido Por la Tabla" + i.Alias)
            self.GrafoAlias_Campos_ListaCampos(i.Alias, i.Lista_Sentencias, padre)

        # Alias de los Campos Sin Lista
        elif isinstance(i, Alias_Campos_ListaCamposSinLista):
           print("Es un Campo Accedido Por la Tabla" + i.Alias)
           self.GrafoAlias_Campos_ListaCamposSinLista(i.Alias, padre)

           # Alias de las Nombres de las Tablas
        elif isinstance(i, Alias_Table_ListaTablas):
            print("Es un Campo Accedido Por la Tabla" + i.Alias)
            self.GrafoAlias_Table_ListaTablas(i.Alias, i.Lista_Sentencias, padre)

        # Alias de las Nombres de las Tablas Sin Lista
        elif isinstance(i, Alias_Table_ListaTablasSinLista):
            print("Es un Campo Accedido Por la Tabla" + i.Alias)
            self.GrafoAlias_Table_ListaTablasSinLista(i.Alias, padre)
        else:
            print("No Ningun Tipo")


    # Instruccion SELECT
    # ----------------------------------------------------------------------------------------------------------

    def GrafoSelect(self, ListaCampos, NombresTablas, Uniones, padre):
        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION_SELECT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "SELECT")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_CAMPOS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeCampos(ListaCampos, 'Node' + str(self.i));

        self.inc();
        dot.node('Node' + str(self.i), "FROM")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_TABLAS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeNombres(NombresTablas, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), Uniones)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))







# ----------------------------------------------------------------------------------------------------------
# ----------------------- GRAFO DROP TABLE-------------------------------------------------------------------
    def grafoDropTable(self, id, padre):
        global dot, i

        self.inc()
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "DROP TABLE")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc()
        dot.node('Node' + str(self.i), id)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR INSERTAR-------------------------------------------------------------------
    def grafoInsert_Data(self, id, valores, padre):
        global  dot,tag,i

        self.inc()
        nuevoPadre=self.i
        dot.node('Node'+str(self.i),"INSERT")
        dot.edge(padre,'Node'+str(self.i))

        self.inc();
        nuevoPadre2 = self.i
        dot.node('Node'+str(self.i),"ID TABLA")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))

        for i in id:
            self.inc();
            dot.node('Node'+  str(self.i), i.val)
            dot.edge('Node' + str(nuevoPadre2),'Node'+str(self.i))

        self.inc();
        nuevoPadre3 = self.i
        dot.node('Node'+str(self.i),"VALORES TABLA")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))
       #GRAFICANDO EXPRESION===========================
        for i in valores:
            print("valores")
            print(i)
            self.inc();
            dot.node('Node'+  str(self.i), "VALOR NUEVO")
            dot.edge('Node' + str(nuevoPadre3),'Node'+str(self.i))
            #LLAMAMOS A GRAFICAR EXPRESION
            padrenuevo4 = self.i
            self.graficar_expresion(i)
            self.inc()
            dot.edge('Node'+str(padrenuevo4),str(padrenuevo4+1))


#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR EXPRESION-----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

    def graficar_expresion(self, expresiones):
        global  dot,tag,i
        if isinstance(expresiones,ExpresionAritmetica):
            self.graficar_arit_log_rel_bb(expresiones,"Aritmetica")
        elif isinstance(expresiones,ExpresionRelacional) :
            self.graficar_arit_log_rel_bb(expresiones,"Relacional")
        elif isinstance(expresiones,ExpresionLogica) :
            self.graficar_arit_log_rel_bb(expresiones,"Logica")
        elif isinstance(expresiones,UnitariaNegAritmetica) :
            self.graficarUnaria(expresiones,"NegAritmetica")
        elif isinstance(expresiones,UnitariaLogicaNOT) :
            self.graficarUnaria(expresiones,"LogicaNOT")
        elif isinstance(expresiones,UnitariaNotBB) :
            self.graficarUnaria(expresiones,"NotBB")
        elif isinstance(expresiones,ExpresionValor) :
            self.inc()
            padreID=self.i
            dot.node(str(padreID),'ExpresionValor')
            dot.edge(str(padreID),str(padreID+1))
            self.inc()
            padreID=self.i
            dot.node(str(padreID),str(expresiones.val))
        elif isinstance(expresiones, UnariaReferencia) :
            self.inc()
            padreID=self.i
            dot.node(str(padreID),' ExpresionReferencia')
            dot.edge(str(padreID),str(padreID+1))
            self.inc()
            padreID=self.i
            dot.node(str(padreID),expresiones.tipoVar.id)
        # elif isinstance(expresiones,'PARENTESIS FALTA'):
        #     self.inc()
        #     padreID=self.i
        #     dot.node(str(padreID),'( valor )')
        #     dot.edge(str(padreID),str(padreID+1))
        #     self.graficar_expresion(expresiones.variable)


    def graficar_arit_log_rel_bb(self,expresion,tipo_exp="") :
        global  dot,tag,i
        self.inc()
        padreID=self.i
        padre=padreID
        dot.node(str(padreID),'Expresion'+tipo_exp)
        self.inc()
        padreID=self.i
        dot.node(str(padreID),'exp1')
        dot.edge(str(padre),str(padreID))
        dot.edge(str(padreID),str(padreID+1))
        self.graficar_expresion(expresion.exp1)
        self.inc()
        padreID=self.i
        dot.node(str(padreID),self.getVar(expresion.operador))
        dot.edge(str(padre),str(padreID))
        self.inc()
        padreID=self.i
        dot.node(str(padreID),'exp2')
        dot.edge(str(padre),str(padreID))
        dot.edge(str(padreID),str(padreID+1))
        self.graficar_expresion(expresion.exp2)

    def graficarUnaria(self,expresion,tipo_exp=""):
        self.inc()
        padreID=self.i
        dot.node(str(padreID),'Expresion'+tipo_exp)
        dot.edge(str(padreID),str(padreID+1))
        if isinstance(expresion,UnitariaNegAritmetica):
            self.graficar_expresion(expresion.exp)
        else:
            self.graficar_expresion(expresion.expresion)

    def getVar(self, padreID):
        if padreID==OPERACION_ARITMETICA.MAS:
            return '+'
        elif padreID==OPERACION_ARITMETICA.MENOS:
            return '-'
        elif padreID==OPERACION_ARITMETICA.MULTI:
            return '*'
        elif padreID==OPERACION_ARITMETICA.DIVIDIDO:
            return '/'
        elif padreID==OPERACION_ARITMETICA.RESIDUO:
            return '%'
        elif padreID==OPERACION_LOGICA.AND:
            return 'AND'
        elif padreID==OPERACION_LOGICA.OR:
            return 'OR'
        elif padreID==OPERACION_RELACIONAL.IGUALQUE:
            return '=='
        elif padreID==OPERACION_RELACIONAL.DISTINTO:
            return '!='
        elif padreID==OPERACION_RELACIONAL.MAYORIGUAL:
            return '>='
        elif padreID==OPERACION_RELACIONAL.MENORIGUAL:
            return '!='
        elif padreID==OPERACION_RELACIONAL.MAYORQUE:
            return '>'
        elif padreID==OPERACION_RELACIONAL.MAYORQUE:
            return '<'
        else:
            return 'op'
#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR CREATE TABLE-------------------------------------------------------------------
    def grafoCreateTable(self, id, cuerpo, inher, padre):
        global dot, i

        self.inc()
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "CREATE TABLE")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc()
        dot.node('Node' + str(self.i), 'Id: '+id)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        for k in cuerpo:
            if isinstance(k, CampoTabla):
                self.grafoCampoTabla(k, nuevoPadre)
            elif isinstance(k, constraintTabla):
                print("* Graficar CONTRAINTS")
                self.grafoConstraintTabla(k, nuevoPadre)


        # Graficar INHERITS DE CREATE TABLE
        if inher is not None:
            print("Si tiene un inher")
            self.grafoInhertis(inher.id, nuevoPadre)
        else:
            print("No tiene inherits")

    def grafoConstraintTabla(self, contraint:constraintTabla, padre):
        global dot, i

        '''CONSTRAINTS OPTIONS: '''

        self.inc();
        nuevop = self.i
        dot.node('Node' + str(self.i), "CONSTRAINT:")
        dot.edge('Node' + str(padre), 'Node' + str(self.i))

        if contraint.valor != None:
            self.inc()
            dot.node('Node' + str(self.i), 'Valor: '+str(contraint.valor))
            dot.edge('Node' + str(nuevop), 'Node' + str(self.i))

        if contraint.id != None:
            self.inc()
            dot.node('Node' + str(self.i), 'Id: ' + str(contraint.id))
            dot.edge('Node' + str(nuevop), 'Node' + str(self.i))

        if contraint.condiciones != None:
            for i in contraint.condiciones:
                print(i)
                self.inc();
                dot.node('Node' + str(self.i), "VALOR NUEVO")
                dot.edge('Node' + str(nuevop), 'Node' + str(self.i))
                # LLAMAMOS A GRAFICAR EXPRESION
                padrenuevo4 = self.i
                self.graficar_expresion(i)
                self.inc()
                dot.edge('Node' + str(padrenuevo4), str(padrenuevo4 + 1))

        if contraint.listas_id != None:
            self.inc()
            miP = self.i
            dot.node('Node' + str(self.i), 'COLUMNA')
            dot.edge('Node' + str(nuevop), 'Node' + str(self.i))
            self.grafoListaIDs(contraint.listas_id, miP)

        if contraint.idRef != None:
            self.inc()
            dot.node('Node' + str(self.i), 'ID TABLA REF: ' + str(contraint.idRef))
            dot.edge('Node' + str(nuevop), 'Node' + str(self.i))

        if contraint.referencia != None:
            self.inc()
            miP = self.i
            dot.node('Node' + str(self.i), 'COLUMNA REFERENCIA')
            dot.edge('Node' + str(nuevop), 'Node' + str(self.i))
            self.grafoListaIDs(contraint.referencia, miP)

    def grafoListaIDs(self, lista : ExpresionValor, padre):
        for v in lista:
            self.inc();
            dot.node('Node'+ str(self.i), str(v.val))
            dot.edge('Node' + str(padre), 'Node'+str(self.i))

    def grafoCampoTabla(self, campo, padre):
        global dot, i

        self.inc();
        nuevop = self.i
        dot.node('Node' + str(self.i), "CAMPO")
        dot.edge('Node' + str(padre), 'Node' + str(self.i))

        self.inc()
        dot.node('Node' + str(self.i), 'Id: '+str(campo.id))
        dot.edge('Node' + str(nuevop), 'Node' + str(self.i))

        self.inc()
        dot.node('Node' + str(self.i), 'Tipo: '+str(campo.tipo))
        dot.edge('Node' + str(nuevop), 'Node' + str(self.i))

        for k in campo.validaciones:
            if isinstance(k, CampoValidacion):
                if k.id != None and k.valor != None:
                    self.grafoCampoValidaciones(k, nuevop)
                elif k.id != None and k.valor == None:
                    self.grafoCampoValidaciones(k, nuevop)

    def grafoCampoValidaciones(self, validacion, padre):
        global dot, i

        self.inc();
        nuevop = self.i
        dot.node('Node' + str(self.i), "VALIDACION")
        dot.edge('Node' + str(padre), 'Node' + str(self.i))

        if (validacion.valor == None):
            self.inc()
            dot.node('Node' + str(self.i), str(validacion.id))
            dot.edge('Node' + str(nuevop), 'Node' + str(self.i))
        else:
            self.inc()
            dot.node('Node' + str(self.i), str(validacion.id)+' '+str(validacion.valor))
            dot.edge('Node' + str(nuevop), 'Node' + str(self.i))

    def grafoInhertis(self, id, padre):
        global dot, i

        self.inc();
        nuevop = self.i
        dot.node('Node' + str(self.i), "INHERITS")
        dot.edge('Node' + str(padre), 'Node' + str(self.i))

        self.inc()
        dot.node('Node' + str(self.i), 'Id: '+id)
        dot.edge('Node' + str(nuevop), 'Node' + str(self.i))

    def grafoCreateDataBase(self, replace, exists, idBase, idOwner, Modo, padre):
        global dot, i

        self.inc()
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "CREATE DATABASE")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc()
        dot.node('Node' + str(self.i), 'Id: '+ idBase)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        if replace == 1:
            self.inc()
            dot.node('Node' + str(self.i), 'Or Replace')
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        if exists == 1:
            self.inc()
            dot.node('Node' + str(self.i), 'If Not Exists')
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        if idOwner != 0:
            self.inc()
            dot.node('Node' + str(self.i), 'Owner: ' + str(idOwner))
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        if Modo != 0:
            self.inc()
            dot.node('Node' + str(self.i), 'Mode: ' + str(Modo))
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
# ----------------------------------------------------------------------------------------------------------

# def GrafoAccesoTabla(self,NombreT,Columna,padre):

#    self.contador+1
#    rootActual = self.contador
#    self.c +='Node'+str(self.contador)+ '[label="Campo"]\n'
#     self.c +='Node'+ padre + '->'+'Node'+str(self.contador)+';\n'
#  self.contador+1
# self.c +='Node'+str(self.contador)+'[label="'+NombreT+]
