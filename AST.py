from Instruccion import *
from subprocess import check_call
#IMPORTACIÓN DE GRAPHVIZ
from graphviz import Digraph


class AST:
    def __init__(self, sentencias):
        self.contador = 0
        self.c = ""
        self.sentencias = sentencias

#ENCABEZADO DE TODO EL GRAFO-----------------------------------------
    def crearReporte(self):
        ast = Digraph('AST', filename='c:/source/ast.gv', node_attr={'color': 'white', 'fillcolor': 'white','style': 'filled', 'shape': 'record'})
        ast.attr(rankdir='BT',ordering='in')
        ast.edge_attr.update(arrowhead='none')
        contador = 1
        tag = 'N'
#CIERRO ENCABEZADO DEL GRAFO----------------------------------------

    def recorrerInstrucciones(self, sente, padre):
        for i in sente:
            #VIENE UN DROP TABLE
            if isinstance(i, DropTable):
                print("Si es un drop table *" + i.id)
                self.grafoDropTable(i.id, padre)
            #VIENE UN INSERT 
            elif isinstance(i, Insert_Dato):
                print("Si es un insert  *" + i.id_Tabla)
                self.grafoInsertDato(i.id_Tabla,i.valores, padre)
            else:
                print("No es droptable")


#GRAFO DROP TABLE--------------------------------------------------------
    def grafoDropTable(self, id, padre):
        self.contador = self.contador + 1
        nuevoPadre = self.contador
        self.c += 'Node' + str(self.contador) + '[label="DROP TRABLE"]\n'
        self.c += 'Node' + padre + '->' 'Node' + str(self.contador) + ';\n'

        self.contador = self.contador + 1
        self.c += 'Node' + str(self.contador) + '[label="'+id+'"]\n'
        self.c += 'Node' + str(nuevoPadre) + '->' 'Node' + str(self.contador) + ';\n'
    
#GRAFO INSERT--------------------------------------------------------
    def grafoInsertDato(self, id_tabla,valores_insert, padre):
        self.contador = self.contador + 1
        nuevoPadre = self.contador
        self.c += 'Node' + str(self.contador) + '[label="INSERT"]\n'
        self.c += 'Node' + padre + '->' 'Node' + str(self.contador) + ';\n'

        self.contador = self.contador + 1
        nuevoPadre2 = self.contador
        self.c += 'Node' + str(self.contador) + '[label="'+"ID_TABLA"+'"]\n'
        self.c += 'Node' + str(nuevoPadre) + '->' 'Node' + str(self.contador) + ';\n'

        self.contador = self.contador + 1
        self.c += 'Node' + str(self.contador) + '[label="'+id_tabla+'"]\n'
        self.c += 'Node' + str(nuevoPadre2) + '->' 'Node' + str(self.contador) + ';\n'

        self.contador = self.contador + 1
        nuevoPadre3 = self.contador
        self.c += 'Node' + str(self.contador) + '[label="'+"VALORES"+'"]\n'
        self.c += 'Node' + str(nuevoPadre) + '->' 'Node' + str(self.contador) + ';\n'

        #RECORRER LA LISTA DE LOS VALORES
        for i in valores_insert:
            self.grafoDropTable(i)
            


#GRAFO EXPRESION--------------------------------------------------------
    def grafoExpresion(self, id, padre):
        self.contador = self.contador + 1
        nuevoPadre = self.contador
        self.c += 'Node' + str(self.contador) + '[label="DROP TRABLE"]\n'
        self.c += 'Node' + padre + '->' 'Node' + str(self.contador) + ';\n'

        self.contador = self.contador + 1
        self.c += 'Node' + str(self.contador) + '[label="'+id+'"]\n'
        self.c += 'Node' + str(nuevoPadre) + '->' 'Node' + str(self.contador) + ';\n'