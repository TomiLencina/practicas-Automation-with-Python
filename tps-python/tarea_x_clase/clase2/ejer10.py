'''
10.	Escriba un programa en Python que acepte dos cadenas de texto 
y compute el producto cartesiano letra a letra entre ellas.
Ejemplo
•	Entrada: str1=abc; str2=123
•	Salida: a1 a2 a3 b1 b2 b3 c1 c2 c3
'''

print("Programa para calcular producto cartesiano de dos cadenas de texto")

cadena1 = input('Ingrese primer  cadena: ')
cadena2 = input('Ingrese segunda cadena: ')

print(f'\n{" ":3s}', end= '|')

for char2 in cadena2:
    print(f'{char2:^7s}', end= '')

print(f'\n{"_" * 3}|{"_" * 7 * len(cadena2)}')

for char1 in cadena1:
    print(f'{char1:3s}', end='|')
    
    for char2 in cadena2:
        print(f'{"(" + char1 + "," + char2 + ")":^7s}', end= '')
    print()

print()