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
                print("Si es un drop table *")
                self.grafoDropTable(i.id, padre)

            elif isinstance(i, Select):
                print("Es Una Instruccion Select")
                self.GrafoSelect(i.Lista_Campos,i.Nombres_Tablas,i.unionn,padre)

            elif isinstance(i, Select2):
                print("Es Una Instruccion Select")
                self.GrafoSelect2(i.Lista_Campos,i.Nombres_Tablas,i.Cuerpo,i.unionn,padre)

            elif isinstance(i, Insert_Datos):
                print("Si es un drop Insert *")
                self.grafoInsert_Data(i.id_table,i.valores, padre)
            #-----------------------------------
            elif isinstance(i, Campo_Accedido):
                print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.grafoCampoAccedido(i.NombreT, i.Columna)

            elif isinstance(i, CreateTable):
                self.grafoCreateTable(i.id, i.cuerpo, i.inhe, padre)

            elif isinstance(i, Delete_Datos):
                print("Es Una Instruccion Delete")
                self.grafoDelete_Data(i.id_table,i.valore_where,padre)

            elif isinstance(i, Update_Datos):
                print("Es Una Instruccion Update")
                self.grafoUpdate__Data(i.id_table,i.valores_set,i.valor_where,padre)

            elif isinstance(i, Alter_Table_AddColumn):
                print("Es Una Instruccion Alter Add Column")
                self.grafoAlter_AddColumn(i.id_table,i.id_columnas,padre)

            else:
                print("No es droptable")



    


    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------
    # INSTRUCCIONES NECESARIAS PARA LOS SELECT
    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------


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


    # Grafo Where con Expreciones
    # ----------------------------------------------------------------------------------------------------------
    # Where Expreciones
    def GrafoCuerpo_Condiciones(self,Lista,padre):
        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "Cuerpo")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "Where")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.Recorrer_Condiciones(Lista, 'Node' + str(nuevoPadre))



    #Recorremos Expresion y mandamos el nodo aumentando el padre
    def Recorrer_Condiciones(self,Lista,padre):

        # GRAFICANDO EXPRESION===========================
            i = Lista
            self.inc();
            dot.node('Node' + str(self.i), "CONDICION")
            dot.edge(padre, 'Node' + str(self.i))

            # LLAMAMOS A GRAFICAR EXPRESION
            padrenuevo = self.i
            self.graficar_expresion(i)
            self.inc()
            dot.edge('Node' + str(padrenuevo), str(padrenuevo + 1))


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


    # Recorrido del Cuerpo
    # ----------------------------------------------------------------------------------------------------------
    def RecorrerCuerpo(self, Cuerpo, padre):
        i=Cuerpo
        if isinstance(i, Cuerpo_Condiciones):
            print("Es un Campo Accedido Por la Cuerpo ")
            self.GrafoCuerpo_Condiciones(i.Cuerpo, padre)
        else:
            print("No hay Ningun Tipo")








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


    def GrafoSelect2(self,ListaCampos, NombresTablas,cuerpo, Uniones, padre ):
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
        dot.node('Node' + str(self.i), "CUERPO")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.RecorrerCuerpo(cuerpo, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), Uniones)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))










    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------
    # FIN DE INSTRUCCIONES NECESARIAS PARA LOS SELECT
    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------








# ----------------------------------------------------------------------------------------------------------
# ----------------------- GRAFO DROP TABLE-------------------------------------------------------------------
    def grafoDropTable(self, id, padre):
        global  dot,tag,i

        self.inc()
        nuevoPadre=self.i
        dot.node('Node'+str(self.i),"DROP_TABLE")
        dot.edge(padre,'Node'+str(self.i))

        self.inc();
        nuevoPadre2 = self.i
        dot.node('Node'+str(self.i),"ID TABLA")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))

        for i in id:
            self.inc();
            dot.node('Node'+  str(self.i), i.val)
            dot.edge('Node' + str(nuevoPadre2),'Node'+str(self.i))

        

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
        #NUEVAS UNITARIAS
        
        #----------------------------------------
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
        if expresion.exp1 and expresion.exp2:
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
        elif  expresion.exp2 == None:
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
        #NUEVAS COSAS
        elif padreID==OPERACION_LOGICA.IS_NOT_NULL:
            return 'IS_NOT_NULL'
        elif padreID==OPERACION_LOGICA.IS_NOT_TRUE:
            return 'IS_NOT_TRUE'
        elif padreID==OPERACION_LOGICA.IS_NOT_FALSE:
            return 'IS_NOT_FALSE'
        elif padreID==OPERACION_LOGICA.IS_NOT_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID==OPERACION_LOGICA.IS_NULL:
            return 'IS_NULL'
        elif padreID==OPERACION_LOGICA.IS_TRUE:
            return 'IS_TRUE'
        elif padreID==OPERACION_LOGICA.IS_FALSE:
            return 'IS_FALSE'
        elif padreID==OPERACION_LOGICA.IS_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID==OPERACION_LOGICA.IS_NOT_DISTINCT:
            return 'IS_NOT_DISTINCT'
        elif padreID==OPERACION_LOGICA.IS_DISTINCT:
            return 'IS_DISTINCT'
        elif padreID==FUNCION_NATIVA.ABS:
            return 'ABS'
        elif padreID==FUNCION_NATIVA.CBRT:
            return 'CBRT'
        elif padreID==FUNCION_NATIVA.CEIL:
            return 'CEIL'
        elif padreID==FUNCION_NATIVA.CEILING:
            return 'CEILING'
        elif padreID==FUNCION_NATIVA.DEGREES:
            return 'DEGREES'
        elif padreID==FUNCION_NATIVA.EXP:
            return 'EXP'
        elif padreID==FUNCION_NATIVA.FACTORIAL:
            return 'FACTORIAL'
        elif padreID==FUNCION_NATIVA.FLOOR:
            return 'FLOOR'
        elif padreID==FUNCION_NATIVA.LN:
            return 'LN'
        elif padreID==FUNCION_NATIVA.LOG:
            return 'LOG'
        elif padreID==FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID==FUNCION_NATIVA.RADIANS:
            return 'RADIANS'
        elif padreID==FUNCION_NATIVA.ROUND:
            return 'ROUND'
        elif padreID==FUNCION_NATIVA.SIGN:
            return 'SIGN'
        elif padreID==FUNCION_NATIVA.SQRT:
            return 'SQRT'
        elif padreID==FUNCION_NATIVA.TRUNC:
            return 'TRUNC'
        elif padreID==FUNCION_NATIVA.ACOS:
            return 'ACOS'
        elif padreID==FUNCION_NATIVA.ACOSD:
            return 'ACOSD'
        elif padreID==FUNCION_NATIVA.ASIN:
            return 'ASIN'
        elif padreID==FUNCION_NATIVA.ASIND:
            return 'ASIND'
        elif padreID==FUNCION_NATIVA.ATAN:
            return 'ATAN'
        elif padreID==FUNCION_NATIVA.ATAND:
            return 'ATAND'
        elif padreID==FUNCION_NATIVA.COS:
            return 'COS'
        elif padreID==FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID==FUNCION_NATIVA.COT:
            return 'COT'
        elif padreID==FUNCION_NATIVA.COTD:
            return 'COTD'
        elif padreID==FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID==FUNCION_NATIVA.SIN:
            return 'SIN'
        elif padreID==FUNCION_NATIVA.SIND:
            return 'SIND'
        elif padreID==FUNCION_NATIVA.TAN:
            return 'TAN'
        elif padreID==FUNCION_NATIVA.TAND:
            return 'TAND'
        elif padreID==FUNCION_NATIVA.SINH:
            return 'SINH'
        elif padreID==FUNCION_NATIVA.COSH:
            return 'COSH'
        elif padreID==FUNCION_NATIVA.TANH:
            return 'TANH'
        elif padreID==FUNCION_NATIVA.ASINH:
            return 'ASINH'
        elif padreID==FUNCION_NATIVA.ACOSH:
            return 'ACOSH'
        elif padreID==FUNCION_NATIVA.ATANH:
            return 'ATANH'
        elif padreID==FUNCION_NATIVA.LENGTH:
            return 'LENGTH'
        elif padreID==FUNCION_NATIVA.TRIM:
            return 'TRIM'
        elif padreID==FUNCION_NATIVA.MD5:
            return 'MD5'
        elif padreID==FUNCION_NATIVA.SHA256:
            return 'SHA256'
        elif padreID==FUNCION_NATIVA.DIV:
            return 'DIV'
        elif padreID==FUNCION_NATIVA.GCD:
            return 'GCD'
        elif padreID==FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID==FUNCION_NATIVA.POWER:
            return 'POWER'
        elif padreID==FUNCION_NATIVA.ATAN2:
            return 'ATAN2'
        elif padreID==FUNCION_NATIVA.ATAN2D:
            return 'ATAN2D'
        elif padreID==FUNCION_NATIVA.GET_BYTE:
            return 'GET_BYTE'
        elif padreID==FUNCION_NATIVA.ENCODE:
            return 'ENCODE'
        elif padreID==FUNCION_NATIVA.DECODE:
            return 'DECODE'

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

        # Graficar INHERITS DE CREATE TABLE
        if inher is not None:
            print("Si tiene un inher")
            self.grafoInhertis(inher.id, nuevoPadre)
        else:
            print("No tiene inherits")

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
                if (k.id != None and k.valor !=None):
                    self.grafoCampoValidaciones(k, nuevop)

    def grafoCampoValidaciones(self, validacion, padre):
        global dot, i

        self.inc();
        nuevop = self.i
        dot.node('Node' + str(self.i), "Validacion:")
        dot.edge('Node' + str(padre), 'Node' + str(self.i))

        self.inc()
        dot.node('Node' + str(self.i), 'Id: '+str(validacion.id))
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

# ----------------------------------------------------------------------------------------------------------

# def GrafoAccesoTabla(self,NombreT,Columna,padre):

#    self.contador+1
#    rootActual = self.contador
#    self.c +='Node'+str(self.contador)+ '[label="Campo"]\n'
#     self.c +='Node'+ padre + '->'+'Node'+str(self.contador)+';\n'
#  self.contador+1
# self.c +='Node'+str(self.contador)+'[label="'+NombreT+]



#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR DELETE-------------------------------------------------------------------
    def grafoDelete_Data(self, id, valores, padre):
        global  dot,tag,i

        self.inc()
        nuevoPadre=self.i
        dot.node('Node'+str(self.i),"DELETE")
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
        dot.node('Node'+str(self.i),"WHERE")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))
       #GRAFICANDO EXPRESION===========================
        i = valores
        self.inc();
        dot.node('Node'+  str(self.i), "VALOR CONDICION")
        dot.edge('Node' + str(nuevoPadre3),'Node'+str(self.i))
        #LLAMAMOS A GRAFICAR EXPRESION
        padrenuevo4 = self.i
        self.graficar_expresion(i)
        self.inc()
        dot.edge('Node'+str(padrenuevo4),str(padrenuevo4+1))
       

#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR UPDATE-------------------------------------------------------------------
    def grafoUpdate__Data(self, id, valores_set,valores, padre):
        global  dot,tag,i

        self.inc()
        nuevoPadre=self.i
        dot.node('Node'+str(self.i),"UPDATE")
        dot.edge(padre,'Node'+str(self.i))

        self.inc();
        nuevoPadre2 = self.i
        dot.node('Node'+str(self.i),"ID TABLA")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))

        for i in id:
            self.inc();
            dot.node('Node'+  str(self.i), i.val)
            dot.edge('Node' + str(nuevoPadre2),'Node'+str(self.i))
        
        
        #GRAFICAR============VALORES DEL SET======================
        self.inc();
        nuevoPadre3 = self.i
        dot.node('Node'+str(self.i),"SET")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))
       #GRAFICANDO EXPRESION===========================
        for i in valores_set:
            self.inc();
            dot.node('Node'+  str(self.i), "VALOR CONDICION SET")
            dot.edge('Node' + str(nuevoPadre3),'Node'+str(self.i))
            #LLAMAMOS A GRAFICAR EXPRESION
            padrenuevo4 = self.i
            self.graficar_expresion(i)
            self.inc()
            dot.edge('Node'+str(padrenuevo4),str(padrenuevo4+1))

        #GRAFICAR============VALORES DEL WHERE======================
        self.inc();
        nuevoPadre3 = self.i
        dot.node('Node'+str(self.i),"WHERE")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))
       #GRAFICANDO EXPRESION===========================
        i = valores
        self.inc();
        dot.node('Node'+  str(self.i), "VALOR CONDICION WHERE")
        dot.edge('Node' + str(nuevoPadre3),'Node'+str(self.i))
        #LLAMAMOS A GRAFICAR EXPRESION
        padrenuevo4 = self.i
        self.graficar_expresion(i)
        self.inc()
        dot.edge('Node'+str(padrenuevo4),str(padrenuevo4+1))



#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR ALTER TABLE ADD COLUM-------------------------------------------------------------------
    def grafoAlter_AddColumn(self, id_tablas,id_columnas, padre):
        global  dot,tag,i

        self.inc()
        nuevoPadre=self.i
        dot.node('Node'+str(self.i),"ALTER TABLE ADD COLUMN")
        dot.edge(padre,'Node'+str(self.i))

        self.inc();
        nuevoPadre2 = self.i
        dot.node('Node'+str(self.i),"ID TABLA")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))

        self.inc();
        dot.node('Node'+  str(self.i), str(id_tablas))
        dot.edge('Node' + str(nuevoPadre2),'Node'+str(self.i))


        self.inc();
        nuevoPadre3 = self.i
        dot.node('Node'+str(self.i),"COLUMNAS")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))
       
        for i in id_columnas:
            self.inc();
            dot.node('Node'+  str(self.i), i.val +' Tipo: '+ i.tipo)
            dot.edge('Node' + str(nuevoPadre3),'Node'+str(self.i))

        