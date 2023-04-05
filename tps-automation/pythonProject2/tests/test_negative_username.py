"""import time
import pytest
from selenium.webdriver.common.by import By
"""

"""
class Test_Negativeusername:

    @pytest.mark.invalid_username
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password,expected_error_message",
                             [
                                 ("incorrectUser", "Password123", "Your username is invalid!"),
                                 ("student", "incorrectPassword", "Your password is invalid!")
                             ])
    def test(self, driver, username, password, expected_error_message):
        # ir a la web
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # meter username incorrecto
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys(username)

        # meter una contraseña incorrecta
        password_locator = driver.find_element(By.NAME, 'password')
        password_locator.send_keys(password)

        # clic al boten submit
        button_locator = driver.find_element(By.ID, 'submit')
        button_locator.click()

        # verificar que el mensaje de error este disponible
        time.sleep(1)
        message = driver.find_element(By.XPATH, '//*[@id="error"]')
        assert message.is_displayed()

        # verificar que el mensaje de error es el siguiente "Your username is invalid!"
        error_text = driver.find_element(By.XPATH, '//*[@id="error"]').text
        assert error_text == expected_error_message"""


import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    @pytest.mark.negative
    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username  student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(5)

        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed"

        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"