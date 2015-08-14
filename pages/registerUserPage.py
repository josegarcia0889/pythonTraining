__author__ = 'jgarcia'

from pythonTraining.pages.commons.registerUserBasePage import RegisterUserBasePage
from pythonTraining.pages.commons.loginBasePage import LogInBasePage
from pythonTraining.commons.testBase import Base
from pythonTraining.commons.utilities import Utilities
from random import random


class RegisterUserPage(RegisterUserBasePage):
    def __init__(self):
        self.utilities = Utilities()

        self.driver = None

        self.loginbasepg = LogInBasePage()

        self.registerbasepg = RegisterUserBasePage()

    def register_screen_displayed(self):

        self.driver = Base().setUp()

        self.loginbasepg.load_driver(self.driver)

        self.utilities.home_page(self.driver)
        self.loginbasepg.open_logOn_Screen()
        self.open_register_screen()

        Base().tearDown(self.driver)

    def register_user_successfully(self):
        self.driver = Base().setUp()

        self.loginbasepg.load_driver(self.driver)

        self.utilities.home_page(self.driver)
        self.loginbasepg.open_logOn_Screen()
        self.open_register_screen()

        username ="jgarcia"+str(random())

        self.registerForm_fillIn(username,"jgarcia+"+str(random())+"@wearegap.com","123456")
        self.click_registerButton()

        self.loginbasepg.verify_logged_user(username)

        Base().tearDown(self.driver)
