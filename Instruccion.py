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


#Campos Accedidos por Lista
class Campo_Accedido(Instruccion): #Nombre.columna  Lista_Posible

    def __init__(self, NombreT, Columna, Lista_Alias=[]):
        self.NombreT       = NombreT
        self.Columna       = Columna
        self.Lista_Alias   = Lista_Alias


#Campos Accedidos por Lista
class Campo_AccedidoSinLista(Instruccion): #Nombre.columna  Lista_Posible

    def __init__(self, NombreT, Columna):
        self.NombreT       = NombreT
        self.Columna       = Columna


#---------------------------------------------------------------------------------------------------


#Nombre Tabla Accedidos
#---------------------------------------------------------------------------------------------------

class AccesoTabla(Instruccion): #Tabla Lista

    def __init__(self, NombreT,Lista_Alias=[]):
        self.NombreT     = NombreT
        self.Lista_Alias = Lista_Alias

#Accediendo sin lista
class AccesoTablaSinLista(Instruccion): #Tabla

    def __init__(self, NombreT):
        self.NombreT     = NombreT

#---------------------------------------------------------------------------------------------------






# Alias
#Alias Campos
#---------------------------------------------------------------------------------------------------
#Alias Campos con lista
class Alias_Campos_ListaCampos(Instruccion):
    def __init__(self, Alias,Lista_Sentencias=[]):
        self.Alias = Alias
        self.Lista_Sentencias = Lista_Sentencias

#Alias Campos sin lista
class Alias_Campos_ListaCamposSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias


#Alias Tablas
#---------------------------------------------------------------------------------------------------

#Alias campos Con Lista
class Alias_Table_ListaTablas(Instruccion):
    def __init__(self, Alias,Lista_Sentencias=[]):
        self.Alias = Alias
        self.Lista_Sentencias = Lista_Sentencias

#Alias campos Sin Lista
class Alias_Table_ListaTablasSinLista(Instruccion):
    def __init__(self, Alias,Lista_Sentencias=[]):
        self.Alias = Alias
        self.Lista_Sentencias = Lista_Sentencias




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

#---------------------------------------------------------------------------------------------------
class Delete_Datos(Instruccion):
    def __init__(self, id_table,valore_where):
        self.id_table = id_table
        self.valore_where = valore_where

#---------------------------------------------------------------------------------------------------
class Update_Datos(Instruccion):
    def __init__(self, id_table,valores_set, valor_where):
        self.id_table = id_table
        self.valores_set = valores_set
        self.valor_where = valor_where