from random import *

class Temporales:
    def __init__(self, tablaSimbolos={}, variables={}, funciones={}, temp= 0, etiqueta = 0):
        self.variables = variables.copy()
        self.funciones = funciones.copy()
        self.tablaSimbolos = tablaSimbolos.copy()
        self.temp = temp
        self.etiqueta = etiqueta

    def varTemporal(self):
        variable = "t" + str(self.temp)
        self.temp += 1
        return str(variable)

    def etiquetaT(self):
        variable = "L" + str(self.etiqueta)
        self.etiqueta += 1
        return variable

    def agregarVar(self, varT, variableObjeto):
        self.variables[varT] = variableObjeto

    def agregarSimbolo(self, simbolo):
        rand = randint(1, 25000)
        self.variables[str(simbolo.nombre)+str(rand)] = simbolo

    def obtenerSimbolo(self, simbolo):
        if not simbolo in self.tablaSimbolos:
            pass
            return None
        else:
            return self.tablaSimbolos[simbolo]

    def actualizarSimbolo(self, simbolo, nuevoSi):
        if not simbolo in self.tablaSimbolos:
            print("Si se actualizo.")
            pass
        else:
            self.tablaSimbolos[simbolo] = nuevoSi

class tipoSimbolo():
    def __init__(self, nombre, tipo, tam, pos, rol, ambito):
        self.nombre = nombre
        self.tipo = tipo
        self.tam = tam
        self.pos = pos
        self.rol = rol
        self.ambito = ambito