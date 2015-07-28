__author__ = 'jgarcia'

import unittest

from pythonTraining.pages.loginPage import LoginPage


class login(unittest.TestCase, LoginPage):

    def test_loginSuccessfully(self):
        self.login_successfully()


    

