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
p0
p1

# Retorno 
p2

# declaraciones 
t0= 963 + 1
t1=t0
--------- IF --------------- 
t2= "abc" + 123
t3= t2 > "bc"
if t3: 
	goto .L0
else : 
	goto .L1
label . L0
     ~verdadero~
goto .L2

label .L1
label .L2

goto .R


p0=9
p1=1
stack.append("F2")

goto .F1
label .F2
label .R
u = stack[-1]
if u == "F1": 
	goto .F1
if u == "F2": 
	goto .F2


main() 
