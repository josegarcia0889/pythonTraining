__author__ = 'jgarcia'


import unittest

from pythonTraining.pages.aboutUsPage import AboutUsPage


class AboutUs(unittest.TestCase):

    def test_aboutUs_screenDisplayed(self):
        aboutpg = AboutUsPage()
        aboutpg.verify_aboutUs_displayed()