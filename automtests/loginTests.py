__author__ = 'jgarcia'

import unittest

from pythonTraining.pages.loginPage import LoginPage


class Login(unittest.TestCase):

    def test_login_requiredFields(self):
        loginpg = LoginPage()
        loginpg.login_requiredFields()

    def test_login_wrongUsername_Password(self):
        loginpg = LoginPage()
        loginpg.login_wrongUsername_Password()

    def test_login_successfully(self):
        loginpg = LoginPage()
        loginpg.login_successfully()


