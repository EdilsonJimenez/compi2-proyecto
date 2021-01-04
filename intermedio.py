from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	t0 = """ INSERT INTO   tbcalifica  values(  2,  "Funciones ELSEEEE",  2.0   ); 
"""
	heap.append(t0)
	F3D.ejecutarSQL()


	goto .END

	label .R
	u = stack.pop()

	label .END
