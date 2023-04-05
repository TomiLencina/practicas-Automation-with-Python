import json
import pandas as pd

# Cargar el archivo JSON en un DataFrame
with open('json.json', 'r') as f:
    datos_json = json.load(f)

df_json = pd.DataFrame(datos_json)

# Cargar la hoja "Servicio" del archivo Excel en un DataFrame
df_excel = pd.read_excel('asegurados.xlsx', sheet_name='Servicio', index_col=0)

print("Valores del archivo JSON:")
print(df_json.head())

print("Valores del archivo Excel antes de la actualización:")
print(df_excel.head())

# Recorrer las filas del DataFrame del archivo Excel
for indice_fila in df_excel.index:
    # Si la fila coincide con una clave del archivo JSON
    if indice_fila in df_json.columns:
        print("Coincidencia encontrada para la fila:", indice_fila)
        # Obtener el valor correspondiente del archivo JSON
        valor = df_json[indice_fila][0]
        # Reemplazar "string" con el valor correspondiente del archivo JSON
        df_excel.loc[indice_fila] = df_excel.loc[indice_fila].replace('string', valor)
        print("Valor actualizado para la fila", indice_fila, ":", df_excel.loc[indice_fila])

# Guardar el DataFrame final en un archivo Excel
df_excel.to_excel('archivo_actualizado.xlsx', index=True)

print("Valores del archivo Excel después de la actualización:")
print(df_excel.head())
