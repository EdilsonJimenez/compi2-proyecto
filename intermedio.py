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


goto .R


label .R
u = stack[-1]
if u == "F1": 
	goto .F1

label .END


main() 
