'''
12.	Escriba un programa que calcule la distancia hamming entre dos cadenas de texto de la misma longitud
Ejemplo

•	Entrada: 0001010011101 y 0000110010001
•	Salida: 4
'''

cadena1 = '0001010011101'
cadena2 = '0000110010001'

distancia_hamming = 0

idxs_diferentes = ''

for idx in range(len(cadena1)):
    if cadena1[idx] != cadena2[idx]:
        distancia_hamming += 1
        idxs_diferentes += f'[{idx}], '

idxs_diferentes = idxs_diferentes[:-2] 

print(f'La distancia Hamming entre las cadenas: {cadena1} y {cadena2}\n'
      f'es de: {distancia_hamming}\n'
      f'Diferencias en índices: {idxs_diferentes}\n')
