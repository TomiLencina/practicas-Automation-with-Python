### maximo, minimo y promedio de 3 nros

def calcular():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))

    maximo = max(a,b,c)
    minimo = min(a,b,c)
    promedio = (a+b+c)/3
    print(f"El maximo los numeros es {maximo}. \n El minimo de los numeros es {minimo}. \n El promedio de los 3 numeros es {promedio}")

calcular()