
def adivinar_num():
    objetivo = 125
    contador = 0
    
    while True:
        num = int(input('Ingrese el numero secreto: \n \t')) 
        if objetivo > num:
            print(f'El numero secreto es mayor que {num}')
            contador += 1
            continue
        elif objetivo < num:
            print(f'El numero secreto es menor que {num}')
            contador += 1
            continue
        else:
            print(f'Felicitaciones, adivinaste el numero... Era {objetivo} \n Lo lograste en {contador} intentos')
            break
adivinar_num()