# 2.	Escriba un programa en Python que acepte una ruta remota de recurso samba, 
# y lo separe en nombre(IP) del equipo y ruta
#	Entrada: //1.1.1.1/eoi/python
#	Salida: host=1.1.1.1; path=/eoi/python

ruta = input("Ingrese ruta samba: ")

#Elimino los dos caracteres iniciales que supongo, son dos barras inclinadas '//'
ruta_limpia = ruta[2:]

#Busco el índice de la siguiente barra inclinada
idx_end_host = ruta_limpia.index('/')

#Uso el índice para crear los dos strings pedidos
host = ruta_limpia[:idx_end_host]

path = ruta_limpia[idx_end_host:]

#Imprimo en el formato pedido
print(f"host={host}; path={path}")