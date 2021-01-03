from Instruccion import *
from expresiones import *
import interprete as Inter
from sentencias import *

class SqlComandos:

    def __init__(self, sentencia):
        self.i = 0
        self.sentencia = sentencia
        self.CadenaSQL = None

    def generarCadenaSQL(self):
        i = self.sentencia

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
            pass

        elif isinstance(i, CreateDataBase):
             self.CadenaSQL = self.cadena_create_database(i)

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
            self.CadenaSQL = self.cadena_drop_database(i)

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
        elif isinstance(i, useClase):
            self.CadenaSQL = "USE " + str(i.id) + ";"

        else:
            return None

    def cadena_create_database(self, createDataBase: CreateDataBase):
        codigo3d = "CREATE "

        if createDataBase.replace == 1:
            codigo3d += "OR REPLACE "
        codigo3d += "DATABASE "
        if createDataBase.exists == 1:
            codigo3d += "IF NOT EXISTS "
        codigo3d += str(createDataBase.idBase)
        if createDataBase.idOwner != 0:
            codigo3d += " OWNER = " + str(createDataBase.idOwner)
        if createDataBase.Modo != 0:
            codigo3d += " MODE = " + str(createDataBase.Modo)
        codigo3d += ";"

        return codigo3d

    def cadena_drop_database(self, dropDataBase: DropDataBase):
        codigo3d = "DROP DATABASE "

        if dropDataBase.existe == 1:
            codigo3d += "IF EXISTS "
        codigo3d += str(dropDataBase.id) + ";"

        return codigo3d


    def cadena_expresion(self, expresiones):
        cadena = ""
        if isinstance(expresiones, ExpresionAritmetica):
            return self.cadena_aritmetica(expresiones)
        elif isinstance(expresiones, ExpresionRelacional):
            return self.cadena_relacional(expresiones)
        elif isinstance(expresiones, ExpresionLogica):
            return self.cadena_logica(expresiones)
        elif isinstance(expresiones, UnitariaNegAritmetica):
            return "- " + str(self.cadena_expresion(expresiones))
        elif isinstance(expresiones, UnitariaLogicaNOT):
            return "NOT " + str(self.cadena_expresion(expresiones))
        elif isinstance(expresiones, UnitariaNotBB):
            return "~ " + str(self.cadena_expresion(expresiones))
        elif isinstance(expresiones, ExpresionValor):
            if isinstance(expresiones.val, string_types):
                return '"' + str(expresiones.val) + '"'
            return expresiones.val

        elif isinstance(expresiones, Variable):
            return expresiones.id
        elif isinstance(expresiones, UnitariaAritmetica):
            return self.getVar(expresiones.operador) + " " + str(self.cadena_expresion(expresiones.exp1))
        elif isinstance(expresiones, ExpresionFuncion):
            return self.cadena_expresion_funcion(expresiones)
        elif isinstance(expresiones, ExpresionTiempo):
            return expresiones.nombre
        elif isinstance(expresiones, ExpresionConstante):
            return expresiones.nombre
        elif isinstance(expresiones, Absoluto):
            try:
                cadena = "(" + self.cadena_expresion(expresiones.variable) + ")"
                return cadena

            except:
                print('Error no se puede aplicar abs() por el tipo de dato')
                # consola.insert('end','>>Error: No se puede aplicar abs() al tipo de dato\n>>')
                # newErr=ErrorRep('Semantico','No se puede aplicar abs() al tipo de dato ',indice)
                # LisErr.agregar(newErr)
                return None
        else:
            print(expresiones)
            print('Error:Expresion no reconocida')
        return None

    def cadena_logica(self, expresion: ExpresionLogica):
        cadena = ""
        exp1 = self.cadena_expresion(expresion.exp1)
        exp2 = self.cadena_expresion(expresion.exp2)

        if exp1 is not None and exp2 is not None:
            cadena = str(exp1) + " " + self.getVar(expresion.operador) + " " + str(exp2)
            return cadena

        if exp1 is not None and exp2 is None:
            cadena = self.getVar(expresion.operador) + " " + str(exp1)
            return cadena

        return None


    def cadena_relacional(self, expresion: ExpresionRelacional):
        cadena = ""

        exp1 = self.cadena_expresion(expresion.exp1)
        exp2 = self.cadena_expresion(expresion.exp2)

        cadena += str(exp1) + " " + self.getVar(expresion.operador) + " " + str(exp2)

        return cadena

    def cadena_aritmetica(self, expresion:ExpresionAritmetica):
        cadena = ""

        exp1 = self.cadena_expresion(expresion.exp1)
        exp2 = self.cadena_expresion(expresion.exp2)

        cadena += str(exp1) + " " + self.getVar(expresion.operador) + " " + str(exp2)

        return cadena



    def cadena_expresion_funcion(self, expresion: ExpresionFuncion, tipo_exp=""):
        cadena = ""

        cadena = self.getVar(expresion.id_funcion) + "("

        parametro1 = ""
        parametro2 = ""
        parametro3 = ""
        parametro4 = ""

        if expresion.exp1 is not None:
            parametro1 = ""
        if expresion.exp2 is not None:
            parametro2 = ""
        if expresion.exp3 is not None:
            parametro3 = ""
        if expresion.exp4 is not None:
            parametro4 = ""

        if expresion.id_funcion == FUNCION_NATIVA.EXTRACT:
            cadena += parametro1 + " FROM TIMESTAMP " + parametro2
        elif expresion.id_funcion == FUNCION_NATIVA.DATE_PART:
            cadena += parametro1 + ", INTERVAL " + parametro2
        else:
            cadena += parametro1

            if parametro2 != "":
                cadena += ", " + parametro2
            if parametro3 != "":
                cadena += ", " + parametro3
            if parametro4 != "":
                cadena += ", " + parametro4

        cadena += ")"
        return cadena


    def getVar(self, padreID):
        if padreID == OPERACION_ARITMETICA.MAS:
            return '+'
        elif padreID == OPERACION_ARITMETICA.MENOS:
            return '-'
        elif padreID == OPERACION_ARITMETICA.MULTI:
            return '*'
        elif padreID == OPERACION_ARITMETICA.DIVIDIDO:
            return '/'
        elif padreID == OPERACION_ARITMETICA.RESIDUO:
            return '%'
        elif padreID == OPERACION_LOGICA.AND:
            return 'AND'
        elif padreID == OPERACION_LOGICA.OR:
            return 'OR'
        elif padreID == OPERACION_RELACIONAL.IGUALQUE:
            return '=='
        elif padreID == OPERACION_RELACIONAL.DISTINTO:
            return '!='
        elif padreID == OPERACION_RELACIONAL.MAYORIGUAL:
            return '>='
        elif padreID == OPERACION_RELACIONAL.MENORIGUAL:
            return '!='
        elif padreID == OPERACION_RELACIONAL.MAYORQUE:
            return '>'
        elif padreID == OPERACION_RELACIONAL.MENORQUE:
            return '<'
        # NUEVAS COSAS
        elif padreID == OPERACION_LOGICA.IS_NOT_NULL:
            return 'IS_NOT_NULL'
        elif padreID == OPERACION_LOGICA.IS_NOT_TRUE:
            return 'IS_NOT_TRUE'
        elif padreID == OPERACION_LOGICA.IS_NOT_FALSE:
            return 'IS_NOT_FALSE'
        elif padreID == OPERACION_LOGICA.IS_NOT_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID == OPERACION_LOGICA.IS_NULL:
            return 'IS_NULL'
        elif padreID == OPERACION_LOGICA.IS_TRUE:
            return 'IS_TRUE'
        elif padreID == OPERACION_LOGICA.IS_FALSE:
            return 'IS_FALSE'
        elif padreID == OPERACION_LOGICA.IS_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID == OPERACION_LOGICA.IS_NOT_DISTINCT:
            return 'IS_NOT_DISTINCT'
        elif padreID == OPERACION_LOGICA.IS_DISTINCT:
            return 'IS_DISTINCT'
        elif padreID == OPERACION_LOGICA.EXISTS:
            return 'EXISTS'
        elif padreID == OPERACION_LOGICA.NOT_EXISTS:
            return 'NOT_EXISTS'
        elif padreID == OPERACION_LOGICA.IN:
            return 'IN'
        elif padreID == OPERACION_LOGICA.NOT_IN:
            return 'NOT_IN'
        elif padreID == FUNCION_NATIVA.ABS:
            return 'ABS'
        elif padreID == FUNCION_NATIVA.CBRT:
            return 'CBRT'
        elif padreID == FUNCION_NATIVA.CEIL:
            return 'CEIL'
        elif padreID == FUNCION_NATIVA.CEILING:
            return 'CEILING'
        elif padreID == FUNCION_NATIVA.DEGREES:
            return 'DEGREES'
        elif padreID == FUNCION_NATIVA.EXP:
            return 'EXP'
        elif padreID == FUNCION_NATIVA.FACTORIAL:
            return 'FACTORIAL'
        elif padreID == FUNCION_NATIVA.FLOOR:
            return 'FLOOR'
        elif padreID == FUNCION_NATIVA.LN:
            return 'LN'
        elif padreID == FUNCION_NATIVA.LOG:
            return 'LOG'
        elif padreID == FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID == FUNCION_NATIVA.RADIANS:
            return 'RADIANS'
        elif padreID == FUNCION_NATIVA.ROUND:
            return 'ROUND'
        elif padreID == FUNCION_NATIVA.SIGN:
            return 'SIGN'
        elif padreID == FUNCION_NATIVA.SQRT:
            return 'SQRT'
        elif padreID == FUNCION_NATIVA.TRUNC:
            return 'TRUNC'
        elif padreID == FUNCION_NATIVA.ACOS:
            return 'ACOS'
        elif padreID == FUNCION_NATIVA.ACOSD:
            return 'ACOSD'
        elif padreID == FUNCION_NATIVA.ASIN:
            return 'ASIN'
        elif padreID == FUNCION_NATIVA.ASIND:
            return 'ASIND'
        elif padreID == FUNCION_NATIVA.ATAN:
            return 'ATAN'
        elif padreID == FUNCION_NATIVA.ATAND:
            return 'ATAND'
        elif padreID == FUNCION_NATIVA.COS:
            return 'COS'
        elif padreID == FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID == FUNCION_NATIVA.COT:
            return 'COT'
        elif padreID == FUNCION_NATIVA.COTD:
            return 'COTD'
        elif padreID == FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID == FUNCION_NATIVA.SIN:
            return 'SIN'
        elif padreID == FUNCION_NATIVA.SIND:
            return 'SIND'
        elif padreID == FUNCION_NATIVA.TAN:
            return 'TAN'
        elif padreID == FUNCION_NATIVA.TAND:
            return 'TAND'
        elif padreID == FUNCION_NATIVA.SINH:
            return 'SINH'
        elif padreID == FUNCION_NATIVA.COSH:
            return 'COSH'
        elif padreID == FUNCION_NATIVA.TANH:
            return 'TANH'
        elif padreID == FUNCION_NATIVA.ASINH:
            return 'ASINH'
        elif padreID == FUNCION_NATIVA.ACOSH:
            return 'ACOSH'
        elif padreID == FUNCION_NATIVA.ATANH:
            return 'ATANH'
        elif padreID == FUNCION_NATIVA.LENGTH:
            return 'LENGTH'
        elif padreID == FUNCION_NATIVA.TRIM:
            return 'TRIM'
        elif padreID == FUNCION_NATIVA.MD5:
            return 'MD5'
        elif padreID == FUNCION_NATIVA.SHA256:
            return 'SHA256'
        elif padreID == FUNCION_NATIVA.DIV:
            return 'DIV'
        elif padreID == FUNCION_NATIVA.GCD:
            return 'GCD'
        elif padreID == FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID == FUNCION_NATIVA.POWER:
            return 'POWER'
        elif padreID == FUNCION_NATIVA.ATAN2:
            return 'ATAN2'
        elif padreID == FUNCION_NATIVA.ATAN2D:
            return 'ATAN2D'
        elif padreID == FUNCION_NATIVA.GET_BYTE:
            return 'GET_BYTE'
        elif padreID == FUNCION_NATIVA.ENCODE:
            return 'ENCODE'
        elif padreID == FUNCION_NATIVA.DECODE:
            return 'DECODE'
        elif padreID == CONDICIONAL_SUBQUERY.ANY:
            return 'ANY'
        elif padreID == CONDICIONAL_SUBQUERY.ALL:
            return 'ALL'
        elif padreID == CONDICIONAL_SUBQUERY.SOME:
            return 'SOME'
        elif padreID == FUNCION_NATIVA.SUBSTRING:
            return 'SUBSTRING'
        elif padreID == FUNCION_NATIVA.SUBSTR:
            return 'SUBSTR'
        elif padreID == FUNCION_NATIVA.SET_BYTE:
            return 'SET_BYTE'
        elif padreID == FUNCION_NATIVA.WIDTH_BUCKET:
            return 'WIDTH_BUCKET'
        elif padreID == OPERACION_ARITMETICA.CUBICA:
            return '||'
        elif padreID == OPERACION_ARITMETICA.CUADRATICA:
            return '|'
        elif padreID == OPERACION_ARITMETICA.POTENCIA:
            return '^'
        elif padreID == FUNCION_NATIVA.EXTRACT:
            return 'EXTRACT'
        elif padreID == FUNCION_NATIVA.DATE_PART:
            return 'DATE_PART'
        elif padreID == FUNCION_NATIVA.NOW:
            return 'NOW'
        elif padreID == FUNCION_NATIVA.PI:
            return 'PI'
        elif padreID == FUNCION_NATIVA.RANDOM:
            return 'RANDOM'
        else:
            return 'op'