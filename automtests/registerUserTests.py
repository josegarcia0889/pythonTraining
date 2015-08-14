__author__ = 'jgarcia'

import unittest

from pythonTraining.pages.registerUserPage import RegisterUserPage


class RegisterUser(unittest.TestCase):
    def test_registerScreenDisplayed(self):  # This test case verifies register screen is displayed
        registerpg = RegisterUserPage()
        registerpg.register_screen_displayed()

    def test_registerUser_successfully(self):  # This test case verifies a new user can be register
        registerpg = RegisterUserPage()
        registerpg.register_user_successfully()
