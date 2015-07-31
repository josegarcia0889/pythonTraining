__author__ = 'jgarcia'

import unittest
from pythonTraining.commons.testBase import Base
import properties as property


class Utilities(Base, unittest.TestCase):
    def __init__(self):
        self.driver = None

    def home_page(self, driver2):
        self.driver = driver2

        self.driver.get(property.qa_site)

        self.driver.maximize_window()

        self.assertIn(self.driver.title, "Nerd Dinner")

        assert "No results found." not in self.driver.page_source


