from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack


	goto .END

	label .F1
	#**** Funcion *****

	# Parametros 
	p0

	# Retorno 
	global r0

	# Declaraciones 
	t0 = 0
	#Fin declaraciones

	t1 = t0 + 5
	t0 = t1


	t2 = """ DELETE  From tbbodega WHERE idbodega == 4;  """
	heap.append(t2)
	F3D.ejecutarSQL()

	goto .R


	label .F2
	#**** Funcion *****

	# Parametros 
	p0

	# Retorno 
	global r1

	# Declaraciones 
	t0 = 0
	#Fin declaraciones

	t1 = t0 + 5
	t0 = t1


	t2 = """ DELETE  From tbbodega WHERE idbodega == 4;  """
	heap.append(t2)
	F3D.ejecutarSQL()

	goto .R


	label .F3
	#**** Funcion *****

	# Parametros 
	p0

	# Retorno 
	global r2

	# Declaraciones 
	t0 = 0
	#Fin declaraciones

	t1 = t0 + 5
	t0 = t1


	t2 = """ UPDATE  tbbodega  SET   bodega == "bodega zona 9"  WHERE  idbodega == 4; """
	heap.append(t2)
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

	label .END
