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
    'on': 'ON',
    'and': 'AND',
    'or': 'OR',
    'insert': 'INSERT',
    'into': 'INTO',
    'update': 'UPDATE',
    'set': 'SET',
    'delete': 'DELETE',
    'values': 'VALUES'

}







tokens = [

             # SIMBOLOS UTILIZADOS EN EL LENGUAJE
             'DIFERENTE',
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

             # ESTOS SON LAS EXPRESIONES REGULARES
             'ID',
             'ENTERO',
             'DECIMAL',
             'CADENASIMPLE',
             'CADENADOBLE',
             'FECHA',

             'COMENTARIOMULTI',
             'COMENTARIONORMAL'

         ] + list(reservadas.values())



# TOKENS DE LOS SIMBOLOS UTILIZADOS EN EL LENGUAJE
t_DIFERENTE = r'!='
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



def t_DECIMAL(t):
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
    '''INSTRUCCION     : DQL_COMANDOS'''
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

def p_Disctint_Rw(t):
    'DISTINCTNT          : DISTINCT'
    t[0] = str(t[1])




#------------------------------------------------------------------------------------------------------------------






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





def p_Cuerpo_Where(t):
    'CUERPO   : WHERE CONDICIONES'

    t[0] = str(t[1]) + str(t[2])
    #print('\n' + str(t[1]) + str(t[2]) + '\n')


def p_Cuerpo_Inners(t):
    'CUERPO   : INNERS'

    t[0] = str(t[1])
   # print('\n' + str(t[1]) + '\n')


#-----------------------------------------------------------------------------------------------------------------



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


def p_OtroLogico_SimboloLogic(t):

    'OTRO_LOGICO : SIMBOLO_LOGICO CONDICIONES'

    t[0] = str(t[1]) + str(t[2])


def p_CondicionRel_Expresionn(t):
    'CONDICION_REL : EXPRESIONNE OPERADOR EXPRESIONNE'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])



#-----------------------------------------------------------------------------------------------------------------

def p_Inners_Lista(t):
    'INNERS : INNERS INNERR'

    t[1].append(t[2])
    t[0] = t[1]



def p_Inners_Inner(t):
    'INNERS : INNERR'

    t[0] = [t[1]]



def p_Inner_InnerJoin(t):
    'INNERR : INNER JOIN TABLA_REF ON CONDICIONES'

    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])



def p_Inner_Join(t):
    'INNERR :  JOIN TABLA_REF ON CONDICIONES'

    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])



def p_Inner_Where(t):
    'INNERR   : WHERE CONDICIONES'

    t[0] = str(t[1]) + str(t[2])
    #print('\n' + str(t[1]) + str(t[2]) + '\n')


def p_TablaRef_Id(t):
    'TABLA_REF : ID'

    t[0] = t[1]

def p_TablaRef_IdAS(t):
    'TABLA_REF : ID AS ID'

    t[0] = str(t[1]) + str(t[2]) + str(t[3])


#------------------------------------------------------------------------------------------------------------------

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


def p_NombreC_id(t):
    'NOMBRE_C : ID'

    t[0] = str(t[1])




def p_CamposC_id(t):
    '''CAMPOSC     :  ID
                    | ENTERO
                    | DECIMAL
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














#-----------------------------------------------------------------------------------------------------------------













def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print(input)

parser.parse(input)