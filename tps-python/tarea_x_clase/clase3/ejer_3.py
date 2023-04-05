#. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
# ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
# mensaje informando de ello

frutas = dict()


frutas = {
    "banana" : 1.35,
    "manzana" : 0.80,
    "pera" : 0.85,
    "naranja" : 0.70
}
ok = True

def verduleria():
    while ok:
        fruta = input("Ingrese la fruta que desea: \n \t")
        
        if fruta in frutas:
            kg = int(input("Ingrese la cantidad de kg que necesita: \n \t "))
            total = frutas[fruta] * kg
            print(f"---El total de su pedido es:  \n \t  \t \t \t ${total} ")
            sc = int(input("Si desea seguir comprando ponga 1, de lo contrario ponga 2: \n  \t"))
            if sc == 1:
                continue
            else:
                break
        else:
            print ("---No tenemos esa fruta---")
            sc = int(input("Si desea seguir comprando ponga 1, de lo contrario ponga 2: \n \t"))
            if sc == 1:
                continue
            else:
                break
    
verduleria()

