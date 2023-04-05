#4.	Escriba un programa en Python que acepte un entero n y compute el valor de n + nn + nnn
#	Entrada: 5
#	Salida: 615 (5 + 55 + 555)

print("Programa para calcular, a partir de un entero n, el valor n + nn + nnn ")

str_n = input("Ingrese un número entero: ")

# Valor numérico del entero n
n = int(str_n)

# Concateno n dos veces y lo paso a entero
nn = int(str_n + str_n)

# Concateno n tres veces y lo paso a entero
nnn = int(str_n * 3)

# Opero
resultado = n + nn + nnn

print(f"{resultado} ({n} + {nn} + {nnn})")