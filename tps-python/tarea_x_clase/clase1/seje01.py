#1.	Escriba un programa en Python que acepte el nombre y los apellidos de una persona 
# y los imprima en orden inverso separados por una coma. Utilice f-strings para implementarlo.


nombre_apellidos = input("Ingrese Nombre y Apellidos, separados por coma: ")

print(nombre_apellidos.split(','))
print(type(nombre_apellidos.split(sep= ',')))
print()
nombre = nombre_apellidos.split(sep= ',')[0]
apellidos = nombre_apellidos.split(sep= ',')[1]

#['nombre', 'apellidos']

#apellidos = input("ingrese Apellidos: ")

print(f"{apellidos}, {nombre}")