from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=1&msaredir=1&client-request-id=79f37043-272c-733b-c1b2-f491ec540964&protectedtoken=true&claims=%7b%22id_token%22%3a%7b%22xms_cc%22%3a%7b%22values%22%3a%5b%22CP1%22%5d%7d%7d%7d&nonce=638144890261454540.fc8273d5-5e56-4ea7-9a8c-2576f44ea405&state=DYtLDoAgDAWLxuNUCvTHcQjC1qXXt5nMJG_xEgCc4REmioBp88LsnaoWloDuPb1aewRliSKvYdiHT6xiujk2k6T4Xvn9Rv4B&sso_reload=true"
    __username_field = (By.XPATH, "//input[@name='userName']")
    __password_field = (By.XPATH, "//input[@type='password']")
    __submit_button = (By.XPATH, "//input[@type='submit']")



    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)
