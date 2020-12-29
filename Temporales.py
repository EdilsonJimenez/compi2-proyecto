class Temporales:
    def __init__(self, variables={}, temp= 0, etiqueta = 0):
        self.variables = variables
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

