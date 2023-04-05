#password

"""import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestNegativePassword:
    @pytest.mark.password
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123",
                               "Your username is invalid!"),
                              ("student", "incorrectPassword",
                               "Your password is invalid!")])
    def test_negative_password(self, username, password, expected_error_message):

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

        driver.quit()
"""

#username
""""# Open browser
# selenium 4
import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Negativeusername:

    @pytest.mark.invalid_username
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password,expected_error_message",
                             [
                                 ("incorrectUser", "Password123", "Your username is invalid!"),
                                 ("student", "incorrectPassword", "Your password is invalid!")
                             ])
    def test(self, driver, username, password, expected_error_message) -> None:
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, 'password')
        password_locator.send_keys(password)

        # Push Submit button
        button_locator = driver.find_element(By.ID, 'submit')
        button_locator.click()

        # Verify error message is displayed
        time.sleep(1)
        message = driver.find_element(By.XPATH, '//*[@id="error"]')
        assert message.is_displayed()

        # Verify error message text is "Your username is invalid!"
        error_text = driver.find_element(By.XPATH, '//*[@id="error"]').text
        assert error_text == expected_error_message
"""

#loginsuccesufully
# Open browser
# selenium 4
"""import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
        print("Creating chrome driver")
        my_driver = webdriver_Chrome(service=ChromeService(ChromeDriverManager().install()))
        yield my_driver
        print("closing chrome driver")
        my_driver.quit()


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):

        # ir a la pag
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # meter usuario
        user = driver.find_element(By.XPATH, "//input[@id='username']")
        user.send_keys("student")
        time.sleep(2)

        # meter contra
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys("Password123")
        time.sleep(2)

        # btn submit
        btn_submit = driver.find_element(By.XPATH, "//button[@id='submit']")
        btn_submit.click()
        time.sleep(2)

        # comprobar nueva url exitosa
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # comprobar mensaje de exito
        msg_exito = driver.find_element(By.XPATH, "//h1[contains(.,'Logged In Successfully')]")
        msg = msg_exito.text
        assert msg == "Logged In Successfully"

        # comprobar boton de logout
        btn_logout = driver.find_element(By.XPATH, "//a[contains(.,'Log out')]")
        assert btn_logout.is_displayed()
"""
