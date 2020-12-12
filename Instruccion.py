class Instruccion:
    'Es una clase abstracta'

# Un drop table esta compuesto por el ID de la tabla que eliminara.
class DropTable(Instruccion):
    def __init__(self, id):
        self.id = id




#---------------------------------------------------------------------------------------------------
class Select(Instruccion) :
    def __init__(self,  unionn, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn





# Campos Accedidos
#---------------------------------------------------------------------------------------------------

class Campo_Accedido(Instruccion): #Nombre.columna  Lista_Posible

    def __init__(self, NombreT, Columna, Lista_Alias=[]):
        self.NombreT       = NombreT
        self.Columna       = Columna
        self.Lista_Alias   = Lista_Alias

#---------------------------------------------------------------------------------------------------


#Nombre Tabla Accedidos
#---------------------------------------------------------------------------------------------------
class AccesoTabla(Instruccion): #Tabla

    def __init__(self, NombreT,Lista_Alias=[]):
        self.NombreT     = NombreT
        self.Lista_Alias = Lista_Alias
#---------------------------------------------------------------------------------------------------






# Alias
#Alias Campos
#---------------------------------------------------------------------------------------------------
class Alias_Campos_ListaCampos(Instruccion):
    def __init__(self, Alias,Lista_Sentencias=[]):
        self.Alias = Alias
        self.Lista_Sentencias = Lista_Sentencias

#---------------------------------------------------------------------------------------------------


#Alias Tablas
#---------------------------------------------------------------------------------------------------
class Alias_Table_ListaTablas(Instruccion):
    def __init__(self, Alias,Lista_Sentencias=[]):
        self.Alias = Alias
        self.Lista_Sentencias = Lista_Sentencias

#---------------------------------------------------------------------------------------------------
