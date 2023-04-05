orden = "----Orden: "

def pizza_vegetariana():
    print("Escoja un ingrediente para agregar... \n 1 - Pimiento \n 2 - Tofu ")
    ingrediente = int(input("Ingrese el numero de su ingrediente para agregar:\n "))
    if ingrediente == 1:
        print(f"{orden}Pizza Vegetariana con muzzarella, tomate y pimiento.")
    elif ingrediente == 2:
        print(f"{orden}Pizza Vegetariana con muzzarella, tomate y tofu.")
    else:
        print("Ingrese un numero valido")
    

def pizza_no_vegetariana():
    print("Escoja un ingrediente para agregar... \n 1 - Peperoni \n 2 - Jamón \n 3 - Salmón")
    ingrediente =int(input("Ingrese el numero de su ingrediente para agregar:\n "))
    if ingrediente == 1:
        print(f"{orden}Pizza No Vegetariana con muzzarella, tomate y peperoni.")
    elif ingrediente == 2:
        print(f"{orden}Pizza No Vegetariana con muzzarella, tomate y Jamon")
    elif ingrediente == 3:
        print(f"{orden}Pizza No Vegetariana con muzzarella, tomate y Salmon")
    else:
        print("Ingrese un numero valido")

def tipo_pizza():

    print("Bienvenido a la pizzeria Bella Napoli.")
    print("Elija el tipo de pizza que quiere... \n 1 - Vegetariana \n 2- No vegetariana")
    
    tipo = int(input("Ingrese el numero de su opcion: \n "))
    
    if tipo == 1:
        pizza_vegetariana()

    elif tipo == 2:
        pizza_no_vegetariana()


tipo_pizza()

