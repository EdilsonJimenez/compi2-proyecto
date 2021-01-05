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

	#Llamada a funcion o procedimiento.
	p0="INICIO CALIFICACION FASE 2"
	stack.append("F2")
	goto .F1
	label .F2
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

	t3 = "CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);"
	heap.append(t3)
	F3D.ejecutarSQL()

	t4 = """
 CREATE TABLE tbCalificacion (
  
 idcalifica  integer   not null     primary key    
,   
 item  varchar( 100)   not null    
,   
 punteo  integer   not null    
  );
"""
	heap.append(t4)
	F3D.ejecutarSQL()

	t5 = "CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);"
	heap.append(t5)
	F3D.ejecutarSQL()

	t6 = """ INSERT INTO   tbProducto  values(  1,  "Laptop Lenovo",  NOW(),  1   );"""
	heap.append(t6)
	F3D.ejecutarSQL()

	t7 = """ INSERT INTO   tbProducto  values(  2,  "Bateria para Laptop Lenovo T420",  NOW(),  1   );"""
	heap.append(t7)
	F3D.ejecutarSQL()

	t8 = """ INSERT INTO   tbProducto  values(  3,  "Teclado Inalambrico",  NOW(),  1   );"""
	heap.append(t8)
	F3D.ejecutarSQL()

	t9 = """ INSERT INTO   tbProducto  values(  4,  "Mouse Inalambrico",  NOW(),  1   );"""
	heap.append(t9)
	F3D.ejecutarSQL()

	t10 = """ INSERT INTO   tbProducto  values(  5,  "WIFI USB",  NOW(),  1   );"""
	heap.append(t10)
	F3D.ejecutarSQL()

	t11 = """ INSERT INTO   tbProducto  values(  6,  "Laptop HP",  NOW(),  1   );"""
	heap.append(t11)
	F3D.ejecutarSQL()

	t12 = """ INSERT INTO   tbProducto  values(  7,  "Teclado Flexible USB",  NOW(),  1   );"""
	heap.append(t12)
	F3D.ejecutarSQL()

	t13 = """ INSERT INTO   tbProducto  values(  8,  "Laptop Samsung",  "2021-01-02",  1   );"""
	heap.append(t13)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p1="tbProducto"
	p2=8
	stack.append("F4")
	goto .F3
	label .F4
	t25 = """ INSERT INTO   tbCalificacion  values(  1,  "Create Table and Insert",  1   );"""
	heap.append(t25)
	F3D.ejecutarSQL()

	t26 = """ INSERT INTO   tbCalificacion  values(  2,  "Update",  1   );"""
	heap.append(t26)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p1="tbProductoUp"
	p2=2
	stack.append("F5")
	goto .F3
	label .F5
	#Llamada a funcion o procedimiento.
	stack.append("F7")
	goto .F6
	label .F7
	t32 = """ INSERT INTO   tbCalificacion  values(  3,  " Valida Funciones",  10   );"""
	heap.append(t32)
	F3D.ejecutarSQL()

	t33 = """
 CREATE TABLE tbbodega (
  
 idbodega  integer   not null     primary key    
,   
 bodega  varchar( 100)   not null    
,   
 estado  integer  
  );
"""
	heap.append(t33)
	F3D.ejecutarSQL()

	t34 = "CREATE INDEX id_index ON tbbodega (bodega);"
	heap.append(t34)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	stack.append("F9")
	goto .F8
	label .F9

	goto .END

	label .F1
	#**** Funcion *****

	# Parametros 
	p0

	# Retorno 
	global r0

	# Declaraciones 
	#Fin declaraciones


	print(" |>> " + str(p0)) 


	# Return
	r0 = p0
	goto .R


	goto .R


	label .F3
	#**** Funcion *****

	# Parametros 
	p1
	p2

	# Retorno 
	global r1

	# Declaraciones 
	t14 = 0
	t15 = 0
	#Fin declaraciones

	# ------ If ------- 
	t16 = p1 == "tbProducto"
	if t16: 
		goto .L0
	else: 
		goto .L1
	label .L0
	print("verdadero")

	t17 = """Select  * from tbProducto; 
"""
	heap.append(t17)
	F3D.ejecutarSQL()
	t14 = 8

	# ------ If ------- 
	t18 = p2 == t14
	if t18: 
		goto .L3
	else: 
		goto .L4
	label .L3
	print("verdadero")
	t15 = 1


	print(" |>> " + str(t15)) 
	goto .L5

	label .L4
	print("falso")
	t15 = 0


	print(" |>> " + str(t15)) 
	label .L5
	goto .L2

	label .L1
	label .L2
	# ------ If ------- 
	t19 = p1 == "tbProductoUp"
	if t19: 
		goto .L6
	else: 
		goto .L7
	label .L6
	print("verdadero")

	t20 = """Select  * from tbProductoUp; 
"""
	heap.append(t20)
	F3D.ejecutarSQL()
	t14 = 2

	# ------ If ------- 
	t21 = p2 == t14
	if t21: 
		goto .L9
	else: 
		goto .L10
	label .L9
	print("verdadero")
	t15 = 11


	print(" |>> " + str(t15)) 
	goto .L11

	label .L10
	print("falso")
	t15 = 0


	print(" |>> " + str(t15)) 
	label .L11
	goto .L8

	label .L7
	label .L8
	# ------ If ------- 
	t22 = p1 == "tbbodega"
	if t22: 
		goto .L12
	else: 
		goto .L13
	label .L12
	print("verdadero")

	t23 = """Select  * from tbbodega; 
"""
	heap.append(t23)
	F3D.ejecutarSQL()
	t14 = 6

	# ------ If ------- 
	t24 = p2 == t14
	if t24: 
		goto .L15
	else: 
		goto .L16
	label .L15
	print("verdadero")
	t15 = 111


	print(" |>> " + str(t15)) 
	goto .L17

	label .L16
	print("falso")
	t15 = 0


	print(" |>> " + str(t15)) 
	label .L17
	goto .L14

	label .L13
	label .L14


	# Return
	r1 = t15
	goto .R


	goto .R


	label .F6
	#**** Funcion *****

	# Parametros 

	# Retorno 
	global r2

	# Declaraciones 
	t27 = 0
	t28 = 0
	t29 = 0
	t30 = 0
	#Fin declaraciones

	# ------ If ------- 
	t31 = t29 > 1
	if t31: 
		goto .L18
	else: 
		goto .L19
	label .L18
	print("verdadero")
	t29 = 20


	print(" |>> " + str(t29)) 
	goto .L20

	label .L19
	print("falso")
	t29 = 10


	print(" |>> " + str(t29)) 
	label .L20


	# Return
	r2 = t29
	goto .R


	goto .R


	label .F8
	#**** Procedimiento *****

	# Parametros 

	# Retorno 
	global r3

	# Declaraciones 
	#Fin declaraciones


	t35 = """ INSERT INTO   tbbodega  values(  1,  "BODEGA CENTRAL",  1   );"""
	heap.append(t35)
	F3D.ejecutarSQL()

	t36 = """ INSERT INTO   tbbodega  values(  2,  "BODEGA ZONA 12",  1   );"""
	heap.append(t36)
	F3D.ejecutarSQL()

	t37 = """ INSERT INTO   tbbodega  values(  3,  "BODEGA ZONA 11",  1   );"""
	heap.append(t37)
	F3D.ejecutarSQL()

	t38 = """ INSERT INTO   tbbodega  values(  4,  "BODEGA ZONA 1",  1   );"""
	heap.append(t38)
	F3D.ejecutarSQL()

	t39 = """ INSERT INTO   tbbodega  values(  5,  "BODEGA ZONA 10",  1   );"""
	heap.append(t39)
	F3D.ejecutarSQL()

	goto .R


	label .R
	u = stack.pop()
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2
	if u == "F3": 
		goto .F3
	if u == "F4": 
		goto .F4
	if u == "F5": 
		goto .F5
	if u == "F6": 
		goto .F6
	if u == "F7": 
		goto .F7
	if u == "F8": 
		goto .F8
	if u == "F9": 
		goto .F9

	label .END
