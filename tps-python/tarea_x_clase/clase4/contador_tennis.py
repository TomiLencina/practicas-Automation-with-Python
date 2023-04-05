#Contador tenis
puntos_doparti = "P1, P1, P2, P2, P1, P2, P1, P1"
puntos_partidos = puntos_doparti.split(",")
print(puntos_partidos)

def contador_tennis():
    p1 = "Love"
    p2 = "Love"
    ok = True
    for x in puntos_partidos:
            if x == "P1":
                if p1 == str:
                    p1 = 15
                elif p1 == 15:
                    p1 = 30
                elif p1 == 30:
                    p1 = 40
                elif p1 == 40 and p2 == 40:
                    p1 = "Deuce"
                elif p1 == "Deuce":
                    p1 = "Ventaja p1"
                elif p1 == "Ventaja p1":
                    p1 = "Ganador"            
            else:
                if p2 == str:
                    p2 = 15
                elif p2 == 15:
                    p2 = 30
                elif p2 == 30:
                    p2 = 40
                elif p2 == 40 and p2 == 40:
                    p2 = "Deuce"
                elif p2 == "Deuce":
                    p2 = "Ventaja p1"
                elif p2 == "Ventaja p1":
                    p2 = "Ganador"   
    marcador = p1 , p2
    print(marcador)


contador_tennis()