class Instruccion:
    'Es una clase abstracta'

# Un drop table esta compuesto por el ID de la tabla que eliminara.
class DropTable(Instruccion):
    def __init__(self, id):
        self.id = id
