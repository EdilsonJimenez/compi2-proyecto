from Instruccion import *
from subprocess import check_call

class AST:
    def __init__(self, sentencias):
        self.contador = 0
        self.c = ""
        self.sentencias = sentencias

    def crearReporte(self):
        f = open('Grafo.dot', 'w')
        self.c = 'digraph G{\n'
        self.c += 'rankdir = TB; \n'
        self.c += 'Node'+ str(self.contador) + '[label="AST"]\n'
        self.recorrerInstrucciones(self.sentencias, str(self.contador))
        self.c += '}\n'
        f.write(self.c)
        print("Graficando.....")
        f.close()
        check_call(['dot', '-Tpng', 'Grafo.dot', '-o', 'Grafo.png'])

    def recorrerInstrucciones(self, sente, padre):
        for i in sente:
            if isinstance(i, DropTable):
                print("Si es un drop table *" + i.id)
                self.grafoDropTable(i.id, padre)
            else:
                print("No es droptable")

    def grafoDropTable(self, id, padre):
        self.contador = self.contador + 1
        nuevoPadre = self.contador
        self.c += 'Node' + str(self.contador) + '[label="DROP TRABLE"]\n'
        self.c += 'Node' + padre + '->' 'Node' + str(self.contador) + ';\n'

        self.contador = self.contador + 1
        self.c += 'Node' + str(self.contador) + '[label="'+id+'"]\n'
        self.c += 'Node' + str(nuevoPadre) + '->' 'Node' + str(self.contador) + ';\n'
