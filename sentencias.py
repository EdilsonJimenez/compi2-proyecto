class Sentencia():
    'Abstracta'

    def Ejecutar(self):
        pass


class CaseSimple(Sentencia):

    def __init__(self, busqueda, listawhen, caseelse):
        self.busqueda = busqueda
        self.listawhen = listawhen
        self.caseelse = caseelse


class CSWhen():

    def __init__(self, expresiones, sentencias):
        self.expresiones = expresiones
        self.sentencias = sentencias

class CElse():

    def __init__(self, sentencias):
        self.sentencias = sentencias


class CaseBuscado(Sentencia):

    def __init__(self, listawhen, caseelse):
        self.listawhen = listawhen
        self.caseelse = caseelse

class CBWhen():

    def __init__(self, expresion, sentencias):
        self.expresion = expresion
        self.sentencias = sentencias


class LoopSimple(Sentencia):

    def __init__(self, label, sentencias, labelfinal):
        self.label = label
        self.sentencias = sentencias
        self.labelfinal = labelfinal

class Exit(Sentencia):

    def __init__(self, label, when):
        self.label = label
        self.when = when

class Continue(Sentencia):

    def __init__(self, label, when):
        self.label = label
        self.when = when


class WhenAuxilar():

    def __init__(self, expresion):
        self.expresion = expresion


