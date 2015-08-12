__author__ = 'jgarcia'

import unittest

from pythonTraining.pages.registerUserPage import RegisterUserPage


class RegisterUser(unittest.TestCase):
    def test_registerScreenDisplayed(self):
        registerpg = RegisterUserPage()
        registerpg.registerScreen_Displayed()

    def test_registerUser_successfully(self):
        registerpg = RegisterUserPage()
        registerpg.register_user_successfully()
