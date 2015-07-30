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

    def test_registerScreenDisplayed(self):
        loginpg = LoginPage()
        loginpg.registerScreen_Displayed()

    def test_successfully_registerUser(self):
        loginpg = LoginPage()
        loginpg.successfully_register_user()
