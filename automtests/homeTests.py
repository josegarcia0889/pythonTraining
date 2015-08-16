__author__ = 'jgarcia'

import unittest

from pythonTraining.pages.homePage import HomePage


class AboutUs(unittest.TestCase):

    def test_aboutUs_screenDisplayed(self):
        aboutpg = HomePage()
        aboutpg.compare_img_url()
