diccionario ={
    'carpeta_N1':{
        'carpeta_N2a':{
            'archivo1': 'contenido1',
            'archivo2': 'contenido2',
            'carpeta_F1':{
                'archivo10': 'contenido10'
            }
        },
        'carpeta_N2b':{
            'archivo3':'contenido3',
            'carpeta_N3a':{
                'archivo4': 'contenido4'
            }
        },
        'archivo7': 1234
    },
    'archivo6': 'contenido6'
}

diccionario['carpeta_N1']['carpeta_N2b']['carpeta_N3a']['archivo4'] = 'contenido_nuevo'

print(diccionario['carpeta_N1']['carpeta_N2b']['carpeta_N3a']['archivo4'])

print(diccionario)


dic_datos_materias = {
    'Artes': {
        'grado': 1,
        'maestro': 'Augusto Gutierres',
        'legajo': 'M10'
    },
    'Matemática': {
        'grado': 1,
        'maestro': 'Cecilia Peña',
        'legajo': 'M20'
    },
    'Geografía': {
        'grado': 1,
        'maestro': 'Sandra Almada',
        'legajo': 'M30'
    },
    'Historia': {
        'grado': 3,
        'maestro': 'Augusto Gutierres',
        'legajo': 'M10'
    }
}

legajo = dic_datos_materias['Geografía']['legajo']

print(f'\nEl legajo del maestro de Geografia es {legajo}\n')

# Quiero generar otro diccionario con los nombres de los maestros y sus materias
"""
{
    'M10': {
        'materias': ['Historia', 'Artes']
    },
    'M20':{
        'materias': ['Matematica']
    }
}
"""

dic_maestros = {}

for materia in dic_datos_materias.keys():
    legajo = dic_datos_materias[materia]['legajo']
    nombre = dic_datos_materias[materia]['maestro']

    if legajo in dic_maestros.keys():
        dic_maestros[legajo]['materias'].append(materia)
    else:
        
        dic_maestros[legajo] = {
            'nombre': nombre,
            'materias': [materia]
        }



print(dic_maestros)






