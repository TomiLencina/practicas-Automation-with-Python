import json
from clases import Continentes, Pais


# constantes - claves de los json

PAIS = 'country'
CONTINENTE = 'continent'
MONEDA_COD = 'currency_code'
POBLACION = 'population'
LENGUAGES = 'languages'


#funcion para verificar si la clave que se busca esta en la lista
def in_list(lista, busqueda): 
  try:
    oi = lista.index(busqueda)
    return True
  except:
    return False


# Funcion para la lectura de los json
  
def lectura_j():
  
  with open('json\country-by-continent.json') as file:
    country_continent = json.load(file)

  with open('json\country-by-currency-code.json') as file:
    country_code = json.load(file)

  with open('json\country-by-population.json') as file:
    country_p = json.load(file)

  with open('json\country-by-languages.json') as file:
    country_l = json.load(file)

  obj_continent = []  
  list_country = [] 
  list_continent = [] 
  
  #creacion de obj pais y asignacion de moneda 
  for p in country_code:
    list_country.append(Pais(p.get(PAIS), p.get(MONEDA_COD)))

  #crea obj continente y agrega continente a list_continent
  for c in country_continent:
    if not in_list(list_continent, c.get(CONTINENTE)):
      list_continent.append(c.get(CONTINENTE))
      obj_continent.append(Continentes(c.get(CONTINENTE)))

  #agregar obj pais al obj continente
    for co in obj_continent :
      if co.get_nombre() == c.get(CONTINENTE):
        index_c = obj_continent.index(co)
        for country in list_country:
          if country.get_nombre() == c.get(PAIS):
            country.set_continente(obj_continent[index_c])
  
  #agrega poblacion al obj pais
  for pob in country_p:
    for pais in list_country:
      if pob.get(PAIS) == pais.get_nombre():
        pais.set_poblacion(pob.get(POBLACION))
        pais.update_p()

  #agrega los lenguajes al obj pais
  for lenguas in country_l:
    for pais in list_country:
      if lenguas.get(PAIS) == pais.get_nombre():
        for i in lenguas.get(LENGUAGES):
          pais.lenguaje.append(i)
        pais.update_l()
  
  return list_country, obj_continent

print(lectura_j())


