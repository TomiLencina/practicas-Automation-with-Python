from lectura import lectura_j
from menu import opcion1, opcion2, opcion3, insert_respuestas, respuestas

# opciones de respuestas
def home():
  print('Escoja la respuesta que desea obtener:')
  print('1 - Qué continente tiene mayor población? Y cuál es el número?')
  print('2 - Cual es el idioma más hablado en el mundo y cuál por cada continente?')
  print('3 - Qué moneda se usa en más países y cuántos países son los que la usan?')
  print('4 - Salir')
  
  option = opcion()

  return option


# Validacion de las opciones del menu
def opcion():
  option = input("Escoja una opcion: ")

  if option.isdigit():
    if int(option)<1:
      print(f'  La opción {option} es incorrecta...')
      print("Intente de nuevo")
      return opcion()
    elif int(option)>4:
      print(f'  La opción {option} es incorrecta...')
      print("Intente de nuevo")
      return opcion()
    return int(option)


def run():
    
    country_list_obj, continent_list_obj = lectura_j()
    #Menú principal
    ok = False

    while not ok:
        opcion = home()

        if opcion == 1:
          opcion1(continent_list_obj)

        elif opcion == 2:
          opcion2(continent_list_obj)

        elif opcion == 3:
            opcion3(country_list_obj)

        elif opcion == 4:
            ok = True
            respuestas()
    insert_respuestas()

    exit()

if __name__ == "__main__":
    run()