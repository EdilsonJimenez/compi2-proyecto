import ts as TS
import jsonMode as Master
from six import string_types
from errores import *
from expresiones import *
LisErr = TablaError([])
ts_global = TS.TablaDeSimbolos()
baseActual = ""


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
class DatoInsert(Instruccion):
    def __init__(self, bd, tabla, columna, valor):
        self.bd = bd
        self.tabla = tabla
        self.columna = columna
        self.valor = valor

class Insert_Datos(Instruccion):
    def __init__(self, id_table, valores):
        self.id_table = id_table
        self.valores = valores

    def Ejecutar(self):
        global ts_global,baseActual
        global LisErr
        r = ts_global.obtenerBasesDatos(baseActual)
        if r is None:
            print(" > No existe la BD para insertar.")
        else:
            print("> Si existe la BD para insertar. " + str(self.id_table[0].val))
            r2 = ts_global.obtenerTabla(self.id_table[0].val)
            if r2 is None:
                print(" > No existe la Tabla para insertar.")
            else:
                print("> Si existe la Tabla para insertar. ")
                # Obtener tabla actual
                rT:CreateTable = ts_global.obtenerTabla(self.id_table[0].val)
                print(">>>>>>>"+str(rT.id))
                temporal:CampoTabla = rT.cuerpo
                cC = 0
                for c in rT.cuerpo:
                    cC += 1

                cV = 0
                for v in self.valores:
                    cV += 1

                if cC == cV:
                    print(" >> Parametros exactos.")
                    index = 0
                    banderaInsert = False
                    for cc in self.valores:

                        if isinstance(temporal[index].tipo, valorTipo):

                            if isinstance(str(cc.val), string_types) and (str(temporal[index].tipo.valor) == 'VARCHAR' or str(temporal[index].tipo.valor) == 'CHARACTER' or str(temporal[index].tipo.valor) == 'CHAR'):
                                print(" >>> Parametros correctos, insertar, Validar la exprecion.")
                                banderaInsert = True
                            else:
                                print(" >>> Parametros incorrectos. ")
                                banderaInsert = False
                        else:
                            print(" Valor: >>>" + str(cc.val))
                            if isinstance(str(cc.val), string_types) and ( str(temporal[index].tipo) == 'TEXT' or str(temporal[index].tipo) == 'INTEGER' or str(temporal[index].tipo) == 'INT' or str(temporal[index].tipo) == 'BIGINT' or str(temporal[index].tipo) == 'DECIMAL' or str(temporal[index].tipo) == 'REAL' or str(temporal[index].tipo) == 'FLOAT' or str(temporal[index].tipo) == 'MONEY'):
                                print(" >>> Parametros correctos, insertar")
                                banderaInsert = True
                            elif str(temporal[index].tipo) == 'BOOLEAN'and (str(cc.val) == "TRUE" or str(cc.val) == "FALSE"):
                                print(" >>> Parametros correctos, insertar")
                                banderaInsert = True
                            elif int(cc.val) > 0 and str(temporal[index].tipo) == 'SMALLINT':
                                print(" >>> Parametros correctos, insertar")
                                banderaInsert = True
                            else:
                                print(" >>> Parametros incorrectos. ")
                                banderaInsert = False

                        index += 1

                    # INSERTANDO DATOS
                    ix = 0
                    if banderaInsert is True:
                        listaTemp = []
                        for ccc in self.valores:
                            d = DatoInsert(baseActual, r2, str(temporal[ix].id), ccc.val)
                            ts_global.agregarDato(d)
                            listaTemp.append(ccc.val)
                            ix += 1

                        sr = Master.insert(baseActual, str(self.id_table[0].val), listaTemp)
                        print(baseActual + str(self.id_table[0].val) + str(len(listaTemp)))
                        if sr is 0:
                            print(" >>>> Insert realizado con exito.")
                        else:
                            print(" No se realizo la insercion." + str(sr))
                else:
                    print(" >> Parametros insuficientes.")

# ***************************** CREATE TABLE Y INHERITS ****************************************
class Inherits(Instruccion):
    def __init__(self, id):
        self.id = id

class CreateTable(Instruccion):
    def __init__(self, id, cuerpo, inhe):
        self.id = id
        self.cuerpo = cuerpo
        self.inhe = inhe

    def Ejecutar(self):
        global ts_global
        global LisErr

        # SI la tabla ya existe en el diccionario.
        r = ts_global.obtenerTabla(self.id)
        if r is None:
            print(" > No existe la tabla. ")
            # se cuenta el numero de columnas
            columnas = 0
            for campos in self.cuerpo:
                columnas += 1
            print("---------------")
            print(baseActual)
            print(columnas)
            rM = Master.createTable(baseActual, self.id, columnas)

            if rM == 0:
                ts_global.agregarTabla(self)
                print(" > Se creo la tabla en la base de datos.")

            elif rM == 1:
                print("> 1")
                er =  ErrorRep('Semantico', 'No se encontro el archivo data.',0)
                LisErr.agregar(er)

            elif rM == 2:
                print("> 2")
                er =  ErrorRep('Semantico', 'No existe la base de datos actual.',0)
                LisErr.agregar(er)

            elif rM == 3:
                print( "> 3")
                er =  ErrorRep('Semantico', 'La tabla ya existe en la base de datos.',0)
                LisErr.agregar(er)
        else:
            print("> La tabla ya esta en la TS. ")
            er = ErrorRep('Semantico', 'La tabla ya existe en la base de datos.', 0)
            LisErr.agregar(er)



# --------------------------------------------------------
class CampoTabla(Instruccion):
    def __init__(self, id, tipo, validaciones):
        self.id = id
        self.tipo = tipo
        self.validaciones = validaciones



#---------------------------------------------------------
class CampoValidacion(Instruccion):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor



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
        global ts_global, baseActual
        global LisErr
        print("Ejecuta create")
        r = ts_global.obtenerBasesDatos(self.idBase)
        if r is None:
            print(" No encontro la BD. ")
            rM = Master.createDatabase(str(self.idBase))
            baseActual = str(self.idBase)

            if rM == 0:
                ts_global.agregarBasesDatos(self)
                print(" > Base de datos creada con exito!")

            elif rM == 1 or rM == 2:
                print("> Base de datos ya existe.")
                er =  ErrorRep('Semantico', 'La Base de datos ya existe',0)
                LisErr.agregar(er)

        else:
            print("Si encontre la BD. ")
            er = ErrorRep('Semantico', 'La Base de datos ya existe', 0)
            LisErr.agregar(er)







class ShowDatabases(Instruccion):
    def __init__(self, cadenaLike):
        self.cadenaLike = cadenaLike

    def Ejecutar(self):
        global ts_global
        global LisErr
        #idDB = self.cadenaLike.replace("\"","")

        r  = Master.showDatabases()

        if r  is not None:  #si lo encuentra

            for element in r:
                print(str(element))
        else:
            print("No encontre la BD.")
            er = ErrorRep('Semantico', 'No Encontre la Base de Datos', 0)
            LisErr.agregar(er)





class AlterDataBase(Instruccion):
    def __init__(self, idDB, opcion):
        self.idDB = idDB
        self.opcion = opcion

    def Ejecutar(self):
        global ts_global
        global LisErr

        c1 = False
        c2 = False
        error=""

        opcion  = self.opcion.replace("\"", "")
        opcionf = self.opcion.replace("\'", "")

        r =  ts_global.obtenerBasesDatos(self.idDB)
        r2 = ts_global.obtenerBasesDatos(opcionf)

        if r is not None:  #si lo encuentra
            print("Se encontro la BD. ")
            c1 = True
        else:
            error += "No se Encontro la Base De datos "
        if r2 is  None:  #No Esta el Nombre para definirlo en la bd
            print("No se encontro la opcion a setear excelente! ")
            c2 = True
        else:
            error += "  Se encontro el Valor a Setear"

        if (c1 and c2):
            print("Excelente se puede editar")
            #Editamos nuestro diccionario
            ts_global.actualizarCreateDataBase(str(self.idDB),str(self.opcion))


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
            er = ErrorRep('Semantico', error, 0)
            LisErr.agregar(er)





class DropDataBase(Instruccion):
    def __init__(self, id, existe):
        self.id = id
        self.existe = existe

    def Ejecutar(self):
        global ts_global
        global LisErr

        r = ts_global.obtenerBasesDatos(self.id)

        if r == None:  #si lo encuentra
            print("No encontre la BD.")
            er = ErrorRep('Semantico', 'No Encontre la Base de Datos', 0)
            LisErr.agregar(er)
        else:

            print("Se encontro la BD. ")

            ts_global.EliminarBD(str(self.id))

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
