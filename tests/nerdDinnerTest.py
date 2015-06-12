__author__ = 'jgarcia'
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class openPage(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()


	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("http://nerddinner.com")

		self.assertIn("Nerd Dinner", driver.title)

		assert "No results found." not in driver.page_source


	def tearDown(self):
		self.driver.close()