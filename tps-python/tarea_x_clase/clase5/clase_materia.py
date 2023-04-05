class Materia:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.notas = {1:None, 2:None} #1: primer semestre, 2: segundo semestre
    
    def set_nota(self, semestre:int, nota:int):
        error = ''
        if isinstance(nota, int):
            if 0 <= nota <= 10:
                if semestre == 1:
                    self.notas[1] = nota
                elif semestre == 2:
                    self.notas[2] = nota
                else:
                    error = 'Semestre inválido'
            else:
                error = 'Nota fuera de rango'
        else:
            error = 'Nota debe ser un entero'
        return error
    

    def get_nombre(self):
        return self.nombre

    def get_notas(self):
        return self.notas
