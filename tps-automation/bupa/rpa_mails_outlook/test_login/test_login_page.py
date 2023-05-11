import time
import pytest
from rpa_mails_outlook.page_objects.login_outlook import LoginOutlook

import pandas as pd
import openpyxl
#import win32com.client as win32


class TestLoginPage:

    @pytest.mark.loginOutlook
    def test_login_page(self, driver):
        #Aplicando Herencia
        login_page = LoginOutlook(driver)
        login_page.open()
        time.sleep(3)
        df = pd.read_excel('Casos_Bajas_140323.xlsx')  # ruta del archivo Excel
        df['Aseg_RutTitular_cr'] = df['Aseg_RutTitular_cr'].astype(str).apply(lambda x: x[:-1] + '-' + x[-1])#Se agrega " - " a los rut
        #"Aseg_RutTitular_cr" primer valor de la columna
        # rut1 = df.loc[0, 'Aseg_RutTitular_cr'] (primer rut de la columna)

        time.sleep(3)
        login_page.execute_login("mail-ejemplo@mail.com", "contrasena")#logion de Outlook
        for nro_rut in df['Aseg_RutTitular_cr']:
            login_page.execute_redaction("tlencina@vates.com", "Baja para pruebas en QA " + nro_rut, "Favor ejecutar Baja para pruebas en QA " + nro_rut)#Cuenta Outlook a utilizar para enciar los mails
            time.sleep(5)




