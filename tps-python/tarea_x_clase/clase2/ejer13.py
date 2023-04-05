'''
13.	Escriba un programa que calcule el máximo común divisor entre dos números enteros. No utilice ningún algoritmo existente. Hágalo probando divisores.
Ejemplo

•	Entrada: a=12; b=44
•	Salida: 4
'''

numero1 = None
numero2 = None

ingresando_numeros = True

print(f"Programa para calcular el MCD entre dos números\n")

while ingresando_numeros:
    if numero1 is None:
        str_numero1 = input("Ingrese primer número natural: ").strip()
        numero1 = int(str_numero1) if str_numero1.isdigit() else None
    
    if numero2 is None:
        str_numero2 = input("Ingrese segundo número natural: ").strip()
        numero2 = int(str_numero2) if str_numero2.isdigit() else None

    if (numero1 is not None) and (numero2 is not None):
        ingresando_numeros = False

#Empiezo a dividir por el menor de ellos a los dos

minimo_div = min(numero1, numero2)

for div_test in range(minimo_div, 0, -1):
    if (numero1 % div_test == 0) and (numero2 % div_test == 0):
        minimo_div = div_test
        break

print(f'\nEl Máximo Común Dividor es = {minimo_div}\n')