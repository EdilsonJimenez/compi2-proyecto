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
                            <TR><TD>tbProducto</TD><TD>idproducto</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbProducto</TD><TD>idproducto</TD><TD>primary</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbProducto</TD><TD>producto</TD><TD>not</TD><TD>auto</TD><TD></TD></TR><TR><TD>tbProducto</TD><TD>fechacreacion</TD><TD>not</TD><TD>auto</TD><TD></TD></TR> <TR>
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
                            </TR><TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR><TR><TD>tbProducto</TD><TD>idproducto</TD><TD>integer</TD><TD></TD><TD></TD></TR><TR><TD>tbProducto</TD><TD>producto</TD><TD>varchar(150)</TD><TD></TD><TD></TD></TR><TR><TD>tbProducto</TD><TD>fechacreacion</TD><TD>date</TD><TD></TD><TD></TD></TR><TR><TD>tbProducto</TD><TD>estado</TD><TD>integer</TD><TD></TD><TD></TD></TR> <TR>
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
                            </TR><TR><TD>DBFase2</TD><TD></TD><TD></TD><TD></TD><TD></TD></TR>
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
                            </TR><TR><TD>idx_producto</TD><TD>tbProducto</TD><TD>True</TD><TD>False</TD><TD></TD></TR>
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
                            </TR><TR><TD>idproducto</TD><TD>None</TD><TD>None</TD><TD>tbProducto</TD><TD>idx_producto</TD></TR></TABLE>>]
}
