from Instruccion import *
from expresiones import *
import interprete as Inter
from sentencias import *

class SqlComandos:

    def __init__(self, sentencias):
        self.i = 0
        self.sentencias = sentencias

    Sql = ""

    def inc(self):
        global i
        self.i += 1


    def recorrerInstrucciones(self, sente):
        global dot
        for i in sente:
            # VIENE UN DROP TABLE
            if isinstance(i, DropTable):
                print("Si es un drop table *")
                #self.grafoDropTable(i.id)

            elif isinstance(i, Select):
                print("Es Una Instruccion Select")
                #self.GrafoSelect(i.Lista_Campos, i.Nombres_Tablas, i.unionn)

            elif isinstance(i, Select2):
                print("Es Una Instruccion Select2")
                #self.GrafoSelect2(i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn)

            elif isinstance(i, Select3):
                print("Es Una Instruccion Select 3 ")
                #self.GrafoSelect3(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.unionn)

            elif isinstance(i, Select4):
                print("Es Una Instruccion Select 4")
                #self.GrafoSelect4(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn)

            elif isinstance(i, Insert_Datos):
                print("Si es un drop Insert *")
                #self.grafoInsert_Data(i.id_table, i.valores)
            # -----------------------------------
            elif isinstance(i, CreateTable):
                #self.grafoCreateTable(i.id, i.cuerpo, i.inhe)

            elif isinstance(i, CreateDataBase):
                #self.grafoCreateDataBase(i.replace, i.exists, i.idBase, i.idOwner, i.Modo)

            elif isinstance(i, Delete_Datos):
                print("Es Una Instruccion Delete")
                #self.grafoDelete_Data(i.id_table, i.valore_where)

            elif isinstance(i, Update_Datos):
                print("Es Una Instruccion Update")
                #self.grafoUpdate__Data(i.id_table, i.valores_set, i.valor_where)

            elif isinstance(i, Alter_COLUMN):
                print("Es Una Instruccion Alter  Column")
                #self.grafoAlter_Column(i.idtabla, i.columnas)

            elif isinstance(i, Alter_Table_AddColumn):
                print("Es Una Instruccion Alter Add Column")
                #self.grafoAlter_AddColumn(i.id_table, i.id_columnas)

            elif isinstance(i, ShowDatabases):
                print("Es Una Instruccion Showdatabases")
                #self.grafoShowDatabases(i.cadenaLike)

            elif isinstance(i, AlterDataBase):
                print("Es Una Instruccion AlterDataBase")
                #self.grafoAlterDataBase(i.idDB, i.opcion)

            elif isinstance(i, DropDataBase):
                print("Es Una Instruccion DropDataBase")
                #self.grafoDropDataBase(i.id, i.existe)

            elif isinstance(i, SelectExtract):
                print("Es Una Instruccion SelectExtract")
                #self.grafoSelectExtract(i.tipoTiempo, i.cadenaFecha)

            elif isinstance(i, SelectDatePart):
                print("Es Una Instruccion SelectDatePart")
                #self.grafoSelectDatePart(i.cadena, i.cadenaIntervalo)

            elif isinstance(i, SelectTipoCurrent):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoSelectTipoCurrent(i.tipoCurrent)

            elif isinstance(i, SelectStamp):
                print("Es Una Instruccion SelectTIMESTAMP")
                #self.grafoSelectStamp(i.cadena)

            elif isinstance(i, Selectnow):
                print("Es Una Instruccion Select Now")
                #self.grafoSelectnow(i.constru)

            elif isinstance(i, CreacionEnum):
                print("Es Una Instruccion SelectCurrentType")

                #self.grafoCreacionEnum(i.listaCadenas)

            elif isinstance(i, Alter_Table_AddColumn):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoAlter_AddColumn(i.id_table, i.id_columnas)

            elif isinstance(i, Alter_Table_Drop_Column):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoAlter_DropColumn(i.id_table, i.columnas)

            elif isinstance(i, Alter_Table_Rename_Column):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoAlter_RenameColumn(i.id_table, i.old_column, i.new_column)

            elif isinstance(i, Alter_Table_Drop_Constraint):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoAlter_DropConstraint(i.id_tabla, i.id_constraint)

            elif isinstance(i, Alter_table_Alter_Column_Set):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoAlter_AlterColumnSet(i.id_tabla, i.id_column)

            elif isinstance(i, Alter_table_Add_Foreign_Key):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoAlter_AddForeignKey(i.id_table, i.id_column, i.id_column_references)

            elif isinstance(i, Alter_Table_Add_Constraint):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoAlter_AddConstraint(i.id_table, i.id_constraint, i.id_column)

            elif isinstance(i, SelectExpresion):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoSelectExpresion(i.listaCampos)

            elif isinstance(i, Funciones_):
                print("Es Una Instruccion SelectCurrentType")
                #self.grafoFuncion(i.Reservada, i.Nombre, i.Retorno,i.Alias, i.Parametros , i.Instrucciones, i.Declaraciones , i.Codigo)

            elif isinstance(i, CrearIndice):
                print("Es Una Instruccion SelectCurrentType")
                #self.GrafoCrearIndice(i)

            elif isinstance(i,Procedimientos_):
                print("Es Una Instruccion SelectCurrentType")
                #self.GrafoProcedure(i.Reservada, i.Nombre, i.Comand,i.Alias, i.Parametros, i.Instrucciones, i.Declaraciones,i.Codigo)


            elif isinstance(i,EjecucionFuncion):
                print("Es Una Instruccion SelectCurrentType")

                #self.GrafoEjecucion(i.Id, i.Parametros)
            else:
                print("No es droptable")
