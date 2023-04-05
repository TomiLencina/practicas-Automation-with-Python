"""import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage

from page_objects.register_obj import Register

class run_register:
    @pytest.mark.register

    def test_register(self,driver):
        register = Register(driver)
        register.open()
        register.execute_register("tom","lenci",3512689,"tom@gmail.com",
                                  "lol","cordoba","cba",555,"arg","toml","contra123","contra123")"""


import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage

from page_objects.register_obj import RecordPositive


class TestRecordRun:
    @pytest.mark.login
    def test_record_positive(self, driver):
        login_page = RecordPositive(driver)
        login_page.open()
        login_page.execute_record("Pablo", "Vegetti", "+549-3518524795", "elpiratacordobes@yahoo.com",
                                  "calle siempre viva 123", "Córdoba", "Córdoba", "5001", "el pirata", "12345", "12345")
        # logged_in_page = LoggedInSuccessfullyPage(driver)
        # assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
