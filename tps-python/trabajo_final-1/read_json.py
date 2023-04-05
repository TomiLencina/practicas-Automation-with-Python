import json
from continents import Continents
from country import Country

COUNTRY = 'country'
CONTINENT = 'continent'
CURRENCY_CODE = 'currency_code'
POPULATION = 'population'
LENGUAGES = 'languages'

def in_list(lista, busqueda): 
  try:
    oi = lista.index(busqueda)
    return True
  except:
    return False

def read():
  
  obj_continent = []  
  list_country = []        
  list_continent = []  

  with open('fede\db\country-by-continent.json') as file:
    country_continent = json.load(file)

  with open('fede\db\country-by-currency-code.json') as file:
    country_code = json.load(file)

  with open('fede\db\country-by-population.json') as file:
    country_p = json.load(file)

  with open('fede\db\country-by-languages.json') as file:
    country_l = json.load(file)

  
  for p in country_code:
    list_country.append(Country(p.get(COUNTRY), p.get(CURRENCY_CODE)))


  for c in country_continent:
    if not in_list(list_continent, c.get(CONTINENT)):
      list_continent.append(c.get(CONTINENT))
      obj_continent.append(Continents(c.get(CONTINENT)))

    for co in obj_continent :
      if co.get_nombre() == c.get(CONTINENT):
        index_c = obj_continent.index(co)
        for country in list_country:
          if country.get_nombre() == c.get(COUNTRY):
            country.set_continente(obj_continent[index_c])

  for pob in country_p:
    for pais in list_country:
      if pob.get(COUNTRY) == pais.get_nombre():
        pais.set_poblacion(pob.get(POPULATION))
        pais.update_p()

  for lenguas in country_l:
    for pais in list_country:
      if lenguas.get(COUNTRY) == pais.get_nombre():
        for i in lenguas.get(LENGUAGES):
          pais.lenguaje.append(i)
        pais.update_l()

  return list_country, obj_continent
