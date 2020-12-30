import FuncionesIntermedias as F3D
heap = F3D.heap

def main():
    global heap
    print('Ejecutando codigo de 3 direcciones')

    t0 = '''CREATE DATABASE IF NOT EXISTS BASE1
    OWNER = root
    MODE = 1;'''

    heap.append(t0)
    F3D.ejecutarSQL()





