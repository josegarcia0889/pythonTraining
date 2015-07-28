__author__ = 'jgarcia'

from pythonTraining.pages.commons import basePage
from pythonTraining.commons.utilities  import Utilities


class LoginPage(Utilities):

    def __init__(self):
        pass

    def login_successfully(self):
        self.home_page()

        basePage.open_logOn_Screen(self)









