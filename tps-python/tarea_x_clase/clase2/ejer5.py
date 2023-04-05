# DONADORES DE SANGRE



def obtener_datos():
    global edad
    global peso
    global pulsaciones
    global  tension
    global plaquetas
    print("Ingrese los siguientes datos...")
    
    edad = int(input("Ingrese su edad: "))
    peso = int(input("Ingrese su peso: "))
    pulsaciones = int(input("Pulsaciones: "))
    tension = int(input("Ingrese su tension: "))
    plaquetas = int(input("Plaquetas: "))
    
    return(edad,peso,pulsaciones,tension,plaquetas)

def validacion():
    if edad >= 18 and edad <= 65:
        if peso > 50:
            if pulsaciones >= 50 and pulsaciones <= 110:
                if tension > 50 and tension < 180: 
                    if plaquetas >= 150000:
                        print("Donador apto")
                    else:
                        print("Donador NO apto por falla en las plaquetas")    
                else:
                    
                    print("Donador NO apto por falla en la tension")
            else:
                print("Donador NO apto por falla en las pulsaciones")
        else:
            print("Donador NO apto por falla en el peso")
    else:
        print("Donador NO apto por no cumplir con la edad requerida")

def donador_apto():
    obtener_datos()
    validacion()

donador_apto()