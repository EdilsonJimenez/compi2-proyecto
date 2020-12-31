from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack
	label .F1

	# Parametros

	# Retorno

	# declaraciones
	t0=24
	t1= 1 + 1
	if t1:
		goto .L0
	else :
		goto .L1
	label .L0

	goto .L2

	label .L1
	label .L2

	goto .R


	stack.append("F2")

	goto .F1
	label .F2
	label .R
	u = stack[-1]
	if u == "F1":
		goto .F1
	if u == "F2":
		goto .F2
