#Import
from clase_alumno import Alumno
from clase_libreta import Libreta
from clase_materia import Materia
from clase_grado import Grado
from clase_institucion import Institucion

from datos import *

#********
# Main
#********
def run():
    print("Escuela")

    #Genero diccionario de las Materias de cada Grado
    dic_grado_materias = {}
    """
    {
        1: [materia1, materia2,]
        2: []
    }
    """
    for id, materia in dic_datos_materias.items():
        
        grado = materia[KEY_GRADO]
        nombre = materia[KEY_MATERIA]

        #Creo objeto Materia
        materia = Materia(nombre)
        
        if grado not in dic_grado_materias.keys():
            dic_grado_materias[grado] = []

        #Agrego la materia al grado
        dic_grado_materias[grado].append(materia)


    #Crear un diccionario de Alumnos, indexados por legajo
    dic_alumnos = {}
    """
    {
        '10': alumno,
        '20': alumno,
        '30': alumno
    }
    """
    for legajo, alumno in dic_datos_alumnos.items():
        
        nombre = alumno[KEY_NOMBRE]
        apellido = alumno[KEY_APELLIDO]
        grado = alumno[KEY_GRADO]

        # Creo objeto Alumno
        alumno = Alumno(nombre, apellido, legajo)

        #Creo objeto Libreta
        libreta = Libreta(grado)

        #Cargo las materias en la libreta
        libreta.set_materias(dic_grado_materias[grado])

        #Asigno la libreta al alumno
        alumno.set_libreta(libreta)

        #Agrego el alumno al diccionario
        dic_alumnos[legajo] = alumno
    
    #Prueba, imprimir los nombres
    print(f'Listado de Alumnos')
    print(f'{[alumno.get_nombre() for alumno in dic_alumnos.values()]}')

    #Probar Setear las notas de un alumno
    legajo = '110'
    materia = 'Arte'
    #Consulta por el legajo en el diccionario de alumnos, si no está, devuelve None
    
    #if legajo in dic_alumnos.keys():
    #    alumno = dic_alumnos[legajo]
    #else:
    #    alumno = None
    
    alumno = dic_alumnos.get(legajo, None)
    
    if alumno != None:
        alumno.set_nota(materia, 1, 10)
        alumno.set_nota(materia, 2, 9)
        print(f'\nPrueba carga de notas\n'
            f'Alumno/a: {alumno.get_nombre()}, '
            f'Materia: {materia}, Notas: {alumno.get_notas(materia)}'
        )
        print(f'{alumno.get_materias()}')
    else:
        print(f'Legajo {legajo} inexistente!')

if __name__ == "__main__":
    run()
