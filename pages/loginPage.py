__author__ = 'jgarcia'

from pythonTraining.pages.commons import basePage
from pythonTraining.commons.utilities import utilities


class LoginPage(utilities):

    def __init__(self):
        pass

    def login_successfully(self):

        self.homePage()

        basePage.open_logOn_Screen(self)









