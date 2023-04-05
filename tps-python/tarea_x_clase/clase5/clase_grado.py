class Grado:
    def __init__(self, numero:int):
        self.numero = numero
        self.alumnos = []
        self.materias = []
    
    def get_cant_alumnos(self, nombre_materia):
        pass


if __name__ == '__main__':
    grado = Grado(1)
    grado.get_cant_alumnos('Materia')