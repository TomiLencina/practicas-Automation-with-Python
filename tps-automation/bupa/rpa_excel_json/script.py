import json
import pandas as pd

# Cargar el archivo JSON en un DataFrame
with open('json.json', 'r') as f:
    datos_json = json.load(f)

df_json = pd.DataFrame(datos_json)

# Cargar la hoja "Servicio" del archivo Excel en un DataFrame
df_excel = pd.read_excel('asegurados.xlsx', sheet_name='Servicio')

# Recorrer las columnas del DataFrame del archivo Excel
for columna in df_excel.columns:
    # Si la columna coincide con una clave del archivo JSON
    if columna in df_json.columns:
        # Reemplazar "string" con el valor correspondiente del archivo JSON
        df_excel[columna] = df_excel[columna].replace('string', df_json[columna])

# Guardar el DataFrame final en un archivo Excel
df_excel.to_excel('archivo_actualizado2.xlsx', index=False)
