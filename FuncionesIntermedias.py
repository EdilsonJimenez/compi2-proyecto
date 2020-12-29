import Gramatica as Gram
import interprete as Inter
from Instruccion import *
heap = []


def ejecutarSQL():


    cadena = heap[-1]

    nueva = str(cadena).upper()
    print(nueva)
    Inter.inicializarEjecucionAscendente(cadena)
    # if len(Lista) > 0:
    #     self.consola.insert('insert', Lista[0])
    # else:
    #     return


