def final():
    
    fin = int(input("Elije una opcion: \n 1- Seguir Jugando \n 2-Dejar de Jugar: \n"))
    if fin == 2:
        global ok
        ok = False
    return ok

ok = True

while ok:
    
    person1 = input("Nombre del jugador 1: \n")
    person2 = input("Nombre del jugador 2: \n")

    mov1 = int(input(f"{person1}, elije tu movimiento: \n 1- Piedra  2- Papel  3- Tijera: \n"))
    mov2 = int(input(f"{person2}, elije tu movimiento: \n 1- Piedra 2- Papel 3- Tijera: \n"))

    if mov1 == 1 and mov2 ==3:
        print(f"Gana {person1}. Piedra le gana a tijera")
    elif mov1 == 2 and mov2 == 1:
        print(f"Gana {person1}. Papel le gana a piedra")
    elif mov1 == 3 and mov2 == 2:
        print(f"Gana {person1}. Tijera le gana a papel")
    elif mov2 == 1 and mov1 == 3:
        print(f"Gana {person2}. Piedra le gana a tijera")
    elif mov2 == 2 and mov1 == 1:
        print(f"Gana {person2}. Papel le gana a piedra.")
    elif mov2 == 3 and mov1 == 2:
        print(f"Gana {person2}. Tijera le gana a papel.")
    else:
        print("Empate")
    final()
    

