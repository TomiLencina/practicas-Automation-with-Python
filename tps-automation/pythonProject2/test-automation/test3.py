# Open browser
# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(2)

# ir a la pag
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

#meter usuario
new_user = driver.find_element(By.XPATH,"//input[@id='username']")
new_user.send_keys("student")
time.sleep(1)

#meter contra
new_contra = driver.find_element(By.XPATH,"//input[@id='password']")
new_contra.send_keys("incorrectPassword ")

#boton enviar
btn_submit = driver.find_element(By.ID, "submit")
btn_submit.click()
time.sleep(1)

#controlar que la contra es invalida
text_invalido = driver.find_element(By.XPATH,"//div[@id='error']")
text_invalido.is_displayed()
time.sleep(2)

#controlar que el texto que aparece es Your username is invalid!
text = text_invalido.text
assert text == "Your password is invalid!"
time.sleep(2)