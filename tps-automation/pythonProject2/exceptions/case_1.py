import pytest
from selenium.webdriver.common.by import By


class Test_Case1:

    @pytest.mark.case1
    def test(self, driver):
        # open page in url
        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        # click add button
        driver.find_element(By.ID, 'add_btn').click()

        # verify row 2input field is displayed
        assert driver.find_element(By.ID, 'row2').is_displayed()