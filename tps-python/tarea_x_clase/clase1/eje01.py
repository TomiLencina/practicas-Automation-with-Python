# Calcular la superficie de un triángulo

print("\nPrograma para calcular la superficie de un triángulo\n")

str_base = input("Ingrese la medida de la base en mm: ")
str_altura = input("Ingrese la medida de la altura en mm: ")

#convierto a punto flotante los valores ingresados por teclado que en principio son strings
base = float(str_base)
altura = float(str_altura) 

superficie = base * altura
print(f"La superficie del triángulo es de: {superficie}")