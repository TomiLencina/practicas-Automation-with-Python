import pytest
from selenium.webdriver.common.by import By


class Test_Case2:

    @pytest.mark.testcase2
    def test(self, driver):
        # open browser
        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        # click add button
        driver.find_element(By.ID, 'add_btn').click()

        # await 2nd row to load
        driver.implicitly_wait(10)

        # type text into the 2nd row
        driver.find_element(By.ID, 'row2').send_keys('text')

        # Push Save button using locator By.name(“Save”)
        driver.find_element(By.ID, 'Save')

        # Verify text saved
        assert driver.find_element(By.ID, 'confirmation').text == 'Row 2 was saved'