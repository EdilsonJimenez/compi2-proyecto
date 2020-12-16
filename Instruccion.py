import ts as TS
import jsonMode as Master
from errores import *
LisErr = TablaError([])
ts_global = TS.TablaDeSimbolos()
Lista = []
Ejecucion = ">"

Lista.append(Ejecucion)

class Instruccion():
    'Abstracta'

    def Ejecutar(self):
        pass

# Un drop table esta compuesto por el ID de la tabla que eliminara.
class DropTable(Instruccion):
    def __init__(self, id):
        self.id = id


class Absoluto(Instruccion) :
    def __init__(self, variable) :
        self.variable=variable

#---------------------------------------------------------------------------------------------------
class Select(Instruccion) :
    def __init__(self,  unionn, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn

    def Ejecutar(self):
        print("Ejecutando  Select ")

        #Recorremos lista de Campos

        #Recorremos lista de nombres de tablas

        #Bamos a ir buscando de las tablas cada uno de los campos a la vez iterando cada tabla con los campos

        #Si viene tabla.nombre  bamos a buscar en especifico cada una de la cuestiones





#---------------------------------------------------------------------------------------------------
class Select2(Instruccion) :
    def __init__(self,  unionn,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn
        self.Cuerpo = Cuerpo

#Con Distinct
#---------------------------------------------------------------------------------------------------
class Select3(Instruccion) :
    def __init__(self, distinct, unionn, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.distinct=distinct
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn
#---------------------------------------------------------------------------------------------------
class Select4(Instruccion) :
    def __init__(self,distinct,  unionn,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.distinct = distinct
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn
        self.Cuerpo = Cuerpo


#subSelect sin cuerpo
#---------------------------------------------------------------------------------------------------

class SubSelect(Instruccion) :
    def __init__(self, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas

#subSelect con cuerpo
#---------------------------------------------------------------------------------------------------
class SubSelect2(Instruccion) :
    def __init__(self,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.Cuerpo = Cuerpo

#subSelect sin cuerpo con distict
#---------------------------------------------------------------------------------------------------

class SubSelect3(Instruccion) :
    def __init__(self,Distict, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Distict       = Distict
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas

#subSelect con cuerpo con distict
#---------------------------------------------------------------------------------------------------
class SubSelect4(Instruccion) :
    def __init__(self,Distict,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Distict       = Distict
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.Cuerpo = Cuerpo



# Campos Accedidos
#---------------------------------------------------------------------------------------------------

#Campos Accedidos por Lista
class Campo_Accedido(Instruccion): #Nombre.columna  Lista_Posible

    def __init__(self, NombreT, Columna, Lista_Alias=[]):
        self.NombreT       = NombreT
        self.Columna       = Columna
        self.Lista_Alias   = Lista_Alias

    def Ejecutar(self):
        print("")


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



# Campos Limit
#---------------------------------------------------------------------------------------------------

class AccesoLimit(Instruccion):

    def __init__(self,Reservada,Expresion_Numerica):
        self.Reservada = Reservada
        self.Expresion_Numerica  =  Expresion_Numerica


#Campos Accedidos desde Las Subconsultas
#---------------------------------------------------------------------------------------------------

class AccesoSubConsultas(Instruccion):

    def __init__(self, AnteQuery=[],Query=[],Lista_Alias=[]):
        self.AnteQuery      = AnteQuery
        self.Query          = Query
        self.Lista_Alias  = Lista_Alias


#---------------------------------------------------------------------------------------------------

#Campos de los unions
#---------------------------------------------------------------------------------------------------

class CamposUnions(Instruccion):
    def __init__(self,Reservada,Comportamiento,Consulta=[]):
        self.Reservada      = Reservada
        self.Comportamiento = Comportamiento
        self.Consulta       = Consulta




# Alias
#---------------------------------------------------------------------------------------------------
#Alias Campos
#---------------------------------------------------------------------------------------------------

#Alias Campos sin lista
class Alias_Campos_ListaCamposSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias
#Alias Tablas
#---------------------------------------------------------------------------------------------------
#Alias campos Sin Lista
class Alias_Table_ListaTablasSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias
#Alias Group By
#---------------------------------------------------------------------------------------------------
#Alias campos Sin Lista
class Alias_Tablas_GroupSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias

#Alias SUB QUERYS
#---------------------------------------------------------------------------------------------------
class Alias_SubQuerysSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias

# FIN ALIAS
#---------------------------------------------------------------------------------------------------





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
#TIPOS DE GROUP BY
#---------------------------------------------------------------------------------------------------
#Group By  Con Having y condiciones
class GroupBy(Instruccion):
    def __init__(self,Lista_Campos=[],Condiciones=[]):
        self.Lista_Campos = Lista_Campos
        self.Condiciones  = Condiciones


#TIPOS DE CASES
#---------------------------------------------------------------------------------------------------
class CaseCuerpo(Instruccion):
    def __init__(self,Cuerpo,Lista_When=[]):
        self.Lista_When = Lista_When
        self.Cuerpo     = Cuerpo
class ExpresionesCase(Instruccion):
    def __init__(self,Reservada,ListaExpresiones=[]):
        self.Reservada            = Reservada
        self.ListaExpresiones     = ListaExpresiones

class TiposWhen(Instruccion):
    def __init__(self,Reservada,Reservada2,Reservada3,ListaExpresiones1=[],ListaExpresiones2=[],ListaExpresiones3=[]):
        self.Reservada    = Reservada
        self.Reservada2   = Reservada2
        self.Reservada3   = Reservada3
        self.ListaExpresiones1 = ListaExpresiones1
        self.ListaExpresiones2 = ListaExpresiones2
        self.ListaExpresiones3 = ListaExpresiones3





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


    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion

        if self.replace == "":
            r = ts_global.obtenerBasesDatos(self.idBase)
            if r is None:
                rM = Master.createDatabase(str(self.idBase))
                Ejecucion += " CREATE DB:  Base de datos creada con exito!"+"\n"
                Lista.clear();
                Lista.append(Ejecucion)
                if rM == 0:
                    ts_global.agregarBasesDatos(self)
                    print(" > Base de datos creada con exito!")
                elif rM == 1 or rM == 2:
                    print("> Base de datos ya existe.")
                    er = ErrorRep('Semantico', 'La Base de datos ya existe', 0)
                    LisErr.agregar(er)
            else:
                print("Si encontre la BD. ")
                Ejecucion +="CREATE DB:  La Base de Datos No se Creo ya que existe! "
                Lista.clear();
                Lista.append(Ejecucion)
                er = ErrorRep('Semantico', 'La Base de datos ya existe', 0)
                LisErr.agregar(er)
        else:
            r = ts_global.obtenerBasesDatos(self.idBase)
            if r is None:

                rM = Master.createDatabase(str(self.idBase))
                Ejecucion += "CREATE DB:    Base de datos creada con exito!"+"\n"
                Lista.clear();
                Lista.append(Ejecucion)

                if rM == 0:
                    ts_global.agregarBasesDatos(self)
                    print(" > Base de datos creada con exito!")
                elif rM == 1 or rM == 2:
                    print("> Base de datos ya existe Se va a Reemplazar ")
            else:
                Ejecucion += "CREATE DB:  Se encontro la BD Bamos a Reemplazar!"+"\n"
                Lista.clear();
                Lista.append(Ejecucion)
                print("Si encontre la BD. Bamos a Reemplazar la Misma! ")



class ShowDatabases(Instruccion):
    def __init__(self, cadenaLike):
        self.cadenaLike = cadenaLike

    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion
        #idDB = self.cadenaLike.replace("\"","")

        r  = Master.showDatabases()
        if r  is not None:  #si lo encuentra
            for element in r:
                print(str(element))
                Ejecucion +="SHOW DB:>"+ str(element) +"\n"
                Lista.clear();
                Lista.append(Ejecucion)
        else:
            print("No encontre la BD.")
            Ejecucion += "SHOW DB: No se encontro la BD" + "\n"
            Lista.clear();
            Lista.append(Ejecucion)

            er = ErrorRep('Semantico', 'No Encontre la Base de Datos', 0)
            LisErr.agregar(er)





class AlterDataBase(Instruccion):
    def __init__(self, idDB, opcion):
        self.idDB = idDB
        self.opcion = opcion

    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion


        c1 = False
        c2 = False
        error=""

        opcion  = self.opcion.replace("\"", "")
        opcionf = self.opcion.replace("\'", "")

        r =  ts_global.obtenerBasesDatos(self.idDB)
        r2 = ts_global.obtenerBasesDatos(opcionf)

        if r is not None:  #si lo encuentra
            c1 = True
        else:
            error += "No se Encontro la Base De datos "
        if r2 is  None:  #No Esta el Nombre para definirlo en la bd
            c2 = True
        else:
            error += "  Se encontro el Valor a Setear"

        if (c1 and c2):
            print("Excelente se puede editar")
            #Editamos nuestro diccionario
            ts_global.actualizarCreateDataBase(str(self.idDB),str(self.opcion))
            Ejecucion += "ALTER DB: Edicion base de Datos Exitosa!" + "\n"
            Lista.clear();
            Lista.append(Ejecucion)
            #Editamos en base de datos fisica
            rM = Master.alterDatabase(str(self.idDB),str(self.opcion))
            if rM==2:
                print("No se encuentra la BD")
            elif rM==3:
                print("Ya se encuentra la BD con el nombre a tratar")
            elif rM==1:
                print("Verificar Ocurrio Error Al editar")
            elif rM==0:
                print("Se Edito la Base de Datos con exito")
            else:
                print( "No llega nunca pero por si las moscas ")
        else:
            print("No encontre la BD.")
            Ejecucion += "ALTER DB:  No se encontro la base de datos! :( " + "\n"
            Lista.clear();
            Lista.append(Ejecucion)
            er = ErrorRep('Semantico', error, 0)
            LisErr.agregar(er)





class DropDataBase(Instruccion):
    def __init__(self, id, existe):
        self.id = id
        self.existe = existe

    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion

        r = ts_global.obtenerBasesDatos(self.id)

        if r == None:  #si lo encuentra
            Ejecucion += "DROP DB:  No se encontro la base de datos! :( " + "\n"
            Lista.clear();
            Lista.append(Ejecucion)

            er = ErrorRep('Semantico', 'No Encontre la Base de Datos', 0)
            LisErr.agregar(er)
        else:
            ts_global.EliminarBD(str(self.id))
            Ejecucion += "DROP DB:  Se elimino correctamente la base de Datos! :) " + "\n"
            Lista.clear();
            Lista.append(Ejecucion)

            rM = Master.dropDatabase(str(self.id))
            if rM==0:
                print("Exito")
            elif rM==1:
                print("Fracaso al escribir en bd")
            elif rM==2:
                print("No existe el elemento en la BD")
            else:
                print("No llega nunca pero por si las moscas")









class SelectExtract(Instruccion):
    def __init__(self, tipoTiempo, cadenaFecha):
        self.tipoTiempo = tipoTiempo
        self.cadenaFecha = cadenaFecha

class SelectDatePart(Instruccion):
    def __init__(self, cadena, cadenaIntervalo):
        self.cadena = cadena
        self.cadenaIntervalo = cadenaIntervalo

class SelectTipoCurrent(Instruccion):
    def __init__(self, tipoCurrent):
        self.tipoCurrent = tipoCurrent

class SelectStamp(Instruccion):
    def __init__(self, cadena):
        self.cadena = cadena

class Selectnow(Instruccion):
    def __init__(self, constru):
        self.constru = constru

class CreacionEnum(Instruccion):
    def __init__(self, listaCadenas):
        self.listaCadenas = listaCadenas

#Prueba clase errores
class ErrorSintactico():
    def __init__(self, valor, error, linea):
        self.valor = valor
        self.error = error
        self.linea = linea

    def imprimirError(self):
        return " Error " + str(self.error) + ", no se esperaba el token: " + str(self.valor) + ", Linea: " + str(self.linea)

#---------------------------------------------------------------------------------------------------
class Update_Datos(Instruccion):
    def __init__(self, id_table, valores_set, valor_where):
        self.id_table = id_table
        self.valores_set = valores_set
        self.valor_where = valor_where


#Clase para el Alter Table----------------------------
class Alter_Table_AddColumn(Instruccion):
    def __init__(self, id_table, id_columnas):
        self.id_table = id_table
        self.id_columnas = id_columnas


class Alter_COLUMN(Instruccion):
    def __init__(self, id_columna,id_tipo):
        self.id_columna = id_columna
        self.id_tipo = id_tipo


class Alter_Table_Drop_Column(Instruccion):
    def __init__(self, id_table, columnas):
        self.id_table = id_table
        self.columnas = columnas


class Alter_Table_Rename_Column(Instruccion):
    def __init__(self, id_table, old_column, new_column):
        self.id_table = id_table
        self.old_column = old_column
        self.new_column = new_column

class Alter_Table_Drop_Constraint(Instruccion):
    def __init__(self, id_table, id_constraint):
        self.id_tabla = id_table
        self.id_constraint = id_constraint

class Alter_table_Alter_Column_Set(Instruccion):
    def __init__(self, id_table, id_column):
        self.id_tabla = id_table
        self.id_column = id_column

class Alter_table_Add_Foreign_Key(Instruccion):
    def __init__(self, id_table, id_column, id_column_references):
        self.id_table = id_table
        self.id_column = id_column
        self.id_column_references = id_column_references

class Alter_Table_Add_Constraint(Instruccion):
    def __init__(self, id_table, id_constraint, id_column):
        self.id_table = id_table
        self.id_constraint = id_constraint
        self.id_column = id_column
