import math

def area_circulo(radio):
    return round(math.pi * radio ** 2,2)

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura 


#Ejemplos 

#prueba1

#radio = int(input("Ingrese el radio de su circulo: \n \t"))

#prueba2

radio = int(input("Ingrese el radio del cilindro: \n \t"))
altura = int(input("Ingrese la altura"))
volumen = volumen_cilindro(radio, altura)
print(f"El volumen del cilindrio es{volumen}")

