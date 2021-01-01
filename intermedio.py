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
global p1

# Declaraciones 
 t0 = 15
# --------- IF --------------- 
t1=  > 5
if t1: 
	goto .L0
else : 
	goto .L1
label . L0
# ~verdadero~

=
goto .L2

label .L1
label .L2
 # return 

p1 = t0

goto .R


	t0=11
	label .L11
	goto .L8

	label .L7
	# ~falso~
	# --------- IF ---------------
	t6= p0 == 4
	if t6:
		goto .L12
	else :
		goto .L13
	label .L12
	# ~verdadero~
	#--------- CASE SIMPLE ---------------
	# --------- IF ---------------
	t7= t0 == 4
	if t7:
		goto .L15
	else :
		goto .L16
	label .L15
	# ~verdadero~

label .R
u = stack[-1]
if u == "F1": 
	goto .F1

	label .END
	print("ESTE ES T0 =" + str(t0))
	print("ESTE ES T1 =" + str(t1))


main() 
