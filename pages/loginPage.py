from gluon.html import B

__author__ = 'jgarcia'

from pythonTraining.pages.commons.loginBasePage import LogInBasePage
from pythonTraining.commons.testBase import Base
from pythonTraining.commons.utilities import Utilities


class LoginPage(LogInBasePage):
    def __init__(self):
        self.utilities = Utilities()

        self.driver = None

    def login_successfully(self):

        self.driver = Base().setUp()

        self.utilities.home_page(self.driver)

        self.open_logOn_Screen(self.driver)












