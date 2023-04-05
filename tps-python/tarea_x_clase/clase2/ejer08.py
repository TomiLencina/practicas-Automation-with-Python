'''
8.	Escriba un programa que encuentre la mínima secuencia de múltiplos de 3 (distintos) 
cuya suma sea igual o inferior a un valor dado.
Ejemplo
•	Entrada: 45
•	Salida: 0, 3, 6, 9, 12, 15

'''

numero = None

ingresando_numero = True

while ingresando_numero:
    str_numero = input("Ingrese un número natural: ").strip()
    numero = int(str_numero) if str_numero.isdigit() else None
    
    if numero is not None:
        ingresando_numero = False
    else:
        print(f'Valor ingresado incorrecto. Reintente')

suma = 0

print(f'\nSecuencia: 0', end='')

for multiplo_3 in range(3, numero, 3):

    suma += multiplo_3

    if suma <= numero:
        print(f', {multiplo_3}', end= '')
    else:
        print(f' : Suma = {suma - multiplo_3}\n')
        break