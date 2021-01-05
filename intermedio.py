from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []
t0 = None

@with_goto 
def main(): 
	global heap
	global stack
	global r0
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



	heap.append(56)
	t6 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t6)
	heap.append("Laptop Lenovo")
	heap.append(1)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t6 = F3D.funcionNativa()

	heap.append(56)
	t7 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t7)
	heap.append("Bateria para Laptop Lenovo T420")
	heap.append(2)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t6 = F3D.funcionNativa()

	heap.append(56)
	t7 = F3D.funcionNativa()

	heap.append(56)
	t8 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t8)
	heap.append("Teclado Inalambrico")
	heap.append(3)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t6 = F3D.funcionNativa()

	heap.append(56)
	t7 = F3D.funcionNativa()

	heap.append(56)
	t8 = F3D.funcionNativa()

	heap.append(56)
	t9 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t9)
	heap.append("Mouse Inalambrico")
	heap.append(4)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t6 = F3D.funcionNativa()

	heap.append(56)
	t7 = F3D.funcionNativa()

	heap.append(56)
	t8 = F3D.funcionNativa()

	heap.append(56)
	t9 = F3D.funcionNativa()

	heap.append(56)
	t10 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t10)
	heap.append("WIFI USB")
	heap.append(5)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t6 = F3D.funcionNativa()

	heap.append(56)
	t7 = F3D.funcionNativa()

	heap.append(56)
	t8 = F3D.funcionNativa()

	heap.append(56)
	t9 = F3D.funcionNativa()

	heap.append(56)
	t10 = F3D.funcionNativa()

	heap.append(56)
	t11 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t11)
	heap.append("Laptop HP")
	heap.append(6)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t6 = F3D.funcionNativa()

	heap.append(56)
	t7 = F3D.funcionNativa()

	heap.append(56)
	t8 = F3D.funcionNativa()

	heap.append(56)
	t9 = F3D.funcionNativa()

	heap.append(56)
	t10 = F3D.funcionNativa()

	heap.append(56)
	t11 = F3D.funcionNativa()

	heap.append(56)
	t12 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t12)
	heap.append("Teclado Flexible USB")
	heap.append(7)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()



	heap.append(1)
	heap.append("2021-01-02")
	heap.append("Laptop Samsung")
	heap.append(8)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	#Llamada a funcion o procedimiento.
	p0="tbProducto"
	p1=8
	stack.append("F2")
	goto .F1
	label .F2
	t24 = r0

	heap.append(t24)
	heap.append("Create Table and Insert")
	heap.append(1)
	heap.append(3)
	heap.append('tbCalificacion')
	F3D.insert()


	heap.append(1)
	heap.append("Create Table and Insert")
	heap.append(1)
	heap.append(3)
	heap.append('tbCalificacion')
	F3D.insert()

	goto .END

	label .F1
	#**** Funcion *****

	# Parametros 
	p0
	p1

	# Retorno 


	# Declaraciones 
	t13 = 0
	t14 = 0
	#Fin declaraciones

	# ------ If ------- 
	t15 = p0 == "tbProducto"
	if t15: 
		goto .L0
	else: 
		goto .L1
	label .L0
	print("verdadero")

	t16 = """Select  * from tbProducto; 
"""
	heap.append(t16)
	F3D.ejecutarSQL()
	t13 = 8

	# ------ If ------- 
	t17 = p1 == t13
	if t17: 
		goto .L3
	else: 
		goto .L4
	label .L3
	print("verdadero")
	t14 = 1


	print(" |>> " + str(t14)) 
	goto .L5

	label .L4
	print("falso")
	t14 = 0


	print(" |>> " + str(t14)) 
	label .L5
	goto .L2

	label .L1
	label .L2
	# ------ If ------- 
	t18 = p0 == "tbProductoUp"
	if t18: 
		goto .L6
	else: 
		goto .L7
	label .L6
	print("verdadero")

	t19 = """Select  * from tbProductoUp; 
"""
	heap.append(t19)
	F3D.ejecutarSQL()
	t13 = 2

	# ------ If ------- 
	t20 = p1 == t13
	if t20: 
		goto .L9
	else: 
		goto .L10
	label .L9
	print("verdadero")
	t14 = 11


	print(" |>> " + str(t14)) 
	goto .L11

	label .L10
	print("falso")
	t14 = 0


	print(" |>> " + str(t14)) 
	label .L11
	goto .L8

	label .L7
	label .L8
	# ------ If ------- 
	t21 = p0 == "tbbodega"
	if t21: 
		goto .L12
	else: 
		goto .L13
	label .L12
	print("verdadero")

	t22 = """Select  * from tbbodega; 
"""
	heap.append(t22)
	F3D.ejecutarSQL()
	t13 = 6

	# ------ If ------- 
	t23 = p1 == t13
	if t23: 
		goto .L15
	else: 
		goto .L16
	label .L15
	print("verdadero")
	t14 = 111


	print(" |>> " + str(t14)) 
	goto .L17

	label .L16
	print("falso")
	t14 = 0


	print(" |>> " + str(t14)) 
	label .L17
	goto .L14

	label .L13
	label .L14


	# Return
	r0 = t14
	goto .R


	goto .R


	label .F3
	#**** Procedimiento *****

	# Parametros 

	# Retorno 
	global r1

	# Declaraciones 
	t10 = 0
	#Fin declaraciones


	t11 = """ UPDATE  tbbodega  SET   bodega = "bodega zona 9"  WHERE  idbodega = 3; """
	heap.append(t11)
	F3D.ejecutarSQL()

	print(" |>> " + str(t10)) 

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

	label .END
