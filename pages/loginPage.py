__author__ = 'jgarcia'

from pythonTraining.pages.commons.loginBasePage import LogInBasePage
from pythonTraining.commons.testBase import Base
from pythonTraining.commons.utilities import Utilities
import pythonTraining.commons.properties as property


class LoginPage(LogInBasePage):
    def __init__(self):
        self.utilities = Utilities()
        self.driver = None

    def login_required_fields(self):
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

    def login_successfully(self):
        self.driver = Base().setUp()

        self.utilities.home_page(self.driver)
        self.open_logOn_Screen()
        self.write_username_password(property.test_username,property.test_password)
        self.click_logOn_button()
        self.verify_logged_user(property.test_username)

        Base().tearDown(self.driver)




















