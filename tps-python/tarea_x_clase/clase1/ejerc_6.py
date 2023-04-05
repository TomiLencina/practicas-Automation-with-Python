print("***CALCULADORA***")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. División")
print("5. División de enteros")
print("6. Modulo")
print("7. Potencia")
print("8. Salir")

def suma():
    numUno = int(input("Ingrese el primer valor a sumar: "))
    numDos = int(input("Ingrese el segundo valor a sumar: "))
    result = numUno + numDos
    print(result)  

def resta():
    numUno = int(input("Ingrese el primer valor a restar: "))
    numDos = int(input("Ingrese el segundo valor a restar: "))
    result = numUno - numDos
    print(result)

def mulitplicacion():
    numUno = int(input("Ingrese el primer valor a mulitplicar: "))
    numDos = int(input("Ingrese el segundo valor a mulitplicar: "))
    result = numUno * numDos
    print(result)

def division():
    numUno = int(input("Ingrese el primer valor a dividir: "))
    numDos = int(input("Ingrese el segundo valor a dividir: "))
    result = numUno / numDos
    print(result)

def divisionEntera():
    numUno = int(input("Ingrese el primer valor a dividir: "))
    numDos = int(input("Ingrese el segundo valor a dividir: "))
    result = numUno // numDos
    print(result)

def modulo():
    numUno = int(input("Ingrese el primer valor del modulo: "))
    numDos = int(input("Ingrese el segundo valor del modulo: "))
    result = numUno % numDos
    print(result)

def potencia():
    numUno = int(input("Ingrese el valor de la base: "))
    numDos = int(input("Ingrese el del exponente: "))
    result = numUno ** numDos
    print(result)


ok = True
while ok:

    opcion = int(input("Ingrese la operacion que desee: "))
    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        mulitplicacion()
    elif opcion == 4:
        division()
    elif opcion == 5:
        divisionEntera()
    elif opcion == 6:
        modulo()
    elif opcion == 7:
        potencia()
    elif opcion == 8:
        ok = False
        print("Cerrando calculadora")
        break
    else:
        print("ESCOJA UN NUMERO DEL 1 AL 8...")
        continue


