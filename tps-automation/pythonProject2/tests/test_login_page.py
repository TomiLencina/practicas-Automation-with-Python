"""import pytest
import time
from selenium.webdriver.common.by import By"""

import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfully
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfully(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"
        #assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"


"""
class Test_PositiveLogin:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver) -> None:
        # ir a la web
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # tipear username correctamente
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys('student')

        # tipear contraseña correctamente
        password_locator = driver.find_element(By.NAME, 'password')
        password_locator.send_keys('Password123')

        # clic al boton submit
        button_locator = driver.find_element(By.ID, 'submit')
        button_locator.click()

        # verificar la nueva url practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        msg_exito = driver.find_element(By.XPATH, "//h1[contains(.,'Logged In Successfully')]")
        msg = msg_exito.text
        assert msg == "Logged In Successfully"


        # Verify button Log out is displayed on the new page
        logout_button = driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a')
        assert logout_button"""