from read_json import read
from options import o1, o2, o3, insert_respuestas, respuestas


def opcion():
  option = input("Coloque el número de la opción elegida:")

  if option.isdigit():
    if int(option)<1:
      print(f'  La opción {option} no existe')
      return opcion()
    elif int(option)>4:
      print(f'  La opción {option} no existe')
      return opcion()
    return int(option)


def home():
  print('Elija la pregunta que quiere hacer:')
  print('1 - ¿Cual es el continente que tiene mayor población?')
  print('2 - ¿Cual es el idioma más usado en cada continente?')
  print('3 - ¿Cual es la Moneda mas usada ?')
  print('4 - No hacer ninguna pregunta')
  option = opcion()

  return option


def run():
    
    country_list_obj, continent_list_obj = read()
    #Menú principal
    salir = False

    while not salir:
        opcion = home()

        if opcion == 1:
          o1(continent_list_obj)

        elif opcion == 2:
          o2(continent_list_obj)

        elif opcion == 3:
            o3(country_list_obj)

        elif opcion == 4:
            salir = True
            respuestas()
    insert_respuestas()

    exit()

if __name__ == "__main__":
    run()