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


#---------------------------------------------------------------------------------------------------
class Select2(Instruccion) :
    def __init__(self,  unionn,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn
        self.Cuerpo = Cuerpo



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





#Campos Accedidos desde Group By
#---------------------------------------------------------------------------------------------------

class AccesoGroupBy(Instruccion): #Tabla Lista

    def __init__(self, NombreT,Columna,Estado,Lista_Alias=[]):
        self.NombreT      = NombreT
        self.Columna      = Columna
        self.Lista_Alias  = Lista_Alias
        self.Estado = Estado


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
    def __init__(self, Alias):
        self.Alias = Alias



#Alias Group By
#---------------------------------------------------------------------------------------------------

#Alias campos Con Lista
class Alias_Tablas_Group(Instruccion):
    def __init__(self, Alias,Lista_Sentencias=[]):
        self.Alias = Alias
        self.Lista_Sentencias = Lista_Sentencias

#Alias campos Sin Lista
class Alias_Tablas_GroupSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias





#Cuerpo Consulta
#---------------------------------------------------------------------------------------------------
#where Condiciones

class Cuerpo_Condiciones(Instruccion):

    def __init__(self,Cuerpo=[]):
        self.Cuerpo = Cuerpo



#Cuerpo Tipo Where condiciones
#---------------------------------------------------------------------------------------------------
class Cuerpo_TipoWhere(Instruccion):
    def __init__(self,Cuerpo=[]):
        self.Cuerpo = Cuerpo



#Cuerpo Tipo Group By
#---------------------------------------------------------------------------------------------------
class Cuerpo_TipoGroup(Instruccion):
    def __init__(self,Cuerpo=[]):
        self.Cuerpo = Cuerpo


#TIPOS DE GROUP BY
#---------------------------------------------------------------------------------------------------
#Group By  Con Having y condiciones

class GroupBy():
    def __init__(self,Lista_Campos=[],Condiciones=[]):
        self.Lista_Campos = Lista_Campos
        self.Condiciones  = Condiciones


















#---------------------------------------------------------------------------------------------------
#INSERTAR DATOS CESAR
class Insert_Datos(Instruccion):
    def __init__(self, id_table, valores):
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

# --------------------------------------------------------------------------------------------------
class constraintTabla(Instruccion):
    def __init__(self, valor, id, condiciones, listas_id, referencia, idRef):
        self.valor = valor
        self.id = id
        self.condiciones = condiciones
        self.listas_id = listas_id
        self.referencia = referencia
        self.idRef = idRef

class CreateDataBase(Instruccion):
    def __init__(self, replace, exists, idBase, idOwner, Modo ):
        self.replace = replace
        self.exists = exists
        self.idBase = idBase
        self.idOwner = idOwner
        self.Modo = Modo

class ShowDatabases(Instruccion):
    def __init__(self, cadenaLike):
        self.cadenaLike = cadenaLike
#---------------------------------------------------------------------------------------------------
class Update_Datos(Instruccion):
    def __init__(self, id_table,valores_set, valor_where):
        self.id_table = id_table
        self.valores_set = valores_set
        self.valor_where = valor_where


#Clase para el Alter Table----------------------------
class Alter_Table_AddColumn(Instruccion):
    def __init__(self, id_table,id_columnas):
        self.id_table = id_table
        self.id_columnas = id_columnas
