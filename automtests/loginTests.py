__author__ = 'jgarcia'

import unittest

from pythonTraining.pages.loginPage import LoginPage


class Login(unittest.TestCase):

    def test_login_requiredFields(self):
        loginPg = LoginPage()
        loginPg.login_requiredFields()

    def test_login_wrongUsername_Password(self):
        loginPg = LoginPage()
        loginPg.login_wrongUsername_Password()
