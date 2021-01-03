from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	t0 = """CREATE DATABASE IF NOT EXISTS califica OWNER = root MODE = 2;"""
	heap.append(t0)
	F3D.ejecutarSQL()

	t1 = """CREATE DATABASE IF NOT EXISTS test OWNER = root MODE = 1;"""
	heap.append(t1)
	F3D.ejecutarSQL()

	t2 = """USE test;"""
	heap.append(t2)
	F3D.ejecutarSQL()

	t3 = """
	 CREATE TABLE tbcalifica (
	  
	 iditem  integer   not null     primary key    
	,   
	 item  varchar( 150)   not null    
	,   
	 puntos  decimal   not null    
	,   
	 seccion  integer  
	  );
	"""
	heap.append(t3)
	F3D.ejecutarSQL()

	t4 = """
	 CREATE TABLE tbusuario (
	  
	 idusuario  integer   NOT NULL     primary key    
	,   
	 nombre  varchar( 50)  
	,   
	 apellido  varchar( 50)  
	,   
	 usuario  varchar( 15)   UNIQUE     NOT NULL    
	,   
	 password  varchar( 80)   NOT NULL    
	,   
	 fechacreacion  date  
	  );
	"""
	heap.append(t4)
	F3D.ejecutarSQL()

	t5 = """
	 CREATE TABLE tbroles (
	  
	 idrol  integer   NOT NULL     primary key    
	,   
	 rol  varchar( 15)  
	  );
	"""
	heap.append(t5)
	F3D.ejecutarSQL()

	t6 = """
	 CREATE TABLE tbrol (
	  
	 idrol  integer   NOT NULL     primary key    
	,   
	 rol  varchar( 15)  
	  );
	"""
	heap.append(t6)
	F3D.ejecutarSQL()

	t7 = """
	 CREATE TABLE tbrolxusuario (
	  
	 idrol  integer   NOT NULL    
	,   
	 idusuario  integer   NOT NULL    
	  );
	"""
	heap.append(t7)
	F3D.ejecutarSQL()

	t8 = """ALTER TABLE tbrolxusuario ADD CONSTRAINT FK_rol FOREIGN KEY (idrol) REFERENCES tbrol (idrol);"""
	heap.append(t8)
	F3D.ejecutarSQL()

	t9 = """ALTER TABLE tbrolxusuario ADD CONSTRAINT FK_usuario FOREIGN KEY (idusuario) REFERENCES tbusuario (idusuario);"""
	heap.append(t9)
	F3D.ejecutarSQL()

	t10 = """ALTER TABLE tbcalifica ADD COLUMN seccion integer;"""
	heap.append(t10)
	F3D.ejecutarSQL()

	t11 = """ALTER TABLE tbusuario ALTER COLUMN password TYPE varchar(80);"""
	heap.append(t11)
	F3D.ejecutarSQL()

	t12 = """
	 CREATE TABLE tbcalifica2 (
	  
	 iditem  integer   not null     primary key    
	,   
	 item  varchar( 150)   not null    
	,   
	 puntos  decimal   not null    
	  );
	"""
	heap.append(t12)
	F3D.ejecutarSQL()

	t13 = """
	 CREATE TABLE tbestado (
	  
	 idestado  integer   not null     PRIMARY KEY    
	,   
	 estado  varchar( 30)  
	  );
	"""
	heap.append(t13)
	F3D.ejecutarSQL()

	t14 = """
	 CREATE TABLE tbempleado (
	  
	 idempleado  integer   not null     UNIQUE     PRIMARY KEY    
	,   
	 primernombre  varchar( 50)   not null    
	,   
	 segundonombre  varchar( 50)  
	,   
	 primerapellido  varchar( 50)   not null    
	,   
	 segundoapellido  varchar( 50)  
	,   
	 fechadenacimiento  DATE  
	,   
	 fechacontratacion  DATE  
	,   
	 idestado  integer  
	  );
	"""
	heap.append(t14)
	F3D.ejecutarSQL()

	t15 = """ALTER TABLE tbempleado ADD CONSTRAINT FK_estado FOREIGN KEY (idestado) REFERENCES tbestado (idestado);"""
	heap.append(t15)
	F3D.ejecutarSQL()

	t16 = """
	 CREATE TABLE cities (
	  
	 name  text  
	,   
	 population  float  
	,   
	 elevation  int  
	  );
	"""
	heap.append(t16)
	F3D.ejecutarSQL()

	t17 = """
	 CREATE TABLE capitals (
	  
	 state  char  2  
	 INHERITScities 
	  );
	"""
	heap.append(t17)
	F3D.ejecutarSQL()

	t18 = """
	 CREATE TABLE tbempleadoidentificacion (
	  
	 idempleado  integer   not null     primary key    
	,   
	 identificacion  varchar( 25)   not null    
	,   
	 ididentificaciontipo  integer  
	  );
	"""
	heap.append(t18)
	F3D.ejecutarSQL()

	t19 = """
	 CREATE TABLE tbidentificaciontipo (
	  
	 ididentificaciontipo  integer   not null     primary key    
	,   
	 tipoidentificacion  varchar( 20)  
	  );
	"""
	heap.append(t19)
	F3D.ejecutarSQL()

	t20 = """ALTER TABLE tbempleadoidentificacion ADD CONSTRAINT FK_identificaciontipo FOREIGN KEY (ididentificaciontipo) REFERENCES tbidentificaciontipo (ididentificaciontipo);"""
	heap.append(t20)
	F3D.ejecutarSQL()

	t21 = """
	 CREATE TABLE tbpuesto (
	  
	 idpuesto  smallint   not null    
	,   
	 puesto  character  25  
	,   
	 salariobase  money  
	,   primary key    idpuesto   ,   
	 tinecomision  boolean  
	  );
	"""
	heap.append(t21)
	F3D.ejecutarSQL()

	t22 = """ALTER TABLE tbpuesto ADD COLUMN tinecomision boolean;"""
	heap.append(t22)
	F3D.ejecutarSQL()

	t23 = """
	 CREATE TABLE tbempleadopuesto (
	  
	 idempleado  integer   not null    
	,   
	 idpuesto  integer   not null    
	,   
	 departamento  varchar( 50)  
	  );
	"""
	heap.append(t23)
	F3D.ejecutarSQL()

	t24 = """ALTER TABLE tbempleadopuesto ADD CONSTRAINT FK_empleado FOREIGN KEY (idempleado) REFERENCES tbempleado (idempleado);"""
	heap.append(t24)
	F3D.ejecutarSQL()

	t25 = """ALTER TABLE tbempleadopuesto ADD CONSTRAINT FK_empleado FOREIGN KEY (idempleado) REFERENCES tbempleado (idempleado);"""
	heap.append(t25)
	F3D.ejecutarSQL()

	t26 = """
	 CREATE TABLE tbventa (
	  
	 idventa  integer   not null     primary key    
	,   
	 idempleado  integer  
	,   
	 fechaventa  date   validaventa No viene check    
	,   
	 montoventa  money   ventavalida No viene check    
	,   
	 ventaregistrada  boolean  
	,   
	 descripcion  text  
	  );
	"""
	heap.append(t26)
	F3D.ejecutarSQL()

	t27 = """
	 CREATE TABLE tblibrosalario (
	  
	 idempleado  integer   not null    
	,   
	 aniocalculo  integer   not null     aniosalario No viene check    
	,   
	 mescalculo  integer   not null     mescalculo No viene check    
	,   
	 salariobase  money   not null    
	,   
	 comision  decimal  
	,   primary key    idempleado     );
	"""
	heap.append(t27)
	F3D.ejecutarSQL()

	t28 = """
	 CREATE TABLE tblibrosalariohis (
	  
	 idhistorico  integer   not null     primary key    
	 INHERITStblibrosalario 
	  );
	"""
	heap.append(t28)
	F3D.ejecutarSQL()

	t29 = """
	 CREATE TABLE tbfuncionesmath (
	  
	 idfuncion  int   not null     primary key    
	,   
	 seno  decimal  
	,   
	 coseno  decimal  
	  );
	"""
	heap.append(t29)
	F3D.ejecutarSQL()


	goto .END

	label .R
	u = stack[-1]

	label .END



	#Llamada a funcion o procedimiento.
	stack.append("F2")

	label .F2

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
	t2 = 15
	t3 = 0
	t4 = 15
	t5 = 0
	t6 = 15
	t7 = 0
	t8 = 15
	t9 = 0
	#Fin declaraciones

	t10 = t1 + 0
	t1 = t10

	t11 = t2 - 0
	t2 = t11

	t12 = t3 * 1
	t3 = t12

	t13 = t4 / 1
	t4 = t13

	t14 = t9 + 0
	t5 = t14

	t15 = t9 - 0
	t6 = t15

	t16 = t9 * 1
	t7 = t16

	t17 = t9 / 1
	t8 = t17

	# ------ If ------- 
	t18 = 100 == 100
	if t18: 
		goto .L0
	else: 
		goto .L1
	label .L0
	print("verdadero")
	t0 = 111

	goto .L2

	label .L1
	label .L2


	# Return
	r0 = t0
	goto .R


	goto .R


	label .R
	u = stack.pop()
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2

	label .END
