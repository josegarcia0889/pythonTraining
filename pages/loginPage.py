from gluon.html import B

__author__ = 'jgarcia'

from pythonTraining.pages.commons.loginBasePage import LogInBasePage
from pythonTraining.commons.testBase import Base
from pythonTraining.commons.utilities import Utilities


class LoginPage(LogInBasePage):
    def __init__(self):
        self.utilities = Utilities()

        self.driver = None

    def login_requiredFields(self):
        self.driver = Base().setUp()

        self.utilities.home_page(self.driver)
        self.open_logOn_Screen()
        self.click_logOn_button()
        self.validate_required_fields()

        Base().tearDown(self.driver)


    def login_wrongUsername_Password(self):
        self.driver = Base().setUp()

        self.utilities.home_page(self.driver)
        self.open_logOn_Screen()
        self.write_username_password('UserTest', '123')
        self.click_logOn_button()
        self.validate_wrong_username_password()

        Base().tearDown(self.driver)
















