from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	t0 = """CREATE DATABASE DBFase2;"""
	heap.append(t0)
	F3D.ejecutarSQL()

	t1 = """USE DBFase2;"""
	heap.append(t1)
	F3D.ejecutarSQL()

	t2 = """
 CREATE TABLE tbProducto (
  
 idproducto  integer   not null     primary key    
,   
 producto  varchar( 150)   not null    
,   
 fechacreacion  date   not null    
,   
 estado  integer  
  );
"""
	heap.append(t2)
	F3D.ejecutarSQL()

	t3 = """
 CREATE TABLE tbCalificacion (
  
 idcalifica  integer   not null     primary key    
,   
 item  varchar( 100)   not null    
,   
 punteo  integer   not null    
  );
"""
	heap.append(t3)
	F3D.ejecutarSQL()

	t4 = """ INSERT INTO   tbProducto  values(  1,  "Laptop Lenovo",  NOW(),  1   );"""
	heap.append(t4)
	F3D.ejecutarSQL()

	t5 = """ INSERT INTO   tbProducto  values(  2,  "Bateria para Laptop Lenovo T420",  NOW(),  1   );"""
	heap.append(t5)
	F3D.ejecutarSQL()

	t6 = """ INSERT INTO   tbProducto  values(  3,  "Teclado Inalambrico",  NOW(),  1   );"""
	heap.append(t6)
	F3D.ejecutarSQL()

	t7 = """ INSERT INTO   tbProducto  values(  4,  "Mouse Inalambrico",  NOW(),  1   );"""
	heap.append(t7)
	F3D.ejecutarSQL()

	t8 = """ INSERT INTO   tbProducto  values(  5,  "WIFI USB",  NOW(),  1   );"""
	heap.append(t8)
	F3D.ejecutarSQL()

	t9 = """ INSERT INTO   tbProducto  values(  6,  "Laptop HP",  NOW(),  1   );"""
	heap.append(t9)
	F3D.ejecutarSQL()

	t10 = """ INSERT INTO   tbProducto  values(  7,  "Teclado Flexible USB",  NOW(),  1   );"""
	heap.append(t10)
	F3D.ejecutarSQL()

	t11 = """ INSERT INTO   tbProducto  values(  8,  "Laptop Samsung",  "2021-01-02",  1   );"""
	heap.append(t11)
	F3D.ejecutarSQL()

	t12 = """Select  * from tbProducto; 
"""
	heap.append(t12)
	F3D.ejecutarSQL()


	goto .END

	label .F1
	#**** Funcion *****

	# Parametros 
	p0

	# Retorno 
	global r0

	# Declaraciones 
	#Fin declaraciones


	#Llamada a funcion o procedimiento.
	stack.append("F2")
	label .F2

	# Return
	r0 = p0
	goto .R


	goto .R


	label .R
	u = stack.pop()
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2

	label .END
