from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	p0=1
	p1=1
	stack.append("F2")

	goto .F1
	label .F2

	goto .END

	label .F1

	#**** Funcion *****


	# Declaraciones
	t0 = 24
	t1 = 25
	#--------- CASE BUSCADO ---------------
	# --------- IF ---------------
	t2= p0 == 1
	if t2:
		goto .L0
	else :
		goto .L1
	label . L0
	# ~verdadero~
	#--------- CASE SIMPLE ---------------
	# --------- IF ---------------
	t3= t0 == 12
	if t3:
		goto .L3
	else :
		goto .L4
	label . L3
	# ~verdadero~

	t1=12
	goto .L5

	label .L4
	# ~falso~

	t1=24
	label .L5
	goto .L2

	label .L1
	# ~falso~
	# --------- IF ---------------
	t4= p0 == 2
	if t4:
		goto .L6
	else :
		goto .L7
	label . L6
	# ~verdadero~
	#--------- CASE SIMPLE ---------------
	# --------- IF ---------------
	t5= t0 == 4
	if t5:
		goto .L9
	else :
		goto .L10
	label . L9
	# ~verdadero~

	t1=32
	goto .L11

	label .L10
	label .L11
	goto .L8

	label .L7
	# ~falso~

	t0=100
	label .L8
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
