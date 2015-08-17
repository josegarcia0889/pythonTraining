__author__ = 'jgarcia'

import unittest

from pythonTraining.pages.homePage import HomePage


class AboutUs(unittest.TestCase):

    def test_compareimages(self):
        aboutpg = HomePage()
        aboutpg.compare_img_url()
