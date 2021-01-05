from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	t0 = """ DELETE  From tbbodega WHERE idbodega == 4;  """
	heap.append(t0)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	stack.append("F2")
	label .F2
	- = -
	heap.append('tbCalificacion')
	heap.append(-)
	heap.append("Valida Delete")
	heap.append(5)
	F3D.insert()
	t1 = """Select  * from tbbodega; 
"""
	heap.append(t1)
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


	label .R
	u = stack.pop()
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2

	label .END
