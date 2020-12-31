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
label .F2

 goto .END

label .F1

#**** Funcion *****

# Parametros 
p0
p1

# Retorno 
p2

# Declaraciones 
t0= 1 / 6
t1= 963 + t0
t2 = t1
# --------- IF --------------- 
t3= p0 == p1
t4= p0 == "abc"
t5= t3 and t4
if t5: 
	goto .L0
else : 
	goto .L1
label . L0
# ~verdadero~
goto .L2

label .L1
label .L2

t6= 9 + 6

p0=t6
 # return 

p2 = p0

goto .R


label .R
u = stack[-1]
if u == "F1": 
	goto .F1
if u == "F2": 
	goto .F2

label .END


main() 
