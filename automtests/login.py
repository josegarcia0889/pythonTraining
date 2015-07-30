__author__ = 'jgarcia'

import unittest

from pythonTraining.pages.loginPage import LoginPage


class Login(unittest.TestCase):
    def test_login_successfully(self):
        loginPg = LoginPage()
        loginPg.login_successfully()
