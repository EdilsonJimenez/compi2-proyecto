from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	t0 = """CREATE DATABASE IF NOT EXISTS test OWNER = root MODE = 1;"""
	heap.append(t0)
	F3D.ejecutarSQL()

	t1 = """DROP DATABASE test;"""
	heap.append(t1)
	F3D.ejecutarSQL()

	t2 = """USE test;"""
	heap.append(t2)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p0=4
	p1=1
	stack.append("F2")
	goto .F1
	label .F2

	goto .END

	label .F1
	#**** Funcion *****

	# Parametros 
	p0
	p1

	# Retorno 
	global r0

	# Declaraciones 

	heap.append(14)
	t3 = F3D.funcionNativa()
	t4 = t3
	t5 = 25
	#Fin declaraciones


	goto .R


	label .R
	u = stack.pop()
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2

	label .END
