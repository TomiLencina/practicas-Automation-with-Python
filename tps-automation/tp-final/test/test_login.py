import time
import pandas as pd
#import win32com.client as win32
import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_outlook import LoginOutlook


class TestLoginPage:

    @pytest.mark.loginOutlook
    def test_login_page(self, driver):
        #  Aplicando Herencia
        """login_page = LoginOutlook(driver)

        login_page.open()
        time.sleep(3)
        login_page.execute_login("mail@prueba.com", "%password%","mail@prueba.com", "test asunto","test de mensaje")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        time.sleep(5)"""
        df = pd.read_excel('Casos_Bajas_140323.xlsx')  # ruta del archivo Excel
        df['Aseg_RutTitular_cr'] = df['Aseg_RutTitular_cr'].astype(str).apply(lambda x: x[:-1] + '-' + x[-1])
        print(df)

        mail = outlook.CreateItem(0)
        mail.To = 'ibecerra@vates.com'
        mail.Subject = 'Lista de DNI'
        mail.Body = '\n'.join(df['DNI'])
        mail.Send()
        #assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"