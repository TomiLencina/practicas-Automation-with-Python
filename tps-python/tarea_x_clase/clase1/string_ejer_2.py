
print("Convertidor")
ruta = int(input("Ingrese su ruta remota de recurso samba: "))

for i in len(ruta):
    if ruta[i] == "/":
        if ruta[i+1] == "/":
            del(ruta[0:1])
            print(ruta)