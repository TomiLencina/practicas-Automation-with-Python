class Alumno:
    def __init__(self, nombre:str, apellido:str, legajo:str):
        
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo        
        self.libreta = None #Asignar un objeto Libreta
    
    def set_nota(self, nombre_materia:str, semestre:int, nota:int):
        """
        Params
            nota: diccionario con estructura
                {semestre:nota}
                ejemplo:
                {1:6}
        """      
        self.libreta.set_nota(nombre_materia, semestre, nota)
    
    def set_libreta(self, libreta):
        self.libreta = libreta

    def get_nombre(self):
        return self.nombre
    
    def get_legajo(self):
        return self.legajo
    
    def get_notas(self, nombre_materia):
        return self.libreta.get_notas(nombre_materia)
    
    def get_promedio(self):
        #ToDo
        pass

    def get_materias(self):
        return(self.libreta.get_materias())
    
    def print_libreta(self):
        pass
