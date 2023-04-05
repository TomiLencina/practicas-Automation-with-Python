"""from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class Register(BasePage):
    __url = "https://demo.guru99.com/test/newtours/"
    __btn_register = (By.XPATH, "//a[@href='register.php'][contains(.,'REGISTER')]")
    __first_name = (By.XPATH, "//input[contains(@name,'firstName')]")
    __last_name = (By.XPATH, "//input[contains(@name,'lastName')]")
    __phone = (By.XPATH, "//input[contains(@name,'phone')]")
    __email = (By.XPATH, "//input[contains(@id,'userName')]")
    __address = (By.XPATH, "//input[contains(@name,'phone')]")
    __city = (By.XPATH, "//input[contains(@name,'city')]")
    __state = (By.XPATH, "//input[contains(@maxlength,'40')]")
    __postal = (By.XPATH, "//input[contains(@name,'postalCode')]")
    __country = (By.XPATH, "//select[contains(@name,'country')]")
    __userName = (By.XPATH, "//input[contains(@id,'email')]")
    __password = (By.XPATH, "//input[@name='password']")
    __confirm_password = (By.XPATH, "//input[contains(@name,'confirmPassword')]")
    __btn_submit = (By.XPATH, "//input[@src='images/submit.gif']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_register(self, first_name: str, last_name: str, phone: int, email: str, address: str,
                         city: str, state: str, postal_code: int, country: str, username: str,
                         password: str, confirm_pass: str):
        super()._click(self.__btn_register)
        super()._type(self.__first_name, first_name)
        super().type(self.__last_name, last_name)
        super().type(self.__phone, phone)
        super()._type(self.__email, email)
        super().type(self.__address, address)
        super()._type(self.__city, city)
        super()._type(self.__state, state)
        super()._type(self.__postal, postal_code)
        super()._type(self.__country, country)
        super()._type(self.__userName, username)
        super()._type(self.__password, password)
        super()._type(self.__confirm_password, confirm_pass)
        super()._click(self.__btn_submit)"""


from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class RecordPositive(BasePage):
    __url = "https://demo.guru99.com/test/newtours/"
    __btn_record = (By.XPATH, "//a[@href='register.php'][contains(.,'REGISTER')]")
    __first_name = (By.XPATH, "//input[@name='firstName']")
    __last_name = (By.XPATH, "//input[@name='lastName']")
    __phone = (By.XPATH, "//input[@name='phone']")
    __email = (By.XPATH, "//input[contains(@id,'userName')]")
    __address = (By.XPATH, "//input[@name='address1']")
    __city = (By.XPATH, "//input[@name='city']")
    __state = (By.XPATH, "//input[@name='state']")
    __postal_code = (By.XPATH, "//input[@name='postalCode']")
    __country_click = (By.XPATH, "//select[@size='1']")
    __user_name = (By.XPATH, "//input[contains(@id,'email')]")
    __password = (By.XPATH, "//input[contains(@name,'password')]")
    __confirmation_pass = (By.XPATH, "//input[contains(@name,'confirmPassword')]")
    __record_btn = (By.XPATH, "//input[contains(@name,'submit')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_record(self, first_name: str, last_name: str, phone: str, email: str, address: str, city: str,
                       state: str, postal_code: str, user_name: str, password: str, conf_pass: str):
        super()._click(self.__btn_record)
        super()._type(self.__first_name, first_name)
        super()._type(self.__last_name, last_name)
        super()._type(self.__phone, phone)
        super()._type(self.__email, email)
        super()._type(self.__address, address)
        super()._type(self.__city, city)
        super()._type(self.__state, state)
        super()._type(self.__postal_code, postal_code)
        super()._click(self.__country_click)
        super()._type(self.__user_name, user_name)
        super()._type(self.__password, password)
        super()._type(self.__confirmation_pass, conf_pass)
        super()._click(self.__record_btn)