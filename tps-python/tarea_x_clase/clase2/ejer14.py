'''
14.	Escriba un programa que calcule el valor de x para el que la función 
f(x)=x^2-6x+3 obtiene su menor resultado. 
Centre la búsqueda en el rango [−9] a [9] sólo con valores enteros.

* El resultado es: x=3 y f(3)=-6 
'''

fminima = None
x_del_min = None

for x in range(-9, 9+1, 1):
    
    funcion = x ** 2 - 6 * x + 3

    if (fminima is None) or (funcion <= fminima):
        fminima = funcion
        x_del_min = x

print(f'\nPara que la función sea mínima, debe ser x = {x_del_min}\n'
      f'El valor de la función en el mínimo es f({x_del_min}) = {fminima}\n') 