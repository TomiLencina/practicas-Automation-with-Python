'''
15.	Escriba un programa que muestre (por filas) la Tabla ASCII, 
empezando con el código 33 y terminando con el 127, 
Tal como se muestra en la siguiente imagen.
'''
CODIGO_INI = 33
CODIGO_FIN = 127
NUM_COLUMNAS = 5

tabla = ''

for codigo in range(CODIGO_INI, CODIGO_FIN + 1):
    
    tabla += f' {codigo:03d} {chr(codigo)} '

    if ((codigo - CODIGO_INI + 1) % NUM_COLUMNAS == 0):
        tabla += '\n'

print(tabla)