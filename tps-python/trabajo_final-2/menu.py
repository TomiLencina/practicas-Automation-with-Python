import json



RESPUESTAS = {}

def respuestas():
  for opcion , respuesta in RESPUESTAS.items():
    print(f'{opcion}')
    for clave , valor in respuesta.items():
      print(f' {clave}  :  {valor}')
  print()

def respuesta(res):
  for clave , valor in res.items():
    print(f' {clave}  :  {valor}')
  print()


#Rta 1
def opcion1(continent_list_obj):
  total = 0
  continent = ''
  repuesta = {}
  for i in continent_list_obj:
    if i.get_poblacion() > total :
      total = i.get_poblacion()
      continent = i.get_nombre()
  
  repuesta['Continente con mayor población'] = continent
  repuesta['Cantidad de población'] = total
  RESPUESTAS['La Respuesta Nro 1 es :'] = repuesta

  print('Respuesta:')
  respuesta(repuesta)


#Rta 2
def opcion2(continent_list_obj):
  repuesta = {}
  m = ''  
  uso_m = 0
  uso_c = 0
  c = ''
  uso_l = {}

  repuesta['En el Mundo'] = m

  for i in continent_list_obj:
    for clave, valor in i.get_idioma().items():
      if valor > uso_c:
        c = clave
        uso_c = valor
      
      if uso_l.get(clave) == None:
        uso_l[clave] = valor
      else:
        uso_l[clave] += valor

    if c != '':
      repuesta[i.get_nombre()] = c
    c = ''
    uso_c = 0

  for idioma, cant in uso_l.items():
    if cant > uso_m :
      m = idioma
      uso_m = cant

  repuesta['En el Mundo'] = m

  RESPUESTAS['La Respuesta Nro 2 es :'] = repuesta

  print('Respuesta:')
  respuesta(repuesta)


#Rta 3
def opcion3(country_list_obj):
  cant_monedas = {} 
  repuesta = {}
  for pais in country_list_obj:
    if cant_monedas.get(pais.get_monedas()) == None:
      cant_monedas[pais.get_monedas()] = 1
    else:
      cant_monedas[pais.get_monedas()] += 1

  total = 0
  for moneda, cant in cant_monedas.items():
    if cant > total :
      currency_mas_usada = moneda
      total = cant

  repuesta['La moneda que más se usa en el Mundo es'] = currency_mas_usada
  repuesta['Los paises que la usan son'] = total

  RESPUESTAS['La Respuesta Nro 3 es :'] = repuesta

  print('Respuesta:')
  respuesta(repuesta)


#Funcion para crear json con respuestas
def insert_respuestas():
  with open('db/respuestas.json', 'w') as respuestas:
    json.dump(RESPUESTAS, respuestas , indent= 2)
