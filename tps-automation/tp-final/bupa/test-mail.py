import time

import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_outlook import LoginOutlook


class TestLoginPage:

    @pytest.mark.loginOutlook
    def test_login_page(self, driver):
        #  Aplicando Herencia
        login_page = LoginOutlook(driver)

        login_page.open()
        time.sleep(3)
        login_page.execute_login("tlencina@vates.com", "%Martes2022%")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        time.sleep(7)

        #assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"