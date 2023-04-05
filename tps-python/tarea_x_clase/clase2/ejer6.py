ok = True

while ok:
    num = int(input("Ingrese un numero: "))
    
    for i in range(num):
        if (i * 5)<num:
            print (i * 5)
            continue
        else:
            ok = False
            break
