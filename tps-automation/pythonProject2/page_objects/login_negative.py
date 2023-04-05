from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedinSuccessfullyPage:
    __url = 'https://practicetestautomation.com/logged-in-successfully/'
    __message_locator = (By.XPATH, '//*[@id="error"]')

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def get_error_text(self) -> str:
        """return the text inside the error display"""
        return self.__driver.find_element(self.__message_locator).text

    def check_error_msg(self, text: str) -> bool:
        """check that the error msg is displayed when bad login is performed"""
        return text == self.get_error_text()