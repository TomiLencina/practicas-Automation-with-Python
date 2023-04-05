#Escriba una función en Python que reciba una lista de valores enteros y devuelva otra lista
#sólo con aquellos valores pares.



def valores_pares(numeros):
    pares = [x for x in numeros if x % 2 == 0]
    return pares


numeros = [0,1,2,3,4,5,6,7,8,9]

print(valores_pares(numeros))