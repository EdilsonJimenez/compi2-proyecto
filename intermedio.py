from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack
	t0 = "CREATE DATABASE IF NOT EXISTS test OWNER = root MODE = 1;"
	heap.append(t0)
	F3D.ejecutarSQL()
	t1 = "USE test;"
	heap.append(t1)
	F3D.ejecutarSQL()

	p0=4
	p1=1
	stack.append("F2")

	goto .F1
	label .F2

	goto .END

	label .F1

	#**** Funcion *****



	# Declaraciones
	t2 = 24
	t3 = 25
	#--------- CASE BUSCADO ---------------
	# --------- IF ---------------
	t4= p0 == 1
	if t4:
		goto .L0
	else :
		goto .L1
	label .L0
	# ~verdadero~
	#--------- CASE SIMPLE ---------------
	# --------- IF ---------------
	t5= t2 == 12
	if t5:
		goto .L3
	else :
		goto .L4
	label .L3
	# ~verdadero~

	t3=12
	goto .L5

	label .L4
	# ~falso~

	t3=24
	label .L5
	goto .L2

	label .L1
	# ~falso~
	# --------- IF ---------------
	t6= p0 == 2
	if t6:
		goto .L6
	else :
		goto .L7
	label .L6
	# ~verdadero~
	#--------- CASE SIMPLE ---------------
	# --------- IF ---------------
	t7= t2 == 4
	if t7:
		goto .L9
	else :
		goto .L10
	label .L9
	# ~verdadero~

	t3=32
	goto .L11

	label .L10
	# ~falso~

	t2=11
	label .L11
	goto .L8

	label .L7
	# ~falso~
	# --------- IF ---------------
	t8= p0 == 4
	if t8:
		goto .L12
	else :
		goto .L13
	label .L12
	# ~verdadero~
	#--------- CASE SIMPLE ---------------
	# --------- IF ---------------
	t9= t2 == 4
	if t9:
		goto .L15
	else :
		goto .L16
	label .L15
	# ~verdadero~

	t3=32
	goto .L17

	label .L16
	# ~falso~

	t2=800
	label .L17
	goto .L14

	label .L13
	# ~falso~

	t2=100
	label .L14
	label .L8
	label .L2
	#--------- CASE BUSCADO ---------------
	# --------- IF ---------------
	t10= p0 == 1
	if t10:
		goto .L18
	else :
		goto .L19
	label .L18
	# ~verdadero~
	#--------- CASE SIMPLE ---------------
	# --------- IF ---------------
	t11= t2 == 12
	if t11:
		goto .L21
	else :
		goto .L22
	label .L21
	# ~verdadero~

	t3=12
	goto .L23

	label .L22
	# ~falso~

	t3=24
	label .L23
	goto .L20

	label .L19
	# ~falso~
	# --------- IF ---------------
	t12= p0 == 2
	if t12:
		goto .L24
	else :
		goto .L25
	label .L24
	# ~verdadero~
	#--------- CASE SIMPLE ---------------
	# --------- IF ---------------
	t13= t2 == 4
	if t13:
		goto .L27
	else :
		goto .L28
	label .L27
	# ~verdadero~

	t3=32
	goto .L29

	label .L28
	# ~falso~
	# --------- IF ---------------
	t14= t2 == 5
	if t14:
		goto .L30
	else :
		goto .L31
	label .L30
	# ~verdadero~

	t3=32
	goto .L32

	label .L31
	# ~falso~

	t2=11
	label .L32
	label .L29
	goto .L26

	label .L25
	# ~falso~
	# --------- IF ---------------
	t15= p0 == 4
	if t15:
		goto .L33
	else :
		goto .L34
	label .L33
	# ~verdadero~
	#--------- CASE SIMPLE ---------------
	# --------- IF ---------------
	t16= t2 == 4
	if t16:
		goto .L36
	else :
		goto .L37
	label .L36
	# ~verdadero~

	t3=32
	goto .L38

	label .L37
	# ~falso~

	t2=9200
	label .L38
	goto .L35

	label .L34
	# ~falso~

	t2=100
	label .L35
	label .L26
	label .L20

	goto .R


	label .R
	u = stack[-1]
	if u == "F1":
		goto .F1
	if u == "F2":
		goto .F2

	label .END



