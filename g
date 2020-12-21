graph g {
	node [height=.1 shape=plaintext]
	table [label=<<TABLE><TR><TD>PRODUCCION</TD><TD>REGLAS SEMANTICAS</TD></TR>
 <TR><TD> REPLACE_OP →   </TD><TD> t[0] = 0 </TD></TR>
 <TR><TD> IF_NOT_EXISTIS →   </TD><TD> t[0] = 0 </TD></TR>
 <TR><TD> OWNER_DATABASE →  OWNER IGUAL ID </TD><TD> t[0] = t[3] </TD></TR>
 <TR><TD> MODE_DATABASE →  MODE IGUAL ENTERO  </TD><TD> t[0] = t[3] </TD></TR>
 <TR><TD> CREATE_DATABASE → CREATE REPLACE_OP DATABASE IF_NOT_EXISTIS ID OWNER_DATABASE MODE_DATABASE PUNTOCOMA  </TD><TD> t[0] = CreateDataBase(t[2], t[4], t[5], t[6], t[7])  </TD></TR>
 <TR><TD> DDL_COMANDOS → OPERACION DDL_COMANDOS   </TD><TD> t[0] = t[1]  </TD></TR>
 <TR><TD> INSTRUCCIONES → INSTRUCCION </TD><TD> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> DQL_COMANDOS → USE ID PUNTOCOMA </TD><TD> DQL_COMANDOS=t[2] </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> NOMBRE_T → carne    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> TIPO_CAMPO →   INT  </TD><TD>   t[0] = t[1]  </TD></TR>
 <TR><TD> LISTA3 →    VALIDACION_CAMPO_CREATE_VACIO    </TD><TD>  t[0] = [t[1]]  </TD></TR>
 <TR><TD> VALIDACIONES_CREATE_TABLE →  LISTA3  </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTA2 →     NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE COMA  </TD><TD> t[0] = CampoTabla(t[1], t[2], t[3]) </TD></TR>
 <TR><TD> LISTA_DE_COLUMNAS →     LISTA2 </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> NOMBRE_T → nombre    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> TIPO_CAMPO →   INT  </TD><TD>   t[0] = t[1]  </TD></TR>
 <TR><TD> LISTA3 →    VALIDACION_CAMPO_CREATE_VACIO    </TD><TD>  t[0] = [t[1]]  </TD></TR>
 <TR><TD> VALIDACIONES_CREATE_TABLE →  LISTA3  </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTA2 →     NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE COMA  </TD><TD> t[0] = CampoTabla(t[1], t[2], t[3]) </TD></TR>
 <TR><TD> LISTA_DE_COLUMNAS →   LISTA_DE_COLUMNAS  LISTA2 </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> NOMBRE_T → apellido    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> TIPO_CAMPO →   TIPO TEXTO PARIZQ expresion_aritmetica PARDER  </TD><TD>  t[0] = valorTipo(t[1], t[3]) </TD></TR>
 <TR><TD> LISTA3 →    VALIDACION_CAMPO_CREATE_VACIO    </TD><TD>  t[0] = [t[1]]  </TD></TR>
 <TR><TD> VALIDACIONES_CREATE_TABLE →  LISTA3  </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTA2 →     NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE COMA  </TD><TD> t[0] = CampoTabla(t[1], t[2], t[3]) </TD></TR>
 <TR><TD> LISTA_DE_COLUMNAS →   LISTA_DE_COLUMNAS  LISTA2 </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> NOMBRE_T → bandera    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> TIPO_CAMPO →   BOOLEAN  </TD><TD>   t[0] = t[1]  </TD></TR>
 <TR><TD> LISTA3 →    VALIDACION_CAMPO_CREATE_VACIO    </TD><TD>  t[0] = [t[1]]  </TD></TR>
 <TR><TD> VALIDACIONES_CREATE_TABLE →  LISTA3  </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTA2 →     NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE   </TD><TD> t[0] = CampoTabla(t[1], t[2], t[3]) </TD></TR>
 <TR><TD> LISTA_DE_COLUMNAS →   LISTA_DE_COLUMNAS  LISTA2 </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> CUERPO_CREATE_TABLE →   LISTA_DE_COLUMNAS </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> DML_COMANDOS →   CREATE TABLE ID PARIZQ  CUERPO_CREATE_TABLE PARDER PUNTOCOMA </TD><TD> t[0] = CreateTable(t[3], t[5], None)  </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> LISTA_ID_ →   ID  </TD><TD>   t[0] = ExpresionValor(t[1])  </TD></TR>
 <TR><TD> LISTA_DE_IDS →  LISTA_DE_IDS LISTA_ID_ </TD><TD>   t[1].append(t[2]) t[0] = t[1]  </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →      VALOR   </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → CADENAS   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → BOOLENA   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion    </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> DATOS →   VALUES PARIZQ VALORES PARDER  </TD><TD> t[0] = t[3] </TD></TR>
 <TR><TD> DML_COMANDOS →   INSERT INTO  LISTA_DE_IDS DATOS PUNTOCOMA   </TD><TD>  t[0] = Insert_Datos(t[3], t[4]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> LISTA_ID_ →   ID  </TD><TD>   t[0] = ExpresionValor(t[1])  </TD></TR>
 <TR><TD> LISTA_DE_IDS →  LISTA_DE_IDS LISTA_ID_ </TD><TD>   t[1].append(t[2]) t[0] = t[1]  </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →      VALOR   </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → CADENAS   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → BOOLENA   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion    </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> DATOS →   VALUES PARIZQ VALORES PARDER  </TD><TD> t[0] = t[3] </TD></TR>
 <TR><TD> DML_COMANDOS →   INSERT INTO  LISTA_DE_IDS DATOS PUNTOCOMA   </TD><TD>  t[0] = Insert_Datos(t[3], t[4]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> LISTA_ID_ →   ID  </TD><TD>   t[0] = ExpresionValor(t[1])  </TD></TR>
 <TR><TD> LISTA_DE_IDS →  LISTA_DE_IDS LISTA_ID_ </TD><TD>   t[1].append(t[2]) t[0] = t[1]  </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →      VALOR   </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → CADENAS   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → BOOLENA   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion    </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> DATOS →   VALUES PARIZQ VALORES PARDER  </TD><TD> t[0] = t[3] </TD></TR>
 <TR><TD> DML_COMANDOS →   INSERT INTO  LISTA_DE_IDS DATOS PUNTOCOMA   </TD><TD>  t[0] = Insert_Datos(t[3], t[4]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> LISTA_ID_ →   ID  </TD><TD>   t[0] = ExpresionValor(t[1])  </TD></TR>
 <TR><TD> LISTA_DE_IDS →  LISTA_DE_IDS LISTA_ID_ </TD><TD>   t[1].append(t[2]) t[0] = t[1]  </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →      VALOR   </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → CADENAS   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → BOOLENA   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion    </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> DATOS →   VALUES PARIZQ VALORES PARDER  </TD><TD> t[0] = t[3] </TD></TR>
 <TR><TD> DML_COMANDOS →   INSERT INTO  LISTA_DE_IDS DATOS PUNTOCOMA   </TD><TD>  t[0] = Insert_Datos(t[3], t[4]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> LISTA_ID_ →   ID  </TD><TD>   t[0] = ExpresionValor(t[1])  </TD></TR>
 <TR><TD> LISTA_DE_IDS →  LISTA_DE_IDS LISTA_ID_ </TD><TD>   t[1].append(t[2]) t[0] = t[1]  </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →      VALOR   </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → CADENAS   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → BOOLENA   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion    </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> DATOS →   VALUES PARIZQ VALORES PARDER  </TD><TD> t[0] = t[3] </TD></TR>
 <TR><TD> DML_COMANDOS →   INSERT INTO  LISTA_DE_IDS DATOS PUNTOCOMA   </TD><TD>  t[0] = Insert_Datos(t[3], t[4]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> LISTA_ID_ →   ID  </TD><TD>   t[0] = ExpresionValor(t[1])  </TD></TR>
 <TR><TD> LISTA_DE_IDS →  LISTA_DE_IDS LISTA_ID_ </TD><TD>   t[1].append(t[2]) t[0] = t[1]  </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →      VALOR   </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → CADENAS   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> expresion_aritmetica → BOOLENA   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>
 <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>
 <TR><TD> VALOR →      expresion    </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>
 <TR><TD> DATOS →   VALUES PARIZQ VALORES PARDER  </TD><TD> t[0] = t[3] </TD></TR>
 <TR><TD> DML_COMANDOS →   INSERT INTO  LISTA_DE_IDS DATOS PUNTOCOMA   </TD><TD>  t[0] = Insert_Datos(t[3], t[4]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> LISTA_CS →  CADENASIMPLE COMA </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> LISTAS_CS →  LISTA_CS </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> LISTA_CS →  CADENASIMPLE COMA </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> LISTAS_CS → LISTAS_CS LISTA_CS </TD><TD> t[1].append(t[2])  t[0] = t[1] </TD></TR>
 <TR><TD> LISTA_CS →  CADENASIMPLE  </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> LISTAS_CS → LISTAS_CS LISTA_CS </TD><TD> t[1].append(t[2])  t[0] = t[1] </TD></TR>
 <TR><TD> DQL_COMANDOS → CREATE TYPE ID AS ENUM PARIZQ  LISTAS_CS PARDER PUNTOCOMA </TD><TD> t[0] = CreacionEnum(t[3], t[7])  </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> LISTA_CS →  CADENASIMPLE COMA </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> LISTAS_CS →  LISTA_CS </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> LISTA_CS →  CADENASIMPLE COMA </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> LISTAS_CS → LISTAS_CS LISTA_CS </TD><TD> t[1].append(t[2])  t[0] = t[1] </TD></TR>
 <TR><TD> LISTA_CS →  CADENASIMPLE  </TD><TD> t[0] = t[1] </TD></TR>
 <TR><TD> LISTAS_CS → LISTAS_CS LISTA_CS </TD><TD> t[1].append(t[2])  t[0] = t[1] </TD></TR>
 <TR><TD> DQL_COMANDOS → CREATE TYPE ID AS ENUM PARIZQ  LISTAS_CS PARDER PUNTOCOMA </TD><TD> t[0] = CreacionEnum(t[3], t[7])  </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> DISTINCTNT →  DISTINCT    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA → carne    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA →  CAMPOS   </TD><TD> t[0] = Campo_AccedidoSinLista("",t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →   LISTAA     </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> LISTAA →  COMA ,   </TD><TD>  t[0] = str(t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →  LISTA_CAMPOS LISTAA     </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA → apellido    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA →  CAMPOS   </TD><TD> t[0] = Campo_AccedidoSinLista("",t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →  LISTA_CAMPOS LISTAA     </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA →  COMA ,   </TD><TD>  t[0] = str(t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →  LISTA_CAMPOS LISTAA     </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA → bandera    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA →  CAMPOS   </TD><TD> t[0] = Campo_AccedidoSinLista("",t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →  LISTA_CAMPOS LISTAA     </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>
 <TR><TD> NOMBRE_T → profesional    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> TABLA →   NOMBRE_T   </TD><TD>  t[0] = AccesoTablaSinLista(t[1]) </TD></TR>
 <TR><TD> NOMBRES_TABLAS →  TABLA   </TD><TD>  t[0] = [t[1]] </TD></TR>
 <TR><TD> UNIONN →   PUNTOCOMA  </TD><TD> t[0] = CamposUnions(t[1],,False) </TD></TR>
 <TR><TD> UNIONS →   UNIONN  </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> DQL_COMANDOS → SELECT DISTINCTNT LISTA_CAMPOS FROM  NOMBRES_TABLAS  UNIONS   </TD><TD> t[0] = Select4(t[2], t[7],t[6], t[3], t[5]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> DISTINCTNT →  DISTINCT    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA → carne    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA →  CAMPOS   </TD><TD> t[0] = Campo_AccedidoSinLista("",t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →   LISTAA     </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> NOMBRE_T → profesional    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> TABLA →   NOMBRE_T   </TD><TD>  t[0] = AccesoTablaSinLista(t[1]) </TD></TR>
 <TR><TD> NOMBRES_TABLAS →  TABLA   </TD><TD>  t[0] = [t[1]] </TD></TR>
 <TR><TD> UNIONN →   PUNTOCOMA  </TD><TD> t[0] = CamposUnions(t[1],,False) </TD></TR>
 <TR><TD> UNIONS →   UNIONN  </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> DQL_COMANDOS → SELECT DISTINCTNT LISTA_CAMPOS FROM  NOMBRES_TABLAS  UNIONS   </TD><TD> t[0] = Select4(t[2], t[7],t[6], t[3], t[5]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> DISTINCTNT →  DISTINCT    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA → apellido    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTALIASS →   ID    </TD><TD>   t[0] = Alias_Campos_ListaCamposSinLista(t[1])  </TD></TR>
 <TR><TD> LISTAA →  CAMPOS ARRAY[]  </TD><TD> t[0] = Campo_Accedido(NULLL, t[1], t[2]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →   LISTAA     </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> NOMBRE_T → profesional    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> TABLA →   NOMBRE_T   </TD><TD>  t[0] = AccesoTablaSinLista(t[1]) </TD></TR>
 <TR><TD> NOMBRES_TABLAS →  TABLA   </TD><TD>  t[0] = [t[1]] </TD></TR>
 <TR><TD> UNIONN →   PUNTOCOMA  </TD><TD> t[0] = CamposUnions(t[1],,False) </TD></TR>
 <TR><TD> UNIONS →   UNIONN  </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> DQL_COMANDOS → SELECT DISTINCTNT LISTA_CAMPOS FROM  NOMBRES_TABLAS  UNIONS   </TD><TD> t[0] = Select4(t[2], t[7],t[6], t[3], t[5]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> DISTINCTNT →  DISTINCT    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA → bandera    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTALIASS →   ID    </TD><TD>   t[0] = Alias_Campos_ListaCamposSinLista(t[1])  </TD></TR>
 <TR><TD> LISTAA →  CAMPOS ARRAY[]  </TD><TD> t[0] = Campo_Accedido(NULLL, t[1], t[2]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →   LISTAA     </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> LISTAA →  COMA ,   </TD><TD>  t[0] = str(t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →  LISTA_CAMPOS LISTAA     </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA → carne    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTALIASS →   ID    </TD><TD>   t[0] = Alias_Campos_ListaCamposSinLista(t[1])  </TD></TR>
 <TR><TD> LISTAA →  CAMPOS ARRAY[]  </TD><TD> t[0] = Campo_Accedido(NULLL, t[1], t[2]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →  LISTA_CAMPOS LISTAA     </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>
 <TR><TD> NOMBRE_T → profesional    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> TABLA →   NOMBRE_T   </TD><TD>  t[0] = AccesoTablaSinLista(t[1]) </TD></TR>
 <TR><TD> NOMBRES_TABLAS →  TABLA   </TD><TD>  t[0] = [t[1]] </TD></TR>
 <TR><TD> UNIONN →   PUNTOCOMA  </TD><TD> t[0] = CamposUnions(t[1],,False) </TD></TR>
 <TR><TD> UNIONS →   UNIONN  </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> DQL_COMANDOS → SELECT DISTINCTNT LISTA_CAMPOS FROM  NOMBRES_TABLAS  UNIONS   </TD><TD> t[0] = Select4(t[2], t[7],t[6], t[3], t[5]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>
 <TR><TD> DISTINCTNT →  DISTINCT    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA → carne    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA →  CAMPOS   </TD><TD> t[0] = Campo_AccedidoSinLista("",t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →   LISTAA     </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> LISTAA →  COMA ,   </TD><TD>  t[0] = str(t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →  LISTA_CAMPOS LISTAA     </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA → apellido    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> LISTAA →  CAMPOS   </TD><TD> t[0] = Campo_AccedidoSinLista("",t[1]) </TD></TR>
 <TR><TD> LISTA_CAMPOS →  LISTA_CAMPOS LISTAA     </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>
 <TR><TD> NOMBRE_T → profesional    </TD><TD>  t[0] = t[1] </TD></TR>
 <TR><TD> TABLA →   NOMBRE_T   </TD><TD>  t[0] = AccesoTablaSinLista(t[1]) </TD></TR>
 <TR><TD> NOMBRES_TABLAS →  TABLA   </TD><TD>  t[0] = [t[1]] </TD></TR>
 <TR><TD> UNIONN →   PUNTOCOMA  </TD><TD> t[0] = CamposUnions(t[1],,False) </TD></TR>
 <TR><TD> UNIONS →   UNIONN  </TD><TD> t[0] = [t[1]] </TD></TR>
 <TR><TD> DQL_COMANDOS → SELECT DISTINCTNT LISTA_CAMPOS FROM  NOMBRES_TABLAS  UNIONS   </TD><TD> t[0] = Select4(t[2], t[7],t[6], t[3], t[5]) </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR></TABLE>>]
}
