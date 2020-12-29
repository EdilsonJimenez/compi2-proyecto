from six import string_types
from expresiones import *
from Instruccion import *

class If_inst(Instruccion):
    def __init__(self, condicion, instIf, instElse):
        print("Se genero el if")
        self.condicion = condicion
        self.instIf = instIf
        self.instElse = instElse



