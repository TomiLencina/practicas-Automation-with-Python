#Numero primo


def num_primo():
    num = int(input("Ingrese el numero: \n"))

    if num == 0 or num == 1:
        print("No es primo")
        pass
    elif num == 2:
        print("Es primo")
    elif num > 2:
        for i in range(2,num):
            if num % i == 0:
                print("No es primo")
                pass
            elif num % i != 0 and i == num-1:
                print("Es primo")

num_primo()