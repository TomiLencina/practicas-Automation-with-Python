
def calc_vocal():
    palabra = input("Ingrese una palabra en castellano: \n")
    tamaño = len(palabra)
    vocal = 0
    for letra in palabra:
        if letra.lower() in "aeiou":
            vocal += 1
    print (tamaño * vocal)

calc_vocal()