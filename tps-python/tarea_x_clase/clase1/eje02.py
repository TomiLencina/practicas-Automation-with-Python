# Calcular las raíces de una expresión cuadrática
# Expresión: 2x^2 - 3x + 4 = 0

# coeficientes
#a = 2
#b = -3
#c = 4
a = int(input('Ingrese coeficiente a: '))
b = int(input('Ingrese coeficiente b: '))
c = int(input('Ingrese coeficiente c: '))


#x1
x1 = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)

#x2
x2 = (-b - (b **2 - 4 * a * c) ** (1/2)) / (2 * a)


print(f"Las raíces de la expresión cuadrática {a}x^2 + ({b})x + ({c}) = 0 son:\n")
print(f"\t x1 = {x1}")
print(f"\t x2 = {x2}")


#Verificación

cero_x1 = a*(x1 ** 2) + b*x1 + c

cero_x2 = a*(x2 ** 2) + b*x2 + c

print(
'''\nVerificamos los resultados reemplazando cada una de las raíces 
en el miembro izquierdo, el resultado debiera dar el valor que 
tenemos en el miembro derecho, es decir: 0 (o muy próximo a 0)\n''')

print(f"\t Reemplazando x1 en la expresión el resultado es = {cero_x1:.6f}")
print(f"\t Reemplazando x2 en la expresión el resultado es = {cero_x2:.6f}")

print(f"Tipo de cero_x1{type(cero_x1)}")

print('')
