# Open browser
# selenium 4
import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(2)

# ir a la pag
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

#completar usuario
usuario = driver.find_element(By.XPATH, "//input[@id='username']")
usuario.send_keys("student")

#completar contraseña
contra = driver.find_element(By.XPATH, "//input[@id='password']")
contra.send_keys("Password123")

#boton enviar
btn_enviar = driver.find_element(By.XPATH, "//button[@id='submit']")
btn_enviar.click()
time.sleep(2)

#verificar nueva url
actual_url = driver.current_url
assert actual_url =="https://practicetestautomation.com/logged-in-successfully/"

#texto  de exito
actual_text = driver.find_element(By.TAG_NAME,"h1")
text = actual_text.text
assert text == "Logged In Successfully"

#esta disponible el logout?
log_out_button_locator = driver.find_element(By.XPATH, "//a[contains(.,'Log out')]")
assert log_out_button_locator.is_displayed()"""

#definir navegador
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(2)

# ir a la pag
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)


#meter usuario
user = driver.find_element(By.XPATH, "//input[@id='username']")
user.send_keys("student")
time.sleep(2)

#meter contra
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("Password123")
time.sleep(2)

#btn submit
btn_submit = driver.find_element(By.XPATH, "//button[@id='submit']")
btn_submit.click()
time.sleep(2)

#comprobar nueva url exitosa
actual_url = driver.current_url
assert actual_url =="https://practicetestautomation.com/logged-in-successfully/"



#comprobar mensaje de exito
msg_exito = driver.find_element(By.XPATH, "//h1[contains(.,'Logged In Successfully')]")
msg = msg_exito.text
assert msg == "Logged In Successfully"

# comprobar boton de logout
btn_logout = driver.find_element(By.XPATH, "//a[contains(.,'Log out')]")
assert btn_logout.is_displayed()







