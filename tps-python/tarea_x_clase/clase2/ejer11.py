'''
11.	Escriba un programa en que acepte dos valores enteros (x e y) que representarán un punto (objetivo) 
en el plano. El programa simulará el movimiento de un «caballo» de ajedrez moviéndose de forma alterna: 
primero avanzando 2 posiciones en x más 1 posición en y. 
En el siguiente movimiento se moverá 1 posición en x más 2 posiciones en y. 
El programa deberá ir mostrando los puntos por los que va pasando el «caballo» hasta llegar al punto objetivo. 
Extra: Agregue las otras posibilidades de movimiento que tiene el caballo para encontrar otras posiciones del 
tablero a ingresar manualmente, dando la posibilidad de modificar además el punto de partida del caballo.
Ejemplo (problema básico)

•	Entrada: objetivo_x=7; objetivo_y=8;
•	Salida: (0, 0) (1, 2) (3, 3) (4, 5) (6, 6) (7, 8)
'''

#En internet se encuentra que este es un problema planteado, cómo recorrer todas las casillas del tablero 
#con un caballo sin repetir casillas. Aquí no es tan estricto porque no dice que no pueda repetir
#no obstante usaré una estrategia planteada, que es primero recorrer las casillas periféricas

objetivo_x = 8
objetivo_y = 7

caballo_x = 1
caballo_y = 1

STR_MOVS = '(+2,+1);(+2,-1);(-2,+1);(-2,-1);(+1,+2);(-1,+2);(+1,-2);(-1,-2)'

NUM_MOVS = STR_MOVS.count('(')

MOV_LEN = STR_MOVS.index(')') + 2

CASILLAS_X_MAX = 8
CASILLAS_Y_MAX = 8

casillas_pisadas = ''

objetivo_no_alcanzado = True

while objetivo_no_alcanzado:

    #Valor para desbordar un cálculo y elegir movimientos distintos cada vez
    for num_desborde in range(1, 10):

        #Extraico y pruebo movimientos
        for mov in range(NUM_MOVS): # 0 ... 7

            #Indice de un movimiento, uso un desborde para que no siempre pruebe los movimientos en el mismo orden
            idx = ((mov ** num_desborde) % NUM_MOVS) * MOV_LEN
            
            #String de cada movimiento ej: (+2,-1)
            str_mov = STR_MOVS[idx: idx + MOV_LEN - 1]
            
            #Movimiento x, ejemplo: -2
            movx = int(str_mov[2]) * (1 if str_mov[1] == '+' else -1)
            
            #Movimiento y, ejemplo: 2
            movy = int(str_mov[5]) * (1 if str_mov[4] == '+' else -1)

            #Nueva coordenada tentativas del caballo
            new_caballo_x = caballo_x + movx
            new_caballo_y = caballo_y + movy

            # Seguir probando otro movimiento si las coordendas dan fuera del tablero
            if new_caballo_x <= 0 or new_caballo_y <= 0:
                continue

            elif new_caballo_x > CASILLAS_X_MAX or new_caballo_y > CASILLAS_Y_MAX:
                continue
            
            #Agregar la coordenada al historial
            str_casilla = f'({new_caballo_x},{new_caballo_y})'
            if str_casilla in casillas_pisadas:
                #Dejo que repita movimientos hechos antes
                pass
                #continue
            else:
                casillas_pisadas += str_casilla
                print(str_casilla)

            #Verificar si llegó al objetivo
            if new_caballo_x == objetivo_x and new_caballo_y == objetivo_y:
                print('Objetivo alcanzado!')
                objetivo_no_alcanzado = False
                break # del for secundario
            else:
                #Actualizar posición del caballo
                caballo_x = new_caballo_x
                caballo_y = new_caballo_y
        
        if objetivo_no_alcanzado == False:
            break # del for principal
        