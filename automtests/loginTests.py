__author__ = 'jgarcia'

import unittest

from pythonTraining.pages.loginPage import LoginPage


class Login(unittest.TestCase):

    def test_login_requiredFields(self):  # This test case verifies required fields on Login screen
        loginpg = LoginPage()
        loginpg.login_requiredFields()

    def test_login_wrongUsername_Password(self):  # This test case verifies user can not login with wrong username
        loginpg = LoginPage()
        loginpg.login_wrongUsername_Password()

    def test_login_successfully(self):  # This test case verifies user can login with valid credentials
        loginpg = LoginPage()
        loginpg.login_successfully()


