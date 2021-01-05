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
	t46 = """ INSERT INTO   tbCalificacion  values(  3,  " Valida Funciones",  10   );"""
	heap.append(t46)
	F3D.ejecutarSQL()

	t47 = """
 CREATE TABLE tbbodega (
  
 idbodega  integer   not null     primary key    
,   
 bodega  varchar( 100)   not null    
,   
 estado  integer  
  );
"""
	heap.append(t47)
	F3D.ejecutarSQL()

	t48 = "CREATE INDEX index_bodega ON tbbodega (bodega);"
	heap.append(t48)
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



	heap.append("2001-02-16 20:38:40")
	heap.append("HOUR")

	heap.append(57)
	t31 = F3D.funcionNativa()
	t27 = t31


	heap.append(1)

	heap.append(35)
	t32 = F3D.funcionNativa()
	t28 = t32

	t33 = t28 * t27
	t33 = t28 * t27


	heap.append(1)
	heap.append(t33)

	heap.append(21)
	t34 = F3D.funcionNativa()
	t29 = t34




	heap.append(4)
	heap.append(1)
	heap.append("FASE2")

	heap.append(46)
	t35 = F3D.funcionNativa()



	heap.append(4)
	heap.append(1)
	heap.append("FASE2")

	heap.append(46)
	t35 = F3D.funcionNativa()

	heap.append(t35)

	heap.append(45)
	t36 = F3D.funcionNativa()
	t37 = t29 + t36
	t29 = t37


	heap.append(-1)

	heap.append(39)
	t38 = F3D.funcionNativa()

	heap.append(-1)

	heap.append(39)
	t38 = F3D.funcionNativa()

	heap.append(t38)

	heap.append(1)
	t39 = F3D.funcionNativa()
	t30 = t39


	heap.append(225)

	heap.append(19)
	t40 = F3D.funcionNativa()
	t41 = t30 * t40
	t30 = t41

	t42 = t29 + t30

	heap.append(0.5)

	heap.append(24)
	t43 = F3D.funcionNativa()
	t44 = t42 / t43
	t29 = t44

	# ------ If ------- 
	t45 = t29 > 1
	if t45: 
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

	label .END
