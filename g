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
 <TR><TD> DML_COMANDOS →   CREATE TABLE ID PARIZQ  CUERPO_CREATE_TABLE PARDER PUNTOCOMA </TD><TD> t[0] = CreateTable(t[3], t[5], None)  </TD></TR><TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR></TABLE>>]
}
