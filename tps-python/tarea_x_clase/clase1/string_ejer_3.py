print("Calculador NIF") 

def calc_nif():
    dni = int(input("Ingrese su documento: "))
    nif = int(dni % 23)

    ok = True
    while ok:
        if nif == 0:
            print(str(dni)+"T")
            break
        elif nif == 1:
            print(str(dni)+"R")
            break
        elif nif == 2:
            print(str(dni)+"W")
            break
        elif nif == 3:
            print(str(dni)+"A")
            break
        elif nif == 4:
            print(str(dni)+"G")
            break
        elif nif == 5:
            print(str(dni)+"M")
            break
        elif nif == 6:
            print(str(dni)+"Y")
            break
        elif nif == 7:
            print(str(dni)+"F")
            break
        elif nif == 8:
            print(str(dni)+"P")
            break
        elif nif == 9:
            print(str(dni)+"D")
            break
        elif nif == 10:
            print(str(dni)+"X")
            break
        elif nif == 11:
            print(str(dni)+"B")
            break
        elif nif == 12:
            print(str(dni)+"N")
            break
        elif nif == 13:
            print(str(dni)+"J")
            break
        elif nif == 14:
            print(str(dni)+"Z")
            break
        elif nif == 15:
            print(str(dni)+"S")
            break
        elif nif == 16:
            print(str(dni)+"Q")
            break
        elif nif == 17:
            print(str(dni)+"V")
            break
        elif nif == 18:
            print(str(dni)+"H")
            break
        elif nif == 19:
            print(str(dni)+"L")
            break
        elif nif == 20:
            print(str(dni)+"C")
            break
        elif nif == 21:
            print(str(dni)+"K")
            break
        elif nif == 22:
            print(str(dni)+"E")
            break
        ok = False

calc_nif()