from Instruccion import *
from graphviz import Digraph
from graphviz import escape


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
        dot.attr('node', shape='box', style='cyan4', color='#31CEF0')

        dot.node('Node' + str(self.i), "AST")
        dot.edge_attr.update(arrowhead='none')
        self.recorrerInstrucciones(self.sentencias, 'Node' + str(self.i))
        dot.render('AST', format='png', view=True)
        print('Hecho')

    def recorrerInstrucciones(self, sente, padre):
        for i in sente:
            if isinstance(i, DropTable):
                print("Si es un drop table *" + i.id)
                self.grafoDropTable(i.id, padre)

            elif isinstance(i, Select):
                print("Es Una Instruccion Select")
                self.GrafoSelect(i.Lista_Campos,i.Nombres_Tablas,i.unionn,padre)
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

    def GrafoCampo_Accedido(self, NombreT, Columna, Lista_Alias, padre):
        global dot

        # NombreT.Campo Lista
        if (NombreT != "") and (Columna != "") and (len(Lista_Alias) != 0):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), Lista_Alias)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))

            # Recorrer lista alias

        # NombreT.Campo
        elif (NombreT != "") and (Columna != "") and (len(Lista_Alias) == 0):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


        # Campo Lista
        elif (NombreT == "") and (Columna != "") and (len(Lista_Alias) != 0):
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


        # Campo
        elif (NombreT == "") and (Columna != "") and (len(Lista_Alias) == 0):
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
    def GrafoAccesoTabla(self, NombreT, Lista_Alias, padre):
        global dot

        # Nombre
        if (NombreT != "") and (len(Lista_Alias) == 0):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Nombre_Tabla")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        # Nombre Lista
        elif (NombreT != "") and (len(Lista_Alias) != 0):

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

    # ALIAS CAMPOS
    # ----------------------------------------------------------------------------------------------------------
    def GrafoAlias_Campos_ListaCampos(self, Alias, Lista_Sentencias, padre):
        global dot

        # as Alias , Lista    and    alias, lista
        if (Alias != "") and (len(Lista_Sentencias) != 0):

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


        # as Alias
        elif (Alias != "") and (len(Lista_Sentencias) == 0):

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


        # Lista
        elif (Alias == "") and (len(Lista_Sentencias) != 0):

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

    # ALIAS Tablas
    # ----------------------------------------------------------------------------------------------------------
    def GrafoAlias_Table_ListaTablas(self, Alias, Lista_Sentencias, padre):
        global dot

        # as Alias , Lista    and    alias, lista
        if (Alias != "") and (len(Lista_Sentencias) != 0):

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


        # as Alias
        elif (Alias != "") and (len(Lista_Sentencias) == 0):

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


        # Lista
        elif (Alias == "") and (len(Lista_Sentencias) != 0):

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

    # Recorrido de la lista de Campos
    # ----------------------------------------------------------------------------------------------------------

    def RecorrerListadeCampos(self, Campos, padre):
        for i in Campos:
            if isinstance(i, Campo_Accedido):
                print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.GrafoCampo_Accedido(i.NombreT, i.Columna, i.Lista_Alias, padre)
            else:
                print("No Ningun Tipo")

    # Recorrido de la lista de Nombres de Tablas
    # ----------------------------------------------------------------------------------------------------------

    def RecorrerListadeNombres(self, Nombres, padre):
        for i in Nombres:
            if isinstance(i, AccesoTabla):
                print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.GrafoAccesoTabla(i.NombreT, i.Lista_Alias, padre)
            else:
                print("No Ningun Tipo")

    # Recorrido de los Alias
    # ----------------------------------------------------------------------------------------------------------

    def RecorrerTiposAlias(self, Lista_Alias, padre):
        for i in Lista_Alias:

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









