import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from rpa_mails_outlook.page_objects.base_page import BasePage



class LoginOutlook(BasePage):
    __url = "https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=1&msaredir=1&client-request-id=acf6939e-a1ed-ae65-dbd8-efb39a5db37e&protectedtoken=true&claims=%7b%22id_token%22%3a%7b%22xms_cc%22%3a%7b%22values%22%3a%5b%22CP1%22%5d%7d%7d%7d&domain_hint=vates.com&nonce=638144913464805227.d74dc64e-81bc-494f-a20f-c96505ce68be&state=Dcu7DoIwGEDhou_iVmnL39tAHDSGARc00bD1RgKxwUCD8e3t8J3tFAihfbbLCpKDpKgUBdC0AgGKcMbk0UvwTkDAilqHQcOADSMDdlpwwl0QyoYiv5dy_prytCaTQk0PS_DjElx6zLVpOuKam2h_evOvbrVML23UsY_vqb_zyTKy2ef1Y8_qDw"
    __username = (By.XPATH, "//input[contains(@id,'i0116')]")
    __submit_button_siguiente = (By.XPATH, "//input[contains(@id,'idSIButton9')]")
    __password = (By.XPATH,
                  "//input[contains(@id,'i0118')]")
    __submit_button = (By.XPATH,
                       "//input[contains(@id,'idSIButton9')]")
    __sumit_button_si = (By.XPATH, "//input[contains(@id,'idSIButton9')]")
    __btn_nuevo_correo = (By.XPATH, "//span[@class='label-186']")
#destinatario del correo
    __destinatario = (By.XPATH, "//div[@aria-label='Para']")
    __click_destinatario = (By.XPATH, "//span[contains(@class,'LudGC full')]")
#asunto del correo
    __asunto = (By.XPATH, "//input[contains(@placeholder,'Agregar un asunto')]")
#mensaje del correo
    __mensaje = (By.XPATH, "//div[contains(@aria-label,'Cuerpo del mensaje, presione Alt+F10 para salir')]")
#enviar correo
    #__btn_enviar_correo_fle = (By.XPATH, "//span[@class='ms-Button-flexContainer flexContainer-164'][contains(.,'')]")
    __btn_enviar_correo = (By.XPATH, "//i[contains(@data-icon-name,'send')]")


    def __init__(self, driver: WebDriver):
        # con herencia
        super().__init__(driver)
        # sin herencia
        # self._driver = driver

    def open(self):
        # herencia
        super()._open_url(self.__url)
        # sin herencia
        # self.driver.get(self.__url)

    def exit(self):
        super()._exit()

    def execute_login(self, username: str, password: str):
        # utilizando herencia
        super()._type(self.__username, username)
        super()._click(self.__submit_button_siguiente)
        super()._type(self.__password, password)
        super()._click(self.__submit_button)
        super()._click(self.__sumit_button_si)

    def execute_redaction(self, destinatario: str, asunto: str, mensaje: str):
        #time.sleep(3)
        super()._click(self.__btn_nuevo_correo)
        time.sleep(3)
        super()._type(self.__destinatario, destinatario)
        super()._click(self.__click_destinatario)
        super()._type(self.__asunto, asunto)
        super()._type(self.__mensaje, mensaje)
        #super()._click(self.__btn_enviar_correo_fle)
        super()._click(self.__btn_enviar_correo)


    #def get_error_message(self) -> str:
    #    return super().get_text(self._error_message, time=3)