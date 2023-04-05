#   Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra.

def is_isograma():
    cadena = input("Ingrese una cadena de texto: ")
    if len(cadena) != len(set(cadena)):
        print("Esta palabra no es un isograma")
    else:
        print("Esta palabra si es un isograma")

is_isograma()

