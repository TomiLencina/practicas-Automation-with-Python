# Dada una cadena de texto que representa una fecha (mes/día/año truncado): ‘3/30/20’ 
# transfórmela en otra cadena de texto con el siguiente formato: ‘31-12-2020’ (día-mesaño completo)

def fechas():
    fecha = input("Ingrese una fecha con formato mes/dia/año truncado... \n")

    nueva_fecha = fecha.split("/")

    nueva_fecha[2] = "20{}".format(nueva_fecha[2])
    print(f"El nuevo formato de la fecha es dd-mm-yy \n {nueva_fecha[1]}/{nueva_fecha[0]}/{nueva_fecha[2]}")


fechas()
