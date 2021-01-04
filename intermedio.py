from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	t0 = """CREATE DATABASE IF NOT EXISTS califica OWNER = root MODE = 2;"""
	heap.append(t0)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p1="abc"
	p2="apell"
	stack.append("F4")
	goto .F2
	label .F4

	goto .END

	label .F1
	#**** Funcion *****

	# Parametros 
	p0

	# Retorno 
	global r0

	# Declaraciones 
	t1 = 0
	#Fin declaraciones

	t1 = p0


	t2 = """
 CREATE TABLE tbcalifica (
  
 iditem  integer   not null     primary key    
,   
 item  varchar( 150)   not null    
,   
 puntos  decimal   not null    
  );
"""
	heap.append(t2)
	F3D.ejecutarSQL()
	# ------ If ------- 
	t3 = t1 > 2
	if t3: 
		goto .L0
	else: 
		goto .L1
	label .L0
	print("verdadero")

	t4 = """ INSERT INTO   tbcalifica  values(  1,  "Funcionalidades IFFFFF",  2.0   );"""
	heap.append(t4)
	F3D.ejecutarSQL()
	goto .L2

	label .L1
	print("falso")

	t5 = """ INSERT INTO   tbcalifica  values(  2,  "Funciones ELSEEEE",  2.0   );"""
	heap.append(t5)
	F3D.ejecutarSQL()
	label .L2


	# Return
	r0 = t1
	goto .R


	goto .R


	label .F2
	#**** Procedimiento *****

	# Parametros 
	p1
	p2

	# Retorno 
	global r1

	# Declaraciones 
	t6 = 10
	#Fin declaraciones


	#Llamada a funcion o procedimiento.
	p0=1
	stack.append("F3")
	goto .F1
	label .F3
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
