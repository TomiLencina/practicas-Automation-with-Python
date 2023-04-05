"""Se tienen los siguientes datos de los alumnos:
• Nombre y Apellido
• Legajo"""


class Alumno:
    def __init__(self,nombre,apellido,legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo

    def agregar_alumno(self,nomb,apellido,legajo):
        pass    

    def mostrar_alumnos(self):
        pass
    

alumno1 = Alumno("Tomas","Lencina",1)    
print(alumno1.nombre)
"""Se tienen los siguientes datos de los maestros
• Nombre y Apellido
• Legajo
• Conjunto de Materias que dicta"""



class Maestro:
    def __init__(self,nombre,apellido,legajo,materias):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.materias = materias


"""La Libreta tiene los siguientes datos:
• El grado al que corresponde
• El listado de Materias de ese grado
• Cada Materia tiene una nota en el primer semestre y otra en el segundo semestre
• Hay un promedio por materia
• Hay un promedio general con las notas cargadas hasta el momento."""

class Libreta:
    def __init__(self,grado):
        self.grado = grado
    
    def materias_por_grados(self,grado):
        pass

    def ver_notas_semestres():
        pass
    def cargar_notas_semestres():        
        pass
    def promedio_por_materia():
        pass
    def promedio_general():
        pass


"""De cada Materia se conoce:
• Nombre
• Maestro/a"""


class Materia:
    def __init__(self,nombreM,maestro):
        self.nombreM = nombreM
        self.maestro = maestro

"""Cada grado consiste en:
• Un maestro
• Grupo de Alumnos
• Conjunto de Materias"""

class Grado(Alumno,Materia):
    pass



