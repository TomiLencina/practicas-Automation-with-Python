# ----Numero Factorial----

def obtener_factorial(num): 
    if num < 0: 
        print("No es posible obtener el factorial de un numero negativo")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

num = int(input("Ingrese un numero positivo:\n \t") )
print(f"Factorial de {num} es {obtener_factorial(num)}") 


