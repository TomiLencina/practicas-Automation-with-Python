# Conversión de tipo de variable

var_flotante = 4.2
var_booleana = True
var_entera = 5

titulo_col1 = 'Valor Original'
titulo_col2 = 'Tipo a Convertir'
titulo_col3 = 'Valor Convertido'

titulo_sup = '_' * (20*3 + 4)
titulo_sep = '|' + ('_' * (20) + '|') * 3

# Imprimo títulos de la tabla
print(f"{titulo_sup}")
print(f"|{titulo_col1 :>20}|{titulo_col2:^20}|{titulo_col3:^20}|")
print(f"{titulo_sep}")

#Imprimo los valores de cada fila
print(f"|{var_flotante:^20.2f}|{'int':^20}|{int(var_flotante):^20}|")

print(f"|{var_flotante:^20.2f}|{'bool':^20}|{str(bool(var_flotante)):^20}|")

print(f"|{str(var_booleana):^20}|{'int':^20}|{int(var_booleana):^20}|")

print(f"|{str(var_booleana):^20}|{'float':^20}|{float(var_booleana):^20}|")

print(f"|{var_entera:^20}|{'float':^20}|{float(var_entera):^20}|")

print(f"|{var_entera:^20}|{'bool':^20}|{str(bool(var_entera)):^20}|")

print(f"{titulo_sep}")