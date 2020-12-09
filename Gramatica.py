# -----------------------------------------------------------------------------
# SQL OGANIZACION DE LENGUAJES Y COMPILADORES 2
# -----------------------------------------------------------------------------

reservadas = {

    # RESERVADAS DEL LENGUAJE
    'select': 'SELECT',
    'distinct': 'DISTINCT',
    'from': 'FROM',
    'where': 'WHERE',
    'as': 'AS',
    'inner': 'INNER',
    'join': 'JOIN',
    # PALABRAS RESERVADAS DQL
    'using': 'USING',
    'left': 'LEFT',
    'right': 'RIGHT',
    'full': 'FULL',
    'outer': 'OUTER',
    'group': 'GROUP',
    'by': 'BY',
    'asc': 'ASC',
    'desc': 'DESC',
    'nulls': 'NULLS',
    'first': 'FIRST',
    'last': 'LAST',
    'having': 'HAVING',

    'on': 'ON',
    'and': 'AND',
    'or': 'OR',
    'insert': 'INSERT',
    'into': 'INTO',
    'update': 'UPDATE',
    'set': 'SET',
    'delete': 'DELETE',
    'values': 'VALUES',
    'type': 'TYPE',
    'database': 'DATABASE',
    'create': 'CREATE',
    'table': 'TABLE',
    'smallint': 'SMALLINT',
    'integer': 'INTEGER',
    'bigint': 'BIGINT',
    'decimal': 'DECIMAL',
    'real': 'REAL',
    'money': 'MONEY',
    'double': 'DOUBLE',
    'precision': 'PRECISION',
    'character': 'CHARACTER',
    'varying': 'VARYING',
    'varchar': 'VARCHAR',
    'character': 'CHARACTER',
    'char': 'CHAR',
    'text': 'TEXT',
    'boolean': 'BOOLEAN',
    'not': 'NOT',
    'null': 'NULL',
    'constraint': 'CONSTRAINT',
    'default': 'DEFAULT',




    # palabras reservadas DDL dabatabases
    'replace': 'REPLACE',
    'if': 'IF',
    'exists': 'EXISTS',
    'owner': 'OWNER',
    'mode': 'MODE',
    'show': 'SHOW',
    'databases': 'DATABASES',
    'like': 'LIKE',
    'alter': 'ALTER',
    'rename': 'RENAME',
    'to': 'TO',
    'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',
    'drop': 'DROP'
}







tokens = [

             # SIMBOLOS UTILIZADOS EN EL LENGUAJE
             'DIFERENTE',
             'NEGACION',
             'IGUAL',
             'MAYOR',
             'MENOR',
             'MENORIGUAL',
             'MAYORIGUAL',

             'PARIZQ',
             'PARDER',
             'COMA',
             'PUNTO',
             'PUNTOCOMA',
             'ASTERISCO',
             'DIVISION',
             'PORCENTAJE',
             'MAS',
             'MENOS',

             
             # ESTOS SON LAS EXPRESIONES REGULARES
             'ID',
             'ENTERO',
             'FLOTANTE',
             'CADENASIMPLE',
             'CADENADOBLE',
             'FECHA',

             'COMENTARIOMULTI',
             'COMENTARIONORMAL'

         ] + list(reservadas.values())



# TOKENS DE LOS SIMBOLOS UTILIZADOS EN EL LENGUAJE
t_DIFERENTE = r'!='
t_NEGACION  = r'\!'
t_IGUAL     = r'='
t_MAYOR     = r'>'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_COMA = r','
t_PUNTO = r'\.'
t_PUNTOCOMA = r';'
t_ASTERISCO = r'\*'
t_DIVISION = r'/'
t_PORCENTAJE = r'%'
t_MAS = r'\+'
t_MENOS = r'-'




# EXPRESIONES REGULARES DEL LENGUAJE


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  # Check for reserved words
    return t



def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)

    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0

    return t



def t_FLOTANTE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_CADENASIMPLE(t):
    r'\'.*?\''

    t.value = t.value[1:-1]  # remuevo las comillas simples
    return t


def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas dobles
    return t


def t_COMENTARIOMULTI(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_COMENTARIONORMAL(t):
    r'--.*\n'
    t.lexer.lineno += 1


def t_FECHA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')





# CARACTERES IGNORADOS DEL LENGUAJE

t_ignore = "\t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)





# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()



# ASOCIACION DE OPERADORES CON PRESEDENCIA

#precedence = ( ) #NO HAY POR EL MOMENTO PERO SE VERA INVOLUCRADO LOS SIMBOLOS LOGICOS


precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVISION'),
    )

# Definición de la gramática

def p_init(t) :
    'INICIO          : INSTRUCCIONES'

    t[0] = t[1]




def p_instrucciones_lista(t) :
    'INSTRUCCIONES     : INSTRUCCIONES INSTRUCCION'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'INSTRUCCIONES    : INSTRUCCION'

    t[0] = [t[1]]





def p_instruccion(t) :
    '''INSTRUCCION  : DQL_COMANDOS
                    | DDL_COMANDOS
                    '''
    t[0] = t[1]






#===================  DEFINICIONES DE LOS TIPOS DE SELECT

def p_instruccion_dql_comandos(t) :
    'DQL_COMANDOS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO PUNTOCOMA'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])

    print('\n' + str(t[0]) + '\n')



def p_instruccion_dql_comandosS(t) :
    'DQL_COMANDOS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS  PUNTOCOMA'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])

    print('\n' + str(t[0]) + '\n')


def p_instruccion_dql_comandosS1(t) :
    'DQL_COMANDOS       : SELECT  DISTINCTNT  LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO PUNTOCOMA'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])

    print('\n' + str(t[0]) + '\n')

def p_instruccion_dql_comandosS2(t) :
    'DQL_COMANDOS       : SELECT DISTINCTNT LISTA_CAMPOS FROM NOMBRES_TABLAS  PUNTOCOMA'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])

    print('\n' + str(t[0]) + '\n')




#------------------------------------------------------------------------------------------------------------------

#Lista de Campos
def p_ListaCampos_ListaCampos(t):
    'LISTA_CAMPOS       : LISTA_CAMPOS LISTA'

    t[1].append(t[2])
    t[0] = t[1]


def p_ListaCampos_Lista(t):
    'LISTA_CAMPOS    : LISTA'
    t[0] = [t[1]]



def p_Lista_NombreS(t):
    'LISTA          : NOMBRE_T PUNTO CAMPOS S'

    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])

    #print('\n' + str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + '\n')


def p_Lista_Nombre(t):
    'LISTA          : NOMBRE_T PUNTO CAMPOS'

    t[0] = str(t[1]) + str(t[2]) + str(t[3])

   # print('\n' + str(t[1]) + str(t[2]) + str(t[3]) + '\n')


def p_Lista_CampoS(t):
    'LISTA          : CAMPOS S'

    t[0] = str(t[1]) + str(t[2])
    #print('\n' + str(t[1]) + str(t[2]) + '\n')




def p_Lista_Campo(t):
    'LISTA          : CAMPOS'

    t[0] = str(t[1])
    #print('\n' + str(t[1]) + '\n')



def p_Campos_id(t):
    'CAMPOS          : ID'

    t[0] = str(t[1])
    #print('\n' + str(t[1]) + '\n')



def p_Campos_Asterisco(t):
    'CAMPOS          : ASTERISCO'

    t[0] = str(t[1])
    #print('\n' + str(t[1]) + '\n')



def p_NombreT_id(t):
    'NOMBRE_T        : ID'

    t[0] = str(t[1])
    #print('\n' + str(t[1]) + '\n')



def p_Alias_id(t):
    'ALIAS          : ID'

    t[0] = str(t[1])
    #print('\n' + str(t[1]) + '\n')




def p_S_ComaLista(t):
    'S          : COMA LISTA'

    t[0] = str(t[1]) + str(t[2])
    #print('\n' + str(t[1]) + str(t[2]) + '\n')




def p_S_AsAlias(t):
    'S          : AS ALIAS'

    t[0] = str(t[1]) + str(t[2])
   # print('\n' + str(t[1]) + str(t[2]) + '\n')



#------------------------------------------------------------------------------------------------------------------

#Distinct


def p_Disctint_Rw(t):
    'DISTINCTNT          : DISTINCT'
    t[0] = str(t[1])




#------------------------------------------------------------------------------------------------------------------

#Nombres Tablas

def p_NombresTablas_NombresTablas(t):
    'NOMBRES_TABLAS       : NOMBRES_TABLAS TABLA'

    t[1].append(t[2])
    t[0] = t[1]

def p_NombresTablas_Tabla(t):
    'NOMBRES_TABLAS    : TABLA'

    t[0] = [t[1]]


def p_Tabla_NombreT(t):
    'TABLA   : NOMBRE_T'

    t[0] = str(t[1])
   # print('\n' + str(t[1]) + '\n')



def p_Tabla_NombreTS(t):
    'TABLA   : NOMBRE_T S1'

    t[0] = str(t[1]) + str(t[2])

    #print('\n' + str(t[1]) + str(t[2]) + '\n')





def p_Ss_ComaLista(t):
    'S1          : COMA TABLA'

    t[0] = str(t[1]) + str(t[2])

    #print('\n' + str(t[1]) + str(t[2]) + '\n')



def p_Ss_AsAlias(t):
    'S1          : AS ALIAS'

    t[0] = str(t[1]) + str(t[2])
    #print('\n' + str(t[1]) + str(t[2]) + '\n')




#------------------------------------------------------------------------------------------------------------------
#Cuerpo




def p_Cuerpo_Where(t):
    'CUERPO   : WHERE CONDICIONES'

    t[0] = str(t[1]) + str(t[2])
    #print('\n' + str(t[1]) + str(t[2]) + '\n')



def p_Cuerpo_Mores(t):
    'CUERPO   : MORES'

    t[0] = str(t[1])



def p_MORES_ListaCampos(t):
    'MORES       : MORES MOREE'

    t[1].append(t[2])
    t[0] = t[1]



def p_MORES_Lista(t):
    'MORES    : MOREE'
    t[0] = [t[1]]










def p_Mores_Inners(t):
    'MOREE   : INNERS'

    t[0] = str(t[1])



def p_Mores_Groups(t):
    'MOREE   : GROUPS'

    t[0] = str(t[1])






#-----------------------------------------------------------------------------------------------------------------

#Condiciones


def p_Condiciones_Lista(t):
    'CONDICIONES : CONDICIONES CONDICION'

    t[1].append(t[2])
    t[0] = t[1]



def p_Condiciones_Condicion(t):
    'CONDICIONES : CONDICION'

    t[0] = [t[1]]




def p_Condicion_CondicionRel(t):
   'CONDICION : CONDICION_REL SIMBOLO_LOGICO  CONDICION_REL  OTRO_LOGICO'
   t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Condicion_CondicionRel_Sin(t):
    'CONDICION : CONDICION_REL SIMBOLO_LOGICO CONDICION_REL'

    t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Condicion_CondiRel(t):
    'CONDICION : CONDICION_REL'

    t[0] = str(t[1])




def p_CondicionRel_Expresionn(t):
    'CONDICION_REL : EXPRESIONNE OPERADOR EXPRESIONNE'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])




def p_CondicionRel_Negacion(t):
    'CONDICION_REL : SIMBOLO_NEG  EXPRESIONNE'
    t[0] = str(t[1]) + str(t[2])


def p_CondicionRel_Expre(t):
    'CONDICION_REL : EXPRESIONNE'
    t[0] = str(t[1])



def p_OtroLogico_SimboloLogic(t):
    'OTRO_LOGICO : SIMBOLO_LOGICO CONDICIONES'

    t[0] = str(t[1]) + str(t[2])




#------------------------------------------------------------------------------------------------------------------
#Expresiones


def p_Expresion_Nombre(t):
    'EXPRESIONNE : NOMBRE_C PUNTO CAMPOSC'

    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_Expresion_CampoC(t):
    'EXPRESIONNE : CAMPOSC'

    t[0] = str(t[1])



def p_SimboloLogico_Logicos(t):
    ''' SIMBOLO_LOGICO : AND
                      | OR '''

    t[0] = str(t[1])






def p_SimboloNegacion_sim(t):
    'SIMBOLO_NEG  :  NEGACION'

    t[0] = str(t[1])






def p_NombreC_id(t):
    'NOMBRE_C : ID'

    t[0] = str(t[1])




def p_CamposC_id(t):
    '''CAMPOSC     :  ID
                    | ENTERO
                    | FLOTANTE
                    | CADENASIMPLE
                    | CADENADOBLE '''
    t[0] = str(t[1])



def p_SimboloRela_Simbolos(t):
    '''OPERADOR     : IGUAL
                    | DIFERENTE
                    | MAYOR
                    | MENOR
                    | MENORIGUAL
                    | MAYORIGUAL '''

    t[0] = str(t[1])




#-----------------------------------------------------------------------------------------------------------------
#inners

def p_Inners_Lista(t):
    'INNERS : INNERS INNERR'

    t[1].append(t[2])
    t[0] = t[1]



def p_Inners_Inner(t):
    'INNERS : INNERR'

    t[0] = [t[1]]





def p_Inner_InnerJoin(t):
    'INNERR : TIPOS_INNER JOIN TABLA_REF ON CONDICIONES'

    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])



def p_Inner_Join(t):
    'INNERR :  JOIN TABLA_REF ON CONDICIONES'

    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])






def p_Inner_InnerJoinUsing(t):
    'INNERR : TIPOS_INNER JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER'

    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])



def p_Inner_JoinUsing(t):
    'INNERR :  JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER '

    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])


def p_Inner_Where(t):
    'INNERR   : WHERE CONDICIONES'

    t[0] = str(t[1]) + str(t[2])
    #print('\n' + str(t[1]) + str(t[2]) + '\n')


def p_SubColumn_join(t):
    'SUB_COLUMN  :  JOIN EXPRESIONNE'

    t[0] = str(t[1]) + str(t[2])




def p_SubColumn_Expresione(t):
    'SUB_COLUMN  :  EXPRESIONNE'

    t[0] = str(t[1])



def p_TiposInner_InnerOuter(t):
    ''' TIPOS_INNER :  INNER OUTER'''
    t[0] = str(t[1]) + str(t[2])

def p_TiposInner_Inner(t):
    ''' TIPOS_INNER :  INNER'''
    t[0] = str(t[1])


def p_TiposInner_LefOuter(t):
    ''' TIPOS_INNER :  LEFT OUTER'''
    t[0] = str(t[1]) + str(t[2])

def p_TiposInner_Left(t):
    ''' TIPOS_INNER :  LEFT'''
    t[0] = str(t[1])


def p_TiposInner_RightOuter(t):
    ''' TIPOS_INNER :  RIGHT OUTER'''
    t[0] = str(t[1]) + str(t[2])

def p_TiposInner_Right(t):
    ''' TIPOS_INNER :  RIGHT'''
    t[0] = str(t[1])


def p_TiposInner_FullOuter(t):
    ''' TIPOS_INNER :  FULL OUTER'''
    t[0] = str(t[1]) + str(t[2])


def p_TiposInner_Full(t):
    ''' TIPOS_INNER :  FULL'''
    t[0] = str(t[1])






def p_TablaRef_Id(t):
    'TABLA_REF : ID'

    t[0] = t[1]

def p_TablaRef_IdAS(t):
    'TABLA_REF : ID AS ID'

    t[0] = str(t[1]) + str(t[2]) + str(t[3])



#-----------------------------------------------------------------------------------------------------------------
#Groups


def p_Groups_ListaG(t):
    'GROUPS : GROUPS GROUPP'

    t[1].append(t[2])
    t[0] = t[1]



def p_Groups_ListaG(t):
    'GROUPS    : GROUPP'

    t[0] = [t[1]]



def p_Group_GroupBy(t):
    'GROUPP    : GROUP BY EXPRE_LIST MORE_ORDER'

    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])



def p_Group_GroupBySin(t):
    'GROUPP    : GROUP BY EXPRE_LIST'

    t[0] = str(t[1]) + str(t[2]) + str(t[3])




def p_ExpreList_Lista(t):
    'EXPRE_LIST : EXPRE_LIST  EXPRES'

    t[1].append(t[2])
    t[0] = t[1]

def p_ExpreList_Expresion(t):
    'EXPRE_LIST    : EXPRES'

    t[0] = [t[1]]



def p_Expre_Campo1(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS S2'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Expre_Campo2(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS '
    t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Expre_Campo3(t):
    'EXPRES    :  CAMPOS S2 '
    t[0] = str(t[1]) + str(t[2])


def p_Expre_Campo4(t):
    'EXPRES    :  CAMPOS '
    t[0] = str(t[1])



def p_Expre_Campo5(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS S2 STATE '
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])




def p_Expre_Campo6(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS STATE'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])



def p_Expre_Campo7(t):
    'EXPRES    :  CAMPOS S2 STATE'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Expre_Campo8(t):
    'EXPRES    :  CAMPOS STATE '
    t[0] = str(t[1]) + str(t[2])



def p_S2(t):
    'S2 : COMA EXPRES'
    t[0] = str(t[1]) + str(t[2])


def p_S2(t):
    'S2 : AS ALIAS'
    t[0] = str(t[1]) + str(t[2])


def p_MoreOrder_Having(t):
    'MORE_ORDER  :  HAVING CONDICIONES'
    t[0] = str(t[1]) + str(t[2])


def p_State_orden1(t):
    'STATE : ASC'
    t[0] = str(t[1])


def p_State_orden2(t):
    'STATE : ASC NULLS FIRST'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_State_orden3(t):
    'STATE : ASC NULLS LAST'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_State_orden4(t):
    'STATE : DESC '
    t[0] = str(t[1])



def p_State_orden5(t):
    'STATE : DESC NULLS FIRST'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_State_orden6(t):
    'STATE : DESC NULLS LAST'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])


























#MI GRANATICA CESAR SAZO------------------------
# CREATE TABLE


def p_instruccion_dml_comandos_CREATE_TABLE(t) :
    'DQL_COMANDOS       : CREATE TABLE NOMBRES_TABLAS PARIZQ  CUERPO_CREATE_TABLE PARDER PUNTOCOMA'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])
    print('\n' + str(t[0]) + '\n')

def p_instruccion_dml_comandos_CUERPO(t) :
    'CUERPO_CREATE_TABLE       : LISTA_DE_COLUMNAS'
    t[1].append(t[1])
    t[0] = t[1]


#LISTA DE COLUMNAS------------------------------------
def p_CREATE_TABLE_LISTA_CAMPOS(t):
    'LISTA_DE_COLUMNAS       : LISTA_DE_COLUMNAS LISTA2'
    t[1].append(t[2])
    t[0] = t[1]


def p_CREATE_TABLE_LISTA2_CAMPOS(t):
    'LISTA_DE_COLUMNAS    : LISTA2'
    t[0] = [t[1]]



def p_Create_TABLE_CAMPOS(t):
    'LISTA2          : NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE COMA'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Create_TABLE_CAMPOS2(t):
    'LISTA2          : NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_Create_TABLE_TIPO_CAMPO(t):
    '''TIPO_CAMPO   : SMALLINT
                    | INTEGER
                    | BIGINT
                    | DECIMAL
                    | REAL
                    | MONEY
                    | DOUBLE PRECISION
                    | CHARACTER VARYING PARIZQ ENTERO PARDER
                    | VARCHAR PARIZQ ENTERO PARDER
                    | CHARACTER PARIZQ ENTERO PARDER
                    | CHAR PARIZQ ENTERO PARDER
                    | TEXT
                    | BOOLEAN'''
    t[0] = str(t[1])

def p_CREATE_TABLE_LISTA3_CAMPOS(t):
    'VALIDACIONES_CREATE_TABLE    : LISTA3'
    t[0] = [t[1]]


def p_Create_TABLE_CAMPOS3(t):
    'LISTA3          :  VALIDACION_CAMPO_CREATE '
    t[0] = str(t[1])

def p_Create_TABLE_CAMPOS4(t):
    'LISTA3          :  VALIDACION_CAMPO_CREATE_VACIO '
    t[0] = str(t[1])


def p_Create_TABLE_TIPO_CAMPO2(t):
    '''VALIDACION_CAMPO_CREATE  : NOT NULL
                                | DEFAULT CADENASIMPLE
                                | DEFAULT CADENADOBLE
                                | DEFAULT FLOTANTE
                                | DEFAULT ENTERO '''
    t[0] = str(t[1])

def p_Create_TABLE_TIPO_CAMPO3(t):
    'VALIDACION_CAMPO_CREATE_VACIO  :  '


def p_Create_TABLE_TIPO_CAMPO4(t):
    '''VALIDACION_CAMPO_CREATE  : NULL  '''
    t[0] = str(t[1])


#DDL
#-----------------------------------------------------------------------------------------------------------------
def p_comando_ddl(t):
    '''DDL_COMANDOS : CREATE_DATABASE
                    | SHOW_DATABASES
                    | ALTER_DATABASE
                    | DROP_DATABASE'''

    t[0] = str(t[1])
    print('\n' + str(t[0]) + '\n')
def p_create_database(t):
    'CREATE_DATABASE : CREATE REPLACE_OP DATABASE IF_NOT_EXISTIS ID OWNER_DATABASE MODE_DATABASE'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])

def p_replace_op(t):
    'REPLACE_OP : OR REPLACE'
    t[0] = str(t[1]) + str(t[2])

def p_replace_op_e(t):
    'REPLACE_OP : '
    t[0] = ''

def p_if_not_exists(t):
    'IF_NOT_EXISTIS : IF NOT EXISTS'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_if_not_exists_e(t):
    'IF_NOT_EXISTIS : '
    t[0] = ''

def p_owner_database(t):
    'OWNER_DATABASE : OWNER IGUAL ID'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_owner_database_e(t):
    'OWNER_DATABASE : '
    t[0] = ''

def p_mode_database(t):
    'MODE_DATABASE : MODE IGUAL ENTERO'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_mode_database_e(t):
    'MODE_DATABASE : '
    t[0] = ''

def p_show_databases(t):
    'SHOW_DATABASES : SHOW DATABASES SHOW_DATABASES_LIKE'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_show_databases_like(t):
    'SHOW_DATABASES_LIKE : LIKE CADENADOBLE'
    t[0] = str(t[1]) + str(t[2])

def p_show_databases_like_e(t):
    'SHOW_DATABASES_LIKE : '
    t[0] = ''

def p_alter_database(t):
    'ALTER_DATABASE : ALTER DATABASE ID ALTER_DATABASE_OP'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])

def p_alter_database_op(t):
    '''ALTER_DATABASE_OP : RENAME TO ID
                        |  OWNER TO ALTER_TABLE_OP_OW'''
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_alter_database_op_ow(t):
    '''ALTER_TABLE_OP_OW : ID
                        |  CURRENT_USER
                        |  SESSION_USER'''
    t[0] = str(t[1])

def p_alter_database_op_e(t):
    'ALTER_DATABASE_OP : '
    t[0] = ''

def p_drop_database(t):
    'DROP_DATABASE : DROP DATABASE IF_EXISTS_DATABASE ID'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])

def p_if_exists_database(t):
    'IF_EXISTS_DATABASE : IF EXISTS'
    t[0] = str(t[1]) + str(t[2])

def p_if_exists_database_e(t):
    'IF_EXISTS_DATABASE : '
    t[0] = ''

#Expresiones numericas
#-----------------------------------------------------------------------------------------------------------------

def p_expnumerica(t):
    '''EXPNUMERICA : EXPNUMERICA MAS EXPNUMERICA
                   | EXPNUMERICA MENOS EXPNUMERICA
                   | EXPNUMERICA ASTERISCO EXPNUMERICA
                   | EXPNUMERICA DIVISION EXPNUMERICA
                   | EXPNUMERICA PORCENTAJE EXPNUMERICA'''
    t[0] = str(t[1]) + str(t[2]) + str(t[3])
    print('\n'+t[0]+'\n')

#-----------------------------------------------------------------------------------------------------------------

def p_expnumerica_agrupacion(t):
    '''EXPNUMERICA : PARIZQ EXPNUMERICA PARDER'''
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_expnumerica_valor(t):
    '''EXPNUMERICA : ID
                   | ENTERO
                   | FLOTANTE'''

    t[0] = str(t[1])

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print(input)

parser.parse(input)