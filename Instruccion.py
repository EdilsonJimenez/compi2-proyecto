class Instruccion:
    'Es una clase abstracta'

# Un drop table esta compuesto por el ID de la tabla que eliminara.
class DropTable(Instruccion):
    def __init__(self, id):
        self.id = id

#---------------------------------------------------------------------------------------------------
class Select(Instruccion) :

    def __init__(self,  Lista_Campos=[],Nombres_Tablas=[],Cuepo=[],Unions=[]) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.Cuepo          =  Cuepo
        self.Unions         = Unions

# Campos Accedidos
#---------------------------------------------------------------------------------------------------

class Campo_Accedido(Instruccion): #Nombre.columna

    def __init__(self, NombreT, Columna):
        self.NombreT = NombreT
        self.Columna = Columna


#---------------------------------------------------------------------------------------------------

class Campo_AccedidoSolo(Instruccion):  # Nombre
    def __init__(self,NombreT):
        self.NombreT = NombreT


# Alias
#---------------------------------------------------------------------------------------------------
class Alias_Table(Instruccion):

    def __init__(self, As, Alias):
        self.As = As
        self.Alias = Alias

#---------------------------------------------------------------------------------------------------
class Alias_TableSinAs(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias


#---------------------------------------------------------------------------------------------------
#INSERTAR DATOS CESAR
class Insert_Datos(Instruccion):
    def __init__(self, id_table,valores):
        self.id_table = id_table
        self.valores = valores
# ***************************** CREATE TABLE Y INHERITS ****************************************
class Inherits(Instruccion):
    def __init__(self, id):
        self.id = id

class CreateTable(Instruccion):
    def __init__(self, id, cuerpo, inhe):
        self.id = id
        self.cuerpo = cuerpo
        self.inhe = inhe

