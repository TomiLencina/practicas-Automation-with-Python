#3.	Escriba un programa en Python que acepte un «string» con los 8 dígitos de un NIF, 
# y calcule su dígito de control
#	Entrada: 12345678
#	Salida: 12345678Z

CODIGOS = 'TRWAGMYFPDXBNJZSQVHLCKE'

#El índice del string "codigos" es la letra a agregar al DNI

str_dni = input("Ingrese un DNI: ")

#Paso DNI a número
dni = int(str_dni)

#Resto de la división por 23, que será el índice de códigos
idx_cod = dni % 23

#codigo
codigo = CODIGOS[idx_cod : idx_cod+1]

nif = str_dni + codigo

print(f"El NIF correspondiente es: {nif}")



