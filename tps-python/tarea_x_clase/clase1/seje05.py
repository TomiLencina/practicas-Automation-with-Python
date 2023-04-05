#5.	Escriba un programa en Python que acepte una palabra en castellano y
#   calcule una métrica que sea el número total de caracteres de la palabra multiplicado 
#   por el número total de vocales que contiene la palabra.
#	Entrada: ordenador
#	Salida: 36

print("Programa para calcular la métrica de una palabra")

palabra = input("Ingrese una palabra: ")

# Número de caracteres
num_caracteres = len(palabra)

# Si hay vocales con tilde, las reemplazo primero por la vocal sin tilde,
# además trabajo con la cadena en minúsculas.

palabra_s_til = palabra.lower().replace('á', 'a')
palabra_s_til = palabra_s_til.replace('é', 'e')
palabra_s_til = palabra_s_til.replace('í', 'i')
palabra_s_til = palabra_s_til.replace('ó', 'o')
palabra_s_til = palabra_s_til.replace('ú', 'u')

# Cuento el número de vocales
num_a = palabra_s_til.count('a')
num_e = palabra_s_til.count('e')
num_i = palabra_s_til.count('i')
num_o = palabra_s_til.count('o')
num_u = palabra_s_til.count('u')

num_vocales = num_a + num_e + num_i + num_o + num_u

#Cálculo de la métrica
metrica = num_caracteres * num_vocales

#Salida
print(f"{metrica}")