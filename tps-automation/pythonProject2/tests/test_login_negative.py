"""import time
import pytest
from selenium.webdriver.common.by import By
"""

"""
class Test_Negativepassword:

    @pytest.mark.invalid_password
    @pytest.mark.negative
    def test(self, driver):
        # ir a la web
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # meter el username en el campo correspondiente
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys('student')

        # meter una contraseña incorrecta en el lugar correspondiente
        password_locator = driver.find_element(By.NAME, 'password')
        password_locator.send_keys('incorrectPassword')

        # clickear boton submit
        button_locator = driver.find_element(By.ID, 'submit')
        button_locator.click()

        time.sleep(1)
        # verificar que el mensaje de error esta disponible
        assert driver.find_element(By.XPATH, '//*[@id="error"]').is_displayed()

        # verificar que el mensaje de error sea "Your username is invalid!"
        error_text = driver.find_element(By.XPATH, '//*[@id="error"]').text
        assert error_text == "Your password is invalid!"
"""

import pytest
from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error_message, "Error message is not expected"
