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
	global r0

	# Declaraciones
	t0 = 0
	#Fin declaraciones

	t1 = t0 + 5
	t0 = t1


	t2 = """ DELETE  From tbbodega WHERE idbodega == 4;  """
	heap.append(t2)
	F3D.ejecutarSQL()

	goto .R


	label .F2
	#**** Funcion *****

	# Parametros
	p0

	# Retorno
	global r1

	# Declaraciones
	t0 = 0
	#Fin declaraciones

	t1 = t0 + 5
	t0 = t1


	t2 = """ DELETE  From tbbodega WHERE idbodega == 4;  """
	heap.append(t2)
	F3D.ejecutarSQL()

	goto .R


	label .F3
	#**** Funcion *****

	# Parametros
	p0

	# Retorno
	global r2

	# Declaraciones
	t0 = 0
	#Fin declaraciones

	t1 = t0 + 5
	t0 = t1


	t2 = """ UPDATE  tbbodega  SET   bodega == "bodega zona 9"  WHERE  idbodega == 4; """
	heap.append(t2)
	F3D.ejecutarSQL()

	goto .R


	label .F3
	#**** Funcion *****

	# Parametros
	p1
	p2

	# Retorno
	global r1

	# Declaraciones
	t14 = 0
	t15 = 0
	#Fin declaraciones

	# ------ If -------
	t16 = p1 == "tbProducto"
	if t16:
		goto .L0
	else:
		goto .L1
	label .L0
	print("verdadero")

	t17 = """Select  * from tbProducto;
"""
	heap.append(t17)
	F3D.ejecutarSQL()
	t14 = 8

	# ------ If -------
	t18 = p2 == t14
	if t18:
		goto .L3
	else:
		goto .L4
	label .L3
	print("verdadero")
	t15 = 1


	print(" |>> " + str(t15))
	goto .L5

	label .L4
	print("falso")
	t15 = 0


	print(" |>> " + str(t15))
	label .L5
	goto .L2

	label .L1
	label .L2
	# ------ If -------
	t19 = p1 == "tbProductoUp"
	if t19:
		goto .L6
	else:
		goto .L7
	label .L6
	print("verdadero")

	t20 = """Select  * from tbProductoUp;
"""
	heap.append(t20)
	F3D.ejecutarSQL()
	t14 = 2

	# ------ If -------
	t21 = p2 == t14
	if t21:
		goto .L9
	else:
		goto .L10
	label .L9
	print("verdadero")
	t15 = 11


	print(" |>> " + str(t15))
	goto .L11

	label .L10
	print("falso")
	t15 = 0


	print(" |>> " + str(t15))
	label .L11
	goto .L8

	label .L7
	label .L8
	# ------ If -------
	t22 = p1 == "tbbodega"
	if t22:
		goto .L12
	else:
		goto .L13
	label .L12
	print("verdadero")

	t23 = """Select  * from tbbodega;
"""
	heap.append(t23)
	F3D.ejecutarSQL()
	t14 = 6

	# ------ If -------
	t24 = p2 == t14
	if t24:
		goto .L15
	else:
		goto .L16
	label .L15
	print("verdadero")
	t15 = 111


	print(" |>> " + str(t15))
	goto .L17

	label .L16
	print("falso")
	t15 = 0


	print(" |>> " + str(t15))
	label .L17
	goto .L14

	label .L13
	label .L14


	# Return
	r1 = t15
	goto .R


	goto .R


	label .F6
	#**** Funcion *****

	# Parametros

	# Retorno
	global r2

	# Declaraciones
	t27 = 0
	t28 = 0
	t29 = 0
	t30 = 0
	#Fin declaraciones

	# ------ If -------
	t31 = t29 > 1
	if t31:
		goto .L18
	else:
		goto .L19
	label .L18
	print("verdadero")
	t29 = 20


	print(" |>> " + str(t29))
	goto .L20

	label .L19
	print("falso")
	t29 = 10


	print(" |>> " + str(t29))
	label .L20


	# Return
	r2 = t29
	goto .R


	goto .R


	label .F8
	#**** Procedimiento *****

	# Parametros

	# Retorno
	global r3

	# Declaraciones
	#Fin declaraciones


	t35 = """ INSERT INTO   tbbodega  values(  1,  "BODEGA CENTRAL",  1   );"""
	heap.append(t35)
	F3D.ejecutarSQL()

	t36 = """ INSERT INTO   tbbodega  values(  2,  "BODEGA ZONA 12",  1   );"""
	heap.append(t36)
	F3D.ejecutarSQL()

	t37 = """ INSERT INTO   tbbodega  values(  3,  "BODEGA ZONA 11",  1   );"""
	heap.append(t37)
	F3D.ejecutarSQL()

	t38 = """ INSERT INTO   tbbodega  values(  4,  "BODEGA ZONA 1",  1   );"""
	heap.append(t38)
	F3D.ejecutarSQL()

	t39 = """ INSERT INTO   tbbodega  values(  5,  "BODEGA ZONA 10",  1   );"""
	heap.append(t39)
	F3D.ejecutarSQL()

	goto .R


	label .R
	u = stack.pop()
	if u == "F1":
		goto .F1
	if u == "F2":
		goto .F2
	if u == "F3":
		goto .F3

	label .END
