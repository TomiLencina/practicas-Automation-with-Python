import collections

def contar_frecuencias(cadena):
    palabras = cadena.split()
    frecuencias = collections.Counter(palabras)
    return frecuencias

def obtener_palabra_mas_repetida(frecuencias):
    palabra, frecuencia = frecuencias.most_common(1)[0]
    return palabra, frecuencia

cadena = "Esta es una cadena de ejemplo para contar las frecuencias de las palabras"
frecuencias = contar_frecuencias(cadena)
print(frecuencias)

palabra_mas_repetida, frecuencia = obtener_palabra_mas_repetida(frecuencias)
print("La palabra mas repetida es: \n \t",palabra_mas_repetida, "\n", "La frecuencia con la que se repite es: \n \t", frecuencia)


#most_common([n])
"""Retorna una lista de los n elementos mas comunes y sus conteos, del mas común al menos común.
Si se omite n o None, most_common() retorna todos los elementos del contador. 
Los elementos con conteos iguales se ordenan en el orden en que se encontraron por primera vez"""

#Counter
"""Una clase Counter es una subclase dict para contar objetos hashables.
Es una colección donde los elementos se almacenan como llaves de diccionario y sus conteos
se almacenan como valores de diccionario.
Se permite que los conteos sean cualquier valor entero, incluidos los conteos de cero o negativos. 
La clase Counter es similar a los bags o multiconjuntos en otros idiomas."""