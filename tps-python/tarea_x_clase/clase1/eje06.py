#6.	Leer dos números por teclado, realizar las operaciones básicas entre ellos: 

'''
    a.	Suma
    b.	Resta
    c.	Multiplicación
    d.	División
    e.	División Entera
    f.	Módulo
    g.	Potencia

'''

print("Ingrese dos números para efectuar las operaciones básicas")

str_num1 = input("Ingrese número 1: ")

str_num2 = input("Ingrese número 2: ")

#Conversión a flotante
num1 = float(str_num1)
num2 = float(str_num2)

print(f"Typo num1: {type(num1)}")
print(f"Typo num2: {type(num2)}")

#Operaciones
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
div_ent = num1 // num2
resto = num1 % num2
potencia = num1 ** num2



#Suma
print(f"{num1:.4g} + {num2:.4g} \t= {suma:<20.4g}")

#Resta
print(f"{num1:.4g} - {num2:.4g} \t= {resta:<20.4g}")

#Multiplicación
print(f"{num1:.4g} * {num2:.4g} \t= {mult:<20.4g}")

#División
print(f"{num1:.4g} / {num2:.4g} \t= {div:<20.4g}")

#División Entera
print(f"{num1:.4g} // {num2:.4g} \t= {div_ent:<20.4g}")

#Resto de la división entera (módulo)
print(f"{num1:.4g} % {num2:.4g} \t= {resto:<20.4g}")

#Potencia
print(f"{num1:.4g} ^ {num2:.4g} \t= {potencia:<20.4g}")