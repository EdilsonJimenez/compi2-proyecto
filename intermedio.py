from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	p0="oscar"
	p1="mazariegos"
	stack.append("F2")

	goto .F1
	label .F2goto .END
	label .F1

	# Parametros 
	p0
	p1

	# Retorno 
	p2

	# declaraciones 
	t0= 963 + 1
	t1 = t0
	# --------- IF --------------- 
	t2= p0 == p1
	if t2: 
		goto .L0
	else : 
		goto .L1
	label . L0
	# ~verdadero~
	goto .L2

	label .L1
	label .L2

	goto .R


	label .R
	u = stack[-1]
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2
	label .END

	main() 
