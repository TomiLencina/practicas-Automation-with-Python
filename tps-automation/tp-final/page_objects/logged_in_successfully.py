from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://demo.guru99.com/test/newtours/login_sucess.php"
    __header_locator = (By.XPATH, "//h3[contains(.,'Login Successfully')]")
    __log_out_button_locator = (By.XPATH, "//a[@href='index.php'][contains(.,'SIGN-OFF')]")

    def __init__(self, driver: WebDriver):
        # con Herencia
        super().__init__(driver)
        # sin herencia

    #  self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def expected_url(self) -> str:
        return self._url

    def header(self) -> str:
        return super()._get_text(self.__header_locator)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__log_out_button_locator)