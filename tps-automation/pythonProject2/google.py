"""Crear test case que realice una búsqueda en google, verifique que cada elemento del resultado
contiene el texto buscado, luego clickee el tercer elemento y luego valide algún elemento de la
página encontrada.
Escribir el test case en formato BDD"""

import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from googlesearch import search

#funcion de busqueda correcta
def busqueda_correcta(busc):

# texto de búsqueda
    query = busc
    cont = 0

# iterar sobre los resultados de búsqueda
    for url in search(query, 5):
    # leer el contenido de la página web
        response = requests.get(url)
        content = response.content.decode("utf-8")
    # verificar si el texto de búsqueda aparece en la página web
        if query in content:
            cont += 1

    return cont


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(2)

# ir a la pag
driver.get("https://www.google.com.ar/")
time.sleep(2)

#Ingresar busqueda en el buscador
busqueda = "cosquin"
buscador = driver.find_element(By.XPATH, "//input[@title='Buscar']")
buscador.send_keys(busqueda)
time.sleep(2)
buscador.submit()
time.sleep(2)

#verificar que la busqueda es correcta
res_busq2 = busqueda_correcta(busqueda)
assert res_busq2 > 0

"""if res_busq2 > 0:
    print(res_busq2)
else:
    print("no se que busco")"""

#ingreso al tercer resultado
acceso = driver.find_element(By.XPATH, "(//h3[contains(.,'Cosquín - Wikipedia, la enciclopedia libre')])[2]")
acceso.click()
time.sleep(2)
url = driver.current_url
assert url == "https://es.wikipedia.org/wiki/Cosqu%C3%ADn"
time.sleep(5)

#verificar que esta pagina habla sobre cosquin
text = driver.find_element(By.XPATH, "//span[@class='mw-page-title-main']")
txt = text.text
assert txt == "Cosquín"
time.sleep(2)



