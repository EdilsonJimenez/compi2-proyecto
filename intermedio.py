from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack
#Llamada a funcion o procedimiento.
p1="abc"
p2="apell"
stack.append("F4")

goto .F2
label .F4

goto .END

label .F1
#**** Funcion *****

# Parametros 
p0

# Retorno 
global r0

# Declaraciones 
t0 = 15
t1 = 0
t2= 1 + 0

t1=t2
# --------- IF --------------- 
t3= 100 == 100
if t3: 
	goto .L0
else : 
	goto .L1
label .L0
print("verdadero")

t0=111
goto .L2

label .L1
label .L2
# --------- IF --------------- 
t4= 90 == 100
if t4: 
	goto .L3
else : 
	goto .L4
label .L3
print("verdadero")

t0=111
goto .L5

label .L4
label .L5


# Return
r0 = t0
goto .R


goto .R


label .F2
#**** Procedimiento *****

# Parametros 
p1
p2

# Retorno 
global r1

# Declaraciones 
t5 = 10
t6 = 20
#Llamada a funcion o procedimiento.
p0=100
stack.append("F3")

goto .F1
label .F3
t6=r0

goto .R


label .R
u = stack.pop()
if u == "F1": 
	goto .F1
if u == "F2": 
	goto .F2
if u == "F3": 
	goto .F3
if u == "F4": 
	goto .F4

label .END


main() 
