from Instruccion import  *
from graphviz import Digraph
from graphviz import escape

from Instruccion import *
from expresiones import *
class Ast2:

    def __init__(self, sentencias):
        self.i=0
        self.sentencias = sentencias

    def inc(self):
        global i
        self.i +=1

#-----------------------------------------
#CREACION DEL REPORTE LA BASE
    def crearReporte(self):
        global dot

        dot = Digraph('AST', format='png',filename='c:/source/ast.gv')
        dot.attr('node', shape='box',style='cyan4',color='#31CEF0')


        dot.node('Node'+ str(self.i), '[label="AST"]')
        dot.edge_attr.update(arrowhead='none')
        self.recorrerInstrucciones(self.sentencias, 'Node'+str(self.i))
        dot.render('AST', format='png', view=True)
        print('Hecho')
#-----------------------------------------
#-----------------------------------------

    def recorrerInstrucciones(self, sente, padre):

        for i in sente:
            #VIENE UN DROP TABLE
            if isinstance(i, DropTable):
                print("Si es un drop table *" + i.id)
                self.grafoDropTable(i.id, padre)
            #VIENE UN INSERT
            if isinstance(i, Insert_Datos):
                print("Si es un drop Insert *")
                self.grafoInsert_Data(i.id_table,i.valores, padre)
            #-----------------------------------
            if isinstance(i, Campo_Accedido):
                print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.grafoCampoAccedido(i.NombreT, i.Columna)
            else:
                print("No es droptable")

#----------------------------------------------------------------------------------------------------------
    def grafoDropTable(self, id, padre):
        global  dot,tag,i

        self.inc();
        nuevoPadre = self.i

        dot.node('Node'+str(self.i),"DROP TRABLE")
        dot.edge(padre,'Node'+str(self.i))

        self.inc();
        dot.node('Node'+  str(self.i), id)
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))
#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR INSERTAR-------------------------------------------------------------------
    def grafoInsert_Data(self, id, valores, padre):
        global  dot,tag,i

        self.inc();
        nuevoPadre = self.i

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
        print("valio")
        
        for i in valores:
            print("valores")
            print(i.val)
            #self.inc();
            #dot.node('Node'+  str(self.i), str(i.val))
            #dot.edge('Node' + str(nuevoPadre3),'Node'+str(self.i))
            #LLAMAMOS A GRAFICAR EXPRESION

       

#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR EXPRESION-----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

   # def GrafoAccesoTabla(self,NombreT,Columna,padre):

   #    self.contador+1
   #    rootActual = self.contador
   #    self.c +='Node'+str(self.contador)+ '[label="Campo"]\n'
   #     self.c +='Node'+ padre + '->'+'Node'+str(self.contador)+';\n'
   #  self.contador+1
   # self.c +='Node'+str(self.contador)+'[label="'+NombreT+]






