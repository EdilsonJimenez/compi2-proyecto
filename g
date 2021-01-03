graph g {
	node [height=.1 shape=plaintext]
	table [label=<<TABLE border="1" cellpadding="0" cellspacing="0"   >
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>DATOS</B> </TD>
                            </TR>
                            <TR bgcolor="#BEF781">
                                <TD bgcolor="#BEF781">BASE DATOS</TD>
                                <TD bgcolor="#BEF781">TABLA</TD>
                                <TD bgcolor="#BEF781">COLUMNA</TD>
                                <TD bgcolor="#BEF781">VALOR </TD>
                                <TD bgcolor="#BEF781">FILA</TD>
                            </TR>
                             <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>VALIDACIONES</B> </TD>
                            </TR>
                            <TR bgcolor="#BEF781">
                                <TD bgcolor="#BEF781">TABLA</TD>
                                <TD bgcolor="#BEF781">CAMPO</TD>
                                <TD bgcolor="#BEF781">TIPO</TD>
                                <TD bgcolor="#BEF781">ID</TD>
                                <TD bgcolor="#BEF781"> </TD>
                            </TR>
                            <TR><TD>tbcalifica</TD><TD>iditem</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbcalifica</TD><TD>iditem</TD><TD>primary</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbcalifica</TD><TD>item</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbcalifica</TD><TD>puntos</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>idusuario</TD><TD>NOT</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>idusuario</TD><TD>primary</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>usuario</TD><TD>UNIQUE</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>usuario</TD><TD>NOT</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>password</TD><TD>NOT</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbroles</TD><TD>idrol</TD><TD>NOT</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbroles</TD><TD>idrol</TD><TD>primary</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbrol</TD><TD>idrol</TD><TD>NOT</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbrol</TD><TD>idrol</TD><TD>primary</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbrolxusuario</TD><TD>idrol</TD><TD>NOT</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbrolxusuario</TD><TD>idusuario</TD><TD>NOT</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbrolxusuario</TD><TD>idrol</TD><TD>FOREIGN KEY</TD><TD>FK_rol</TD><TD></TD></TR><TR><TD>tbrolxusuario</TD><TD>idusuario</TD><TD>FOREIGN KEY</TD><TD>FK_usuario</TD><TD></TD></TR><TR><TD>tbcalifica2</TD><TD>iditem</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbcalifica2</TD><TD>iditem</TD><TD>primary</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbcalifica2</TD><TD>item</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbcalifica2</TD><TD>puntos</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbestado</TD><TD>idestado</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbestado</TD><TD>idestado</TD><TD>PRIMARY</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>idempleado</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>idempleado</TD><TD>UNIQUE</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>idempleado</TD><TD>PRIMARY</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>primernombre</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>primerapellido</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>idestado</TD><TD>FOREIGN KEY</TD><TD>FK_estado</TD><TD></TD></TR><TR><TD>tbempleadoidentificacion</TD><TD>idempleado</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleadoidentificacion</TD><TD>idempleado</TD><TD>primary</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleadoidentificacion</TD><TD>identificacion</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbidentificaciontipo</TD><TD>ididentificaciontipo</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbidentificaciontipo</TD><TD>ididentificaciontipo</TD><TD>primary</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleadoidentificacion</TD><TD>ididentificaciontipo</TD><TD>FOREIGN KEY</TD><TD>FK_identificaciontipo</TD><TD></TD></TR><TR><TD>tbempleadopuesto</TD><TD>idempleado</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleadopuesto</TD><TD>idpuesto</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbempleadopuesto</TD><TD>idempleado</TD><TD>FOREIGN KEY</TD><TD>FK_empleado</TD><TD></TD></TR><TR><TD>tbempleadopuesto</TD><TD>idempleado</TD><TD>FOREIGN KEY</TD><TD>FK_empleado</TD><TD></TD></TR><TR><TD>tbfuncionesmath</TD><TD>idfuncion</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbfuncionesmath</TD><TD>idfuncion</TD><TD>primary</TD><TD>auto</TD><TD></TD></TR> <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"><B> TABLAS</B> </TD>
                            </TR>
                            <TR bgcolor="#BEF781">
                                <TD bgcolor="#BEF781">ID TABLA</TD>
                                <TD bgcolor="#BEF781">ID COLUMNA</TD>
                                <TD bgcolor="#BEF781">TIPO COLUMNA</TD>
                                <TD bgcolor="#BEF781">  </TD>
                                <TD bgcolor="#BEF781">  </TD>
                            </TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbcalifica</TD><TD>iditem</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbcalifica</TD><TD>item</TD><TD>varchar(150)</TD><TD></TD><TD></TD></TR><TR><TD>tbcalifica</TD><TD>puntos</TD><TD>decimal</TD><TD></TD><TD></TD></TR><TR><TD>tbcalifica</TD><TD>seccion</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbcalifica</TD><TD>seccion</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbusuario</TD><TD>idusuario</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>nombre</TD><TD>varchar(50)</TD><TD></TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>apellido</TD><TD>varchar(50)</TD><TD></TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>usuario</TD><TD>varchar(15)</TD><TD></TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>password</TD><TD>varchar(80)</TD><TD></TD><TD></TD></TR><TR><TD>tbusuario</TD><TD>fechacreacion</TD><TD>date</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbroles</TD><TD>idrol</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbroles</TD><TD>rol</TD><TD>varchar(15)</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbrol</TD><TD>idrol</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbrol</TD><TD>rol</TD><TD>varchar(15)</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbrolxusuario</TD><TD>idrol</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbrolxusuario</TD><TD>idusuario</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbcalifica2</TD><TD>iditem</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbcalifica2</TD><TD>item</TD><TD>varchar(150)</TD><TD></TD><TD></TD></TR><TR><TD>tbcalifica2</TD><TD>puntos</TD><TD>decimal</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbestado</TD><TD>idestado</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbestado</TD><TD>estado</TD><TD>varchar(30)</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbempleado</TD><TD>idempleado</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>primernombre</TD><TD>varchar(50)</TD><TD></TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>segundonombre</TD><TD>varchar(50)</TD><TD></TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>primerapellido</TD><TD>varchar(50)</TD><TD></TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>segundoapellido</TD><TD>varchar(50)</TD><TD></TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>fechadenacimiento</TD><TD>DATE</TD><TD></TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>fechacontratacion</TD><TD>DATE</TD><TD></TD><TD></TD></TR><TR><TD>tbempleado</TD><TD>idestado</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>cities</TD><TD>name</TD><TD>text</TD><TD></TD><TD></TD></TR><TR><TD>cities</TD><TD>population</TD><TD>float</TD><TD></TD><TD></TD></TR><TR><TD>cities</TD><TD>elevation</TD><TD>int</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbempleadoidentificacion</TD><TD>idempleado</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbempleadoidentificacion</TD><TD>identificacion</TD><TD>varchar(25)</TD><TD></TD><TD></TD></TR><TR><TD>tbempleadoidentificacion</TD><TD>ididentificaciontipo</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbidentificaciontipo</TD><TD>ididentificaciontipo</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbidentificaciontipo</TD><TD>tipoidentificacion</TD><TD>varchar(20)</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbempleadopuesto</TD><TD>idempleado</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbempleadopuesto</TD><TD>idpuesto</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbempleadopuesto</TD><TD>departamento</TD><TD>varchar(50)</TD><TD></TD><TD></TD></TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbfuncionesmath</TD><TD>idfuncion</TD><TD>int</TD><TD></TD><TD></TD></TR><TR><TD>tbfuncionesmath</TD><TD>seno</TD><TD>decimal</TD><TD></TD><TD></TD></TR><TR><TD>tbfuncionesmath</TD><TD>coseno</TD><TD>decimal</TD><TD></TD><TD></TD></TR> <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>TIPOS </B></TD>
                            </TR>
                            <TR bgcolor="#BEF781">
                                <TD bgcolor="#BEF781">BASE DE DATOS</TD>
                                <TD bgcolor="#BEF781"> TIPO </TD>
                                <TD bgcolor="#BEF781">VALOR</TD>
                                <TD bgcolor="#BEF781">  </TD>
                                <TD bgcolor="#BEF781">  </TD>
                            </TR> <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>BASES DE DATOS</B> </TD>
                            </TR>
                            <TR>
                                <TD bgcolor="#BEF781">ID BASE DE DATOS</TD>
                                <TD bgcolor="#BEF781"></TD>
                                <TD bgcolor="#BEF781"></TD>
                                <TD bgcolor="#BEF781"></TD>
                                <TD bgcolor="#BEF781"></TD>
                            </TR><TR><TD>califica</TD><TD></TD><TD></TD><TD></TD><TD></TD></TR><TR><TD>test</TD><TD></TD><TD></TD><TD></TD><TD></TD></TR>
                            <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>INDICES</B> </TD>
                            </TR>
                            <TR>
                                <TD bgcolor="#BEF781">ID INDICE</TD>
                                <TD bgcolor="#BEF781">ID TABLA</TD>
                                <TD bgcolor="#BEF781">UNIQUE</TD>
                                <TD bgcolor="#BEF781">HASH</TD>
                                <TD bgcolor="#BEF781"></TD>
                            </TR>
                            <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>COLUMNAS INDICE</B> </TD>
                            </TR>
                            <TR>
                                <TD bgcolor="#BEF781">ID COLUMNA</TD>
                                <TD bgcolor="#BEF781">ORDEN</TD>
                                <TD bgcolor="#BEF781">NULLS</TD>
                                <TD bgcolor="#BEF781">ID INDICE</TD>
                                <TD bgcolor="#BEF781">ID TABLA</TD>
                            </TR></TABLE>>]
}
