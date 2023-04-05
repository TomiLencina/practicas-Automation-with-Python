class Libreta:
    def __init__(self, grado:int):
        self.grado = grado
        self.materias = [] #Lista de objetos Materia
        self.promedios = {}
    
    def set_nota(self, nombre_materia:str, semestre:int, nota:int):
        error = ''
        for materia in self.materias:
            if nombre_materia == materia.get_nombre():
                error = materia.set_nota(semestre, nota)
                break
        else:
            error = 'Materia no encontrada'        
        return error
    
    def set_materias(self, materias:list):
        if isinstance(materias, list):
            self.materias = materias
        else:
            self.materias = []

    def get_materias(self):
        return self.materias
    
    def get_nom_materias(self):
        return [materia.get_nombre() for materia in self.materias]
    
    def get_notas(self, nombre_materia:str):
        for materia in self.materias:
            if materia.get_nombre() == nombre_materia:
                notas = materia.get_notas()
                break
        else:
            #Materia no encontrada
            notas = {1:None, 2:None}
        return notas
    
    def get_materias(self):
        materias = [materia.get_nombre() for materia in self.materias]
        return materias
    