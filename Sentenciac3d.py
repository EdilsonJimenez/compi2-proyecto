from Instruccion_pl import *
from Temporales import *

class Codigo3d:

    def __init__(self, instrucciones):
        self.i = 0
        self.instrucciones = instrucciones

    def Traducir(self):
        global ts_global
        for i in self.instrucciones:
            if isinstance(i, If_inst):
                self.transIf(i)
            else:
                print("NO TRADUCE....")

    def transIf(self, instancia):
        global T
        cadena = ""
        condicion = ""
        #procesamos la "condicion" del IF ----> self.transExpresion(instancia.expresion)
        cadena += "if" + str(condicion) + ": \n"
        cadena += "else : \n"
        cadena += "label . "+ T.varTemporal() +"\n"
        # Si el if trae instruciones en IF
        if instancia.instIf != 0:
            print("Trae Instrucciones If")
            self.recorrerSentencias(instancia.instIf)
        # Si el if trae instruciones en ELSE
        if instancia.instElse != None:
            if instancia.instElse != 0:
                print("Trae Instrucciones Else")
                self.recorrerSentencias(instancia.instElse)

